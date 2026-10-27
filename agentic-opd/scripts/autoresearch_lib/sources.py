from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import META, NOTES, PAPER_BRIEFS, ROOT, SURVEY_BRIEFS
from .frontmatter import split_frontmatter


PAPERS = ROOT / "papers"
QUEUE = ROOT / "synthesis" / "queue.md"
GENERATED = META / "generated"
QUEUE_HINTS = ("queue", "target", "candidate")


@dataclass
class Card:
    path: Path
    fm: dict[str, Any]
    body: str

    @property
    def slug(self) -> str:
        return self.path.stem

    @property
    def arxiv_id(self) -> str:
        value = str(self.fm.get("arxiv_id") or "").strip()
        if value:
            return value
        match = re.search(r"(?m)^\s*arxiv_id:\s*(\S+)\s*$", self.body)
        return match.group(1).strip() if match else ""

    @property
    def title(self) -> str:
        return str(self.fm.get("title") or "").strip()


@dataclass
class QueueRow:
    status: str
    title: str
    arxiv_id: str
    year: str
    source: str
    note: str
    raw: str

    @property
    def slug(self) -> str:
        return ""


def note_files() -> list[Path]:
    if not NOTES.exists():
        return []
    return sorted(p for p in NOTES.glob("*.md") if p.is_file())


def is_queue_path(path: Path) -> bool:
    name = path.name.lower()
    return any(hint in name for hint in QUEUE_HINTS)


def read_card(path: Path) -> Card:
    fm, body = split_frontmatter(path.read_text(errors="ignore"))
    return Card(path=path, fm=fm, body=body)


def formal_cards() -> list[Card]:
    cards = []
    for path in note_files():
        card = read_card(path)
        status = str(card.fm.get("status") or "").lower()
        if is_queue_path(path) or status in {"queue", "provisional"}:
            continue
        cards.append(card)
    return cards


def provisional_paths() -> list[Path]:
    if not NOTES.exists():
        return []
    return sorted(
        p for p in NOTES.rglob("*.md") if any("provisional" in part.lower() for part in p.parts) or "provisional" in p.name.lower()
    )


def queue_rows() -> list[QueueRow]:
    if not QUEUE.exists():
        return []
    rows: list[QueueRow] = []
    for line in QUEUE.read_text().splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and cells[0].lower() in {"status", "paper", "title"}:
            continue
        if len(cells) < 2 or not cells[1]:
            continue
        cells += [""] * (6 - len(cells))
        rows.append(QueueRow(cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], stripped))
    return rows


def off_scope_count() -> int:
    folder = META / "off-scope"
    return len(list(folder.glob("*.md"))) if folder.exists() else 0


def paper_briefs() -> list[Path]:
    return sorted(PAPER_BRIEFS.glob("*.md")) if PAPER_BRIEFS.exists() else []


def survey_briefs() -> list[Path]:
    if not SURVEY_BRIEFS.exists():
        return []
    return sorted([*SURVEY_BRIEFS.glob("*.json"), *SURVEY_BRIEFS.glob("*.md")])


def pdfs() -> list[Path]:
    return sorted(PAPERS.glob("*.pdf")) if PAPERS.exists() else []
