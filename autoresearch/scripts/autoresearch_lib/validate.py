from __future__ import annotations

import json
import re
from dataclasses import dataclass

from .config import GENERATED, NOTES, TRIAGE_RULES
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
    if "<!-- meta:" in card.body and any(meta_value(card, key) for key in ["pdf", "html", "brief"]):
        return True
    return bool(brief_matches(card.title, card.arxiv_id, card.slug) or pdf_matches(card.title, card.arxiv_id, card.slug))


def meta_value(card, key: str) -> str:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(.+?)\s*$", card.body)
    return match.group(1).strip() if match else ""


def has_source_identifier(card) -> bool:
    return bool(card.fm.get("url") or card.fm.get("arxiv_id") or meta_value(card, "url") or meta_value(card, "arxiv_id"))


def has_brief_anchor(card) -> bool:
    return bool(brief_matches(card.title, card.arxiv_id, card.slug) or "<!-- brief:" in card.body or meta_value(card, "brief"))


def load_rules() -> dict:
    if not TRIAGE_RULES.exists():
        return {}
    return json.loads(TRIAGE_RULES.read_text())


def is_survey(card) -> bool:
    return str(card.fm.get("paper_type") or "").strip() == "survey"


def is_missing(value) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() in {"", "unknown"}
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False


def validate_project() -> ValidationResult:
    rules = load_rules()
    required = rules.get("required_frontmatter", [])
    allowed = rules.get("allowed", {})
    nested_required = rules.get("required_nested_frontmatter", {})
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
        required_keys = required or ["title", "year"]
        for key in required_keys:
            if is_missing(card.fm.get(key)):
                errors.append(f"{rel(card.path)}: missing frontmatter `{key}`")
        for key, values in allowed.items():
            value = card.fm.get(key)
            if value not in {None, ""} and str(value).strip() not in values:
                errors.append(f"{rel(card.path)}: illegal {key} `{value}`")
        for key, child_keys in nested_required.items():
            value = card.fm.get(key)
            if not isinstance(value, dict):
                errors.append(f"{rel(card.path)}: `{key}` must be a mapping")
                continue
            for child_key in child_keys:
                if is_missing(value.get(child_key)):
                    errors.append(f"{rel(card.path)}: missing {key}.{child_key}")
        if not has_source_identifier(card):
            warnings.append(f"{rel(card.path)}: missing url/arxiv_id")
        if not has_evidence(card):
            errors.append(f"{rel(card.path)}: missing PDF/HTML/brief evidence anchor")
        if not is_survey(card) and not has_brief_anchor(card):
            warnings.append(f"{rel(card.path)}: missing bounded original paper brief")
        for banned in ["## Selection Basis", "## Bounded Brief", "## RL Mechanism", "## 和 Agent Data 的关系"]:
            if banned in card.body:
                errors.append(f"{rel(card.path)}: banned legacy section `{banned}`")

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
