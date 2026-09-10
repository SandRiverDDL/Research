from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from .config import GENERATED, L1_CARD_TEMPLATE
from .matching import brief_matches, card_keys, card_matches, matches_query, pdf_matches, queue_matches, row_keys, survey_brief_matches
from .sources import QueueRow, formal_cards, off_scope_count, paper_briefs, pdfs, provisional_paths, queue_rows, survey_briefs
from .text import rel, slugify, utc_now
from .validate import validate_project


def status_payload() -> dict[str, Any]:
    result = validate_project()
    return {
        "generated_at": utc_now(),
        "formal_cards": len(formal_cards()),
        "queue_rows": len(queue_rows()),
        "paper_briefs": len(paper_briefs()),
        "survey_briefs": len(survey_briefs()),
        "pdfs": len(pdfs()),
        "off_scope": off_scope_count(),
        "validation_errors": len(result.errors),
        "validation_warnings": len(result.warnings),
    }


def lookup_data(query: str) -> dict[str, Any]:
    cards = formal_cards()
    rows = queue_rows()
    c_matches = card_matches(query, cards)
    q_matches = queue_matches(query, rows)
    title = c_matches[0].title if c_matches else (q_matches[0].title if q_matches else query)
    arxiv_id = c_matches[0].arxiv_id if c_matches else (q_matches[0].arxiv_id if q_matches else "")
    slug = c_matches[0].slug if c_matches else slugify(title)
    return {
        "query": query,
        "queue_matches": [asdict(row) for row in q_matches[:20]],
        "card_matches": [rel(card.path) for card in c_matches[:20]],
        "brief_matches": [rel(path) for path in brief_matches(title, arxiv_id, slug)],
        "survey_brief_matches": [rel(path) for path in survey_brief_matches(title, arxiv_id, slug)],
        "pdf_matches": [rel(path) for path in pdf_matches(title, arxiv_id, slug)],
    }


def audit_data() -> dict[str, Any]:
    cards = formal_cards()
    rows = queue_rows()
    card_key_set = set().union(*(card_keys(card) for card in cards)) if cards else set()

    queue_without_card = []
    queue_without_brief = []
    queue_without_pdf = []
    for row in rows:
        if "card written" in row.status.lower():
            continue
        if not row_keys(row).intersection(card_key_set):
            queue_without_card.append(row)
        slug = slugify(row.title)
        if not brief_matches(row.title, row.arxiv_id, slug):
            queue_without_brief.append(row)
        if not pdf_matches(row.title, row.arxiv_id, slug):
            queue_without_pdf.append(row)

    cards_without_brief = [
        card for card in cards if not brief_matches(card.title, card.arxiv_id, card.slug) and "<!-- brief:" not in card.body
    ]
    cards_without_pdf_anchor = [card for card in cards if "<!-- pdf:" not in card.body and "<!-- html:" not in card.body]

    return {
        "generated_at": utc_now(),
        "summary": {
            "queue_without_card": len(queue_without_card),
            "queue_without_brief": len(queue_without_brief),
            "queue_without_pdf": len(queue_without_pdf),
            "cards_without_brief": len(cards_without_brief),
            "cards_without_pdf_anchor": len(cards_without_pdf_anchor),
            "provisional": len(provisional_paths()),
        },
        "queue_without_card": [asdict(row) for row in queue_without_card[:80]],
        "queue_without_brief": [asdict(row) for row in queue_without_brief[:80]],
        "queue_without_pdf": [asdict(row) for row in queue_without_pdf[:80]],
        "cards_without_brief": [rel(card.path) for card in cards_without_brief],
        "cards_without_pdf_anchor": [rel(card.path) for card in cards_without_pdf_anchor],
    }


def write_audit(data: dict[str, Any]) -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    (GENERATED / "hygiene-audit.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Hygiene Audit", "", f"> Generated: {data['generated_at']}", "", "## Summary", ""]
    lines.extend(f"- {key}: {value}" for key, value in data["summary"].items())
    lines.extend(["", "## Queue Without Card", ""])
    if data["queue_without_card"]:
        for row in data["queue_without_card"][:20]:
            lines.append(f"- {row.get('arxiv_id') or 'no-id'} — {row.get('title')}")
    else:
        lines.append("None.")
    lines.extend(["", "## Card Hygiene", ""])
    for key in ["cards_without_brief", "cards_without_pdf_anchor"]:
        lines.append(f"### {key}")
        items = data[key]
        lines.extend([f"- {item}" for item in items[:40]] or ["None."])
    (GENERATED / "hygiene-audit.md").write_text("\n".join(lines) + "\n")


def pack_rows(limit: int, query: str = "") -> list[QueueRow]:
    rows = queue_rows()
    if query:
        rows = [row for row in rows if matches_query(query, row.title, row.arxiv_id, row.raw)]
    else:
        rows = [row for row in rows if "card written" not in row.status.lower()]
    rows.sort(
        key=lambda row: (
            0 if brief_matches(row.title, row.arxiv_id, slugify(row.title)) else 1,
            row.year,
            row.title,
        )
    )
    return rows[:limit]


def format_pack(rows: list[QueueRow]) -> str:
    lines = ["# Pack", "", "Read once:"]
    lines.append(f"- {rel(L1_CARD_TEMPLATE)}" if L1_CARD_TEMPLATE.exists() else "- card template: missing")
    lines.append("")
    if not rows:
        lines.append("No matching queue rows. Use `lookup <query>` or add rows to `comparison/queue.md`.")
        return "\n".join(lines) + "\n"
    for idx, row in enumerate(rows, 1):
        slug = slugify(row.title)
        paper = brief_matches(row.title, row.arxiv_id, slug)
        survey = survey_brief_matches(row.title, row.arxiv_id, slug)
        pdf = pdf_matches(row.title, row.arxiv_id, slug)
        lines.extend(
            [
                f"## {idx}. {slug}",
                "",
                f"- Title: {row.title}",
                f"- arXiv: {row.arxiv_id or 'none'}",
                f"- Queue: {row.raw}",
                f"- Paper brief: {rel(paper[0]) if paper else 'missing'}",
                f"- Survey brief: {rel(survey[0]) if survey else 'missing'}",
                f"- PDF: {rel(pdf[0]) if pdf else 'missing'}",
            ]
        )
        if paper or pdf:
            lines.append("- Suggested next action: Codex read bounded inputs and decide whether to write/update card.")
        else:
            lines.append("- Suggested next action: find/download source or build brief before writing a formal card.")
        lines.append("")
    return "\n".join(lines)
