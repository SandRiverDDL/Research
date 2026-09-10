from __future__ import annotations

import json
from dataclasses import dataclass

from .config import GENERATED, NOTES
from .matching import brief_matches, duplicate_groups, pdf_matches
from .sources import formal_cards, note_files, read_card
from .text import rel, utc_now


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]
    card_count: int


def has_evidence(card) -> bool:
    if "<!-- pdf:" in card.body or "<!-- html:" in card.body or "<!-- brief:" in card.body:
        return True
    return bool(brief_matches(card.title, card.arxiv_id, card.slug) or pdf_matches(card.title, card.arxiv_id, card.slug))


def validate_project() -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    cards = formal_cards()

    for path in note_files():
        card = read_card(path)
        if not card.fm:
            errors.append(f"{rel(path)}: missing YAML frontmatter")
            continue
        status = str(card.fm.get("status") or "").lower()
        if status == "provisional" and path.parent == NOTES:
            errors.append(f"{rel(path)}: provisional note must not live in notes/ root")

    for card in cards:
        for key in ["title", "year"]:
            if card.fm.get(key) in {None, "", "unknown"}:
                errors.append(f"{rel(card.path)}: missing frontmatter `{key}`")
        if not (card.fm.get("url") or card.fm.get("arxiv_id")):
            warnings.append(f"{rel(card.path)}: missing url/arxiv_id")
        if not has_evidence(card):
            errors.append(f"{rel(card.path)}: missing PDF/HTML/brief evidence anchor")

    for key, paths in duplicate_groups(cards):
        joined = ", ".join(rel(path) for path in paths)
        warnings.append(f"duplicate {key}: {joined}")

    return ValidationResult(errors, warnings, len(cards))


def write_validation(result: ValidationResult) -> None:
    payload = {
        "generated_at": utc_now(),
        "summary": {
            "errors": len(result.errors),
            "warnings": len(result.warnings),
            "cards": result.card_count,
        },
        "errors": result.errors,
        "warnings": result.warnings,
    }
    GENERATED.mkdir(parents=True, exist_ok=True)
    (GENERATED / "card-validation.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Card Validation", "", f"> Generated: {payload['generated_at']}", "", "## Summary", ""]
    lines.extend(
        [
            f"- Cards checked: {result.card_count}",
            f"- Errors: {len(result.errors)}",
            f"- Warnings: {len(result.warnings)}",
        ]
    )
    if result.errors:
        lines.extend(["", "## Errors", ""])
        lines.extend(f"- {item}" for item in result.errors)
    if result.warnings:
        lines.extend(["", "## Warnings", ""])
        lines.extend(f"- {item}" for item in result.warnings)
    if not result.errors and not result.warnings:
        lines.extend(["", "No hygiene issues found."])
    (GENERATED / "card-validation.md").write_text("\n".join(lines) + "\n")
