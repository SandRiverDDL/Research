from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from .frontmatter import split_frontmatter


ARXIV_RE = re.compile(r"(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)", re.IGNORECASE)
YEAR_RE = re.compile(r"^\d{4}$")


@dataclass(frozen=True)
class Card:
    path: Path
    frontmatter: dict[str, Any]
    body: str

    @property
    def title(self) -> str:
        return scalar(self.frontmatter.get("title"))

    @property
    def authors(self) -> list[str]:
        value = self.frontmatter.get("authors")
        if isinstance(value, list):
            return [scalar(item) for item in value if scalar(item)]
        text = scalar(value)
        return [text] if text else []

    @property
    def year(self) -> str:
        return scalar(self.frontmatter.get("year"))

    @property
    def venue(self) -> str:
        return scalar(self.frontmatter.get("venue"))

    @property
    def source(self) -> str:
        return scalar(self.frontmatter.get("source") or self.frontmatter.get("url"))

    @property
    def paper_id(self) -> str:
        explicit = scalar(self.frontmatter.get("paper_id"))
        if explicit:
            return canonical_paper_id(explicit)
        legacy_arxiv = scalar(self.frontmatter.get("arxiv_id"))
        if legacy_arxiv:
            return canonical_paper_id(f"arxiv:{legacy_arxiv}")
        return paper_id_from_url(self.source)

    @property
    def status(self) -> str:
        return scalar(self.frontmatter.get("status")).lower()

    @property
    def is_formal(self) -> bool:
        return self.status not in {"queue", "provisional"}


@dataclass(frozen=True)
class Validation:
    cards: tuple[Card, ...]
    errors: tuple[str, ...]
    warnings: tuple[str, ...]


def scalar(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def canonical_paper_id(value: str) -> str:
    raw = value.strip()
    if not raw:
        return ""
    if raw.startswith(("http://", "https://")):
        return paper_id_from_url(raw)
    if ":" not in raw:
        match = ARXIV_RE.fullmatch(raw)
        return f"arxiv:{match.group(1)}" if match else raw
    namespace, identifier = raw.split(":", 1)
    namespace = namespace.strip().lower()
    identifier = identifier.strip()
    if namespace == "arxiv":
        match = ARXIV_RE.search(identifier)
        return f"arxiv:{match.group(1)}" if match else raw
    if namespace == "doi":
        identifier = identifier.lower()
    return f"{namespace}:{identifier}" if namespace and identifier else raw


def paper_id_from_url(value: str) -> str:
    try:
        parsed = urlparse(value)
    except ValueError:
        return ""
    host = parsed.netloc.lower()
    if host.endswith("arxiv.org"):
        match = ARXIV_RE.search(parsed.path)
        if match:
            return f"arxiv:{match.group(1)}"
    if host.endswith("openreview.net"):
        forum_id = parse_qs(parsed.query).get("id", [""])[0]
        if forum_id:
            return f"openreview:{forum_id}"
    if host in {"doi.org", "dx.doi.org"}:
        doi = parsed.path.lstrip("/").lower()
        if doi:
            return f"doi:{doi}"
    return ""


def read_card(path: Path) -> Card:
    text = path.read_text(encoding="utf-8", errors="ignore")
    frontmatter, body = split_frontmatter(text)
    return Card(path=path, frontmatter=frontmatter, body=body)


def scan_cards(notes_dir: Path) -> list[Card]:
    if not notes_dir.exists():
        return []
    return [
        card
        for path in sorted(notes_dir.glob("*.md"))
        if path.is_file()
        for card in [read_card(path)]
        if card.is_formal
    ]


def validate_cards(notes_dir: Path) -> Validation:
    cards = scan_cards(notes_dir)
    errors: list[str] = []
    warnings: list[str] = []
    ids: dict[str, list[Path]] = {}
    titles: dict[str, list[Path]] = {}

    for card in cards:
        rel = card.path.name
        if not card.frontmatter:
            errors.append(f"{rel}: missing or invalid YAML frontmatter")
            continue
        if not card.title:
            errors.append(f"{rel}: missing title")
        if not card.authors:
            errors.append(f"{rel}: missing authors")
        if not YEAR_RE.fullmatch(card.year):
            errors.append(f"{rel}: missing or invalid year")
        if not card.venue:
            errors.append(f"{rel}: missing venue")
        if not card.paper_id or ":" not in card.paper_id:
            errors.append(f"{rel}: missing or invalid paper_id/arxiv_id")
        else:
            ids.setdefault(card.paper_id, []).append(card.path)
        if not valid_source_url(card.source):
            errors.append(f"{rel}: missing or invalid source/url")
        title_key = compact(card.title)
        if title_key:
            titles.setdefault(title_key, []).append(card.path)

    for paper_id, paths in sorted(ids.items()):
        if len(paths) > 1:
            errors.append(f"duplicate {paper_id}: {', '.join(path.name for path in paths)}")
    for title, paths in sorted(titles.items()):
        if len(paths) > 1:
            warnings.append(f"duplicate title: {', '.join(path.name for path in paths)}")

    return Validation(tuple(cards), tuple(errors), tuple(warnings))


def valid_source_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
    except ValueError:
        return False
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def lookup(cards: list[Card], query: str) -> list[Card]:
    query = query.strip()
    if not query:
        return []
    query_id = canonical_paper_id(query)
    if ":" in query_id:
        exact = [card for card in cards if card.paper_id == query_id]
        if exact:
            return exact

    lowered = query.lower()
    compacted = compact(query)
    matches = []
    for card in cards:
        values = [
            card.title,
            " ".join(card.authors),
            card.year,
            card.venue,
            card.paper_id,
            card.source,
            card.path.stem,
        ]
        if any(
            lowered in value.lower() or (compacted and compacted in compact(value))
            for value in values
            if value
        ):
            matches.append(card)
    return matches


def public_record(card: Card, root: Path) -> dict[str, object]:
    try:
        path = card.path.relative_to(root)
    except ValueError:
        path = card.path
    return {
        "paper_id": card.paper_id,
        "title": card.title,
        "authors": card.authors,
        "year": card.year,
        "venue": card.venue,
        "source": card.source,
        "card": str(path),
    }
