from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from autoresearch_lib.registry import lookup, scan_cards, validate_cards


OLD_CARD = """---
title: Old Paper
authors: [Ada Author, et al.]
year: 2025
venue: icml-2025
arxiv_id: 2501.01234
url: https://arxiv.org/abs/2501.01234
addresses: [exposure-bias]
decisions:
  rollout: student
---

## Any legacy heading

Legacy body.
"""

NEW_CARD = """---
title: New Paper
authors: [Bea Builder, et al.]
year: 2026
venue: icml-2026
paper_id: arxiv:2601.12345
source: https://arxiv.org/abs/2601.12345
---

- **问题**：Observed failure mode.
- **增量**：Baseline → intervention → mechanism.
- **证据**：§4 Table 2.
- **Pattern**：[解释] Reusable pattern.
"""


class RegistryTests(unittest.TestCase):
    def make_notes(self, files: dict[str, str]) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        notes = Path(temp.name)
        for name, text in files.items():
            (notes / name).write_text(text, encoding="utf-8")
        return temp, notes

    def test_old_and_new_cards_validate_without_body_schema(self) -> None:
        temp, notes = self.make_notes({"old.md": OLD_CARD, "new.md": NEW_CARD})
        self.addCleanup(temp.cleanup)
        result = validate_cards(notes)
        self.assertEqual(2, len(result.cards))
        self.assertEqual((), result.errors)

    def test_queue_note_is_not_a_formal_card(self) -> None:
        queue = """---\ntitle: Queue\nstatus: queue\n---\n\nUnreviewed rows.\n"""
        temp, notes = self.make_notes({"old.md": OLD_CARD, "queue.md": queue})
        self.addCleanup(temp.cleanup)
        self.assertEqual(1, len(scan_cards(notes)))

    def test_duplicate_across_legacy_and_minimal_schema(self) -> None:
        duplicate = NEW_CARD.replace("arxiv:2601.12345", "arxiv:2501.01234").replace(
            "2601.12345", "2501.01234"
        )
        temp, notes = self.make_notes({"old.md": OLD_CARD, "new.md": duplicate})
        self.addCleanup(temp.cleanup)
        result = validate_cards(notes)
        self.assertTrue(any("duplicate arxiv:2501.01234" in item for item in result.errors))

    def test_lookup_by_id_url_title_and_slug(self) -> None:
        temp, notes = self.make_notes({"26_new-paper.md": NEW_CARD})
        self.addCleanup(temp.cleanup)
        cards = scan_cards(notes)
        for query in [
            "2601.12345",
            "https://arxiv.org/abs/2601.12345v2",
            "New Paper",
            "26_new-paper",
        ]:
            self.assertEqual(["New Paper"], [card.title for card in lookup(cards, query)])

    def test_research_fields_and_headings_are_not_required(self) -> None:
        body = NEW_CARD.replace("- **问题**：Observed failure mode.\n", "").replace(
            "- **Pattern**：[解释] Reusable pattern.\n", "Free-form interpretation.\n"
        )
        temp, notes = self.make_notes({"new.md": body})
        self.addCleanup(temp.cleanup)
        self.assertEqual((), validate_cards(notes).errors)

    def test_missing_source_is_rejected(self) -> None:
        card = NEW_CARD.replace("source: https://arxiv.org/abs/2601.12345\n", "")
        temp, notes = self.make_notes({"new.md": card})
        self.addCleanup(temp.cleanup)
        self.assertTrue(any("source/url" in item for item in validate_cards(notes).errors))


if __name__ == "__main__":
    unittest.main()
