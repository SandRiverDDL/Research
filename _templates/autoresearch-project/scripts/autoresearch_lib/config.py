from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
META = ROOT / "_meta"
NOTES = ROOT / "notes"
PAPER_BRIEFS = META / "briefs" / "papers"
SURVEY_BRIEFS = META / "briefs" / "surveys"
GENERATED = META / "generated"
L1_CARD_TEMPLATE = ROOT / "doc" / "templates" / "l1-card.md"
