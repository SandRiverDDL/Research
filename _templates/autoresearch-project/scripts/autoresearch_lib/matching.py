from __future__ import annotations

from pathlib import Path

from .config import PAPER_BRIEFS, ROOT, SURVEY_BRIEFS
from .sources import Card, QueueRow, pdfs
from .text import compact_text, slugify


def paper_keys(title: str = "", arxiv_id: str = "", slug: str = "") -> set[str]:
    keys = set()
    if arxiv_id:
        keys.add(f"arxiv:{arxiv_id}")
    if title:
        keys.add(f"title:{compact_text(title)[:120]}")
    if slug:
        keys.add(f"slug:{compact_text(slug)}")
    return {key for key in keys if key.split(":", 1)[1]}


def card_keys(card: Card) -> set[str]:
    return paper_keys(card.title, card.arxiv_id, card.slug)


def row_keys(row: QueueRow) -> set[str]:
    return paper_keys(row.title, row.arxiv_id, slugify(row.title))


def matches_query(query: str, *values: str) -> bool:
    q = query.lower().strip()
    qc = compact_text(query)
    return any((q and q in value.lower()) or (qc and qc in compact_text(value)) for value in values if value)


def card_matches(query: str, cards: list[Card]) -> list[Card]:
    return [card for card in cards if matches_query(query, card.title, card.arxiv_id, card.slug, str(card.path))]


def queue_matches(query: str, rows: list[QueueRow]) -> list[QueueRow]:
    return [row for row in rows if matches_query(query, row.title, row.arxiv_id, row.raw)]


def brief_matches(title: str = "", arxiv_id: str = "", slug: str = "") -> list[Path]:
    candidates: list[Path] = []
    if PAPER_BRIEFS.exists():
        if arxiv_id:
            candidates.extend(PAPER_BRIEFS.glob(f"{arxiv_id}_*.md"))
        if slug:
            candidates.extend(PAPER_BRIEFS.glob(f"*_{slug}.md"))
        title_compact = compact_text(title)
        if title_compact:
            for path in PAPER_BRIEFS.glob("*.md"):
                if title_compact[:48] and title_compact[:48] in compact_text(path.stem):
                    candidates.append(path)
    return sorted(set(candidates))


def survey_brief_matches(title: str = "", arxiv_id: str = "", slug: str = "") -> list[Path]:
    candidates: list[Path] = []
    if SURVEY_BRIEFS.exists():
        if arxiv_id:
            candidates.extend(SURVEY_BRIEFS.glob(f"{arxiv_id}_*.json"))
        if slug:
            candidates.extend(SURVEY_BRIEFS.glob(f"*_{slug}.json"))
    return sorted(set(candidates))


def pdf_matches(title: str = "", arxiv_id: str = "", slug: str = "") -> list[Path]:
    candidates: list[Path] = []
    all_pdfs = pdfs()
    if arxiv_id:
        candidates.extend(path for path in all_pdfs if arxiv_id in path.name)
    if slug:
        candidates.extend(path for path in all_pdfs if slug in path.name)
    title_compact = compact_text(title)
    if title_compact:
        candidates.extend(path for path in all_pdfs if title_compact[:48] and title_compact[:48] in compact_text(path.stem))
    return sorted(set(candidates))


def duplicate_groups(cards: list[Card]) -> list[tuple[str, list[Path]]]:
    by_key: dict[str, list[Path]] = {}
    for card in cards:
        for key in card_keys(card):
            by_key.setdefault(key, []).append(card.path)
    groups = []
    seen: set[tuple[str, ...]] = set()
    for key, paths in by_key.items():
        unique = sorted(set(paths))
        if len(unique) <= 1:
            continue
        sig = tuple(str(path) for path in unique)
        if sig in seen:
            continue
        seen.add(sig)
        groups.append((key, unique))
    return groups
