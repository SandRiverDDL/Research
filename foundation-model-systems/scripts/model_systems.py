#!/usr/bin/env python3
"""Lightweight maintenance for foundation-model-system source dossiers."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
LENSES = ROOT / "lenses"
COMPARISON = ROOT / "comparison"
GENERATED = ROOT / "_meta" / "generated"


FRONTMATTER_RE = re.compile(r"```yaml\s*\n---\n(.*?)\n---\n```", re.DOTALL)
TR_PREFIX_CITATION_RE = re.compile(r"\[TR\s+p", re.IGNORECASE)
LEADING_CITATION_RE = re.compile(r"(?m)^-\s+\[[^\]]+\](?::|\s)")
GENERIC_BLOG_CITATION_RE = re.compile(r"\[blog\]", re.IGNORECASE)


@dataclass
class SourceRecord:
    source_id: str
    path: Path
    lane: str
    source_type: str = ""
    org: str = ""
    release_date: str = ""
    priority: str = ""
    status: str = ""
    openness: str = ""
    confidence: str = ""


@dataclass
class ValidationResult:
    issues: list[str]
    warnings: list[str]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def parse_simple_yaml(text: str) -> dict[str, object]:
    """Parse the restricted YAML shape used in dossier metadata."""
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}
    data: dict[str, object] = {}
    current_key: str | None = None
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key:
            value = line[4:].strip()
            current = data.setdefault(current_key, [])
            if isinstance(current, list):
                current.append(value)
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                data[key] = value
                current_key = None
            else:
                data[key] = []
                current_key = key
    return data


def source_records() -> list[SourceRecord]:
    records: list[SourceRecord] = []
    for readme in sorted(SOURCES.glob("*/README.md")):
        meta = parse_simple_yaml(readme.read_text(encoding="utf-8"))
        source_id = str(meta.get("source_id") or readme.parent.name)
        source_type = str(meta.get("source_type") or "")
        records.append(
            SourceRecord(
                source_id=source_id,
                path=readme.parent,
                lane="source",
                source_type=source_type,
                org=str(meta.get("org") or ""),
                release_date=str(meta.get("release_date") or ""),
                priority=str(meta.get("priority") or ""),
                status=str(meta.get("status") or ""),
                openness=str(meta.get("openness") or ""),
                confidence=str(meta.get("confidence") or ""),
            )
        )
    return records


def validate_sources(records: list[SourceRecord]) -> list[str]:
    issues: list[str] = []
    valid_priorities = {"S", "A", "B", "C"}
    valid_status = {"stub", "intake", "section-notes", "lens-ready", "compared"}
    valid_openness = {"open-weights", "fully-open", "api-only", "unclear"}
    for record in records:
        readme = record.path / "README.md"
        bundle = record.path / "source-bundle.md"
        index = record.path / "section-index.md"
        if not bundle.exists():
            issues.append(f"{rel(record.path)}: missing source-bundle.md")
        if record.source_type in {"model-tr", "open-project", "blog-bundle"} and not index.exists():
            issues.append(f"{rel(record.path)}: missing section-index.md")
        if not record.priority:
            issues.append(f"{rel(readme)}: missing priority")
        elif record.priority not in valid_priorities:
            issues.append(f"{rel(readme)}: unknown priority {record.priority!r}")
        if not record.status:
            issues.append(f"{rel(readme)}: missing status")
        elif record.status not in valid_status:
            issues.append(f"{rel(readme)}: unknown status {record.status!r}")
        if record.openness and record.openness not in valid_openness:
            issues.append(f"{rel(readme)}: unknown openness {record.openness!r}")
        text = readme.read_text(encoding="utf-8")
        required_sections = [
            ("one-line takeaway", ["## One-line Takeaway", "## 一句话"]),
            ("source bundle", ["## Source Bundle"]),
            ("lens hooks", ["## Lens Hooks"]),
            ("need to read", ["## Need To Read", "## 阅读入口"]),
        ]
        for label, headings in required_sections:
            if not any(heading in text for heading in headings):
                issues.append(f"{rel(readme)}: missing section {label}")
    return issues


def validate_lenses(records: list[SourceRecord]) -> list[str]:
    issues: list[str] = []
    source_ids = {record.source_id for record in records}
    for note in sorted(LENSES.glob("*/*.md")):
        text = note.read_text(encoding="utf-8")
        meta = parse_simple_yaml(text)
        listed = meta.get("sources", [])
        if not listed:
            issues.append(f"{rel(note)}: missing sources metadata")
        elif isinstance(listed, list):
            for source_id in listed:
                if source_id not in source_ids:
                    issues.append(f"{rel(note)}: unknown source {source_id!r}")
        if "source:" not in text:
            issues.append(f"{rel(note)}: no source links found")
        if "anchor:" not in text:
            issues.append(f"{rel(note)}: no anchor placeholders found")
    return issues


def validate_comparisons(records: list[SourceRecord]) -> list[str]:
    issues: list[str] = []
    source_ids = {record.source_id for record in records}
    for note in sorted(COMPARISON.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        meta = parse_simple_yaml(text)
        listed = meta.get("sources", [])
        if not listed:
            issues.append(f"{rel(note)}: missing sources metadata")
        elif isinstance(listed, list):
            for source_id in listed:
                if source_id not in source_ids:
                    issues.append(f"{rel(note)}: unknown source {source_id!r}")
        for required in ["## Executive Takeaway", "## Source Matrix", "## Evidence Used", "## Limits"]:
            if required not in text:
                issues.append(f"{rel(note)}: missing section {required}")
    return issues


def validate_citation_style() -> list[str]:
    issues: list[str] = []
    search_roots = [SOURCES, LENSES, COMPARISON, ROOT / "doc"]
    for root in search_roots:
        if not root.exists():
            continue
        for note in sorted(root.rglob("*.md")):
            text = note.read_text(encoding="utf-8")
            if TR_PREFIX_CITATION_RE.search(text):
                issues.append(f"{rel(note)}: use page-only TR anchors like [29-30], not [TR p29-p30]")
            if LEADING_CITATION_RE.search(text):
                issues.append(f"{rel(note)}: move citation anchors to the end of the claim, not the bullet start")
            if GENERIC_BLOG_CITATION_RE.search(text):
                issues.append(f"{rel(note)}: use a semantic blog label like [blog-build-2026], not [blog]")
    return issues


def validate_stage_notes(records: list[SourceRecord]) -> list[str]:
    warnings: list[str] = []
    for record in records:
        notes_dir = record.path / "notes"
        if not notes_dir.exists():
            continue
        for note in sorted(notes_dir.rglob("*.md")):
            line_count = len(note.read_text(encoding="utf-8").splitlines())
            if line_count > 220:
                warnings.append(f"{rel(note)}: {line_count} lines; consider splitting by substage if it contains independent flows")
    return warnings


def write_manifest(records: list[SourceRecord]) -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    manifest = GENERATED / "source-manifest.jsonl"
    with manifest.open("w", encoding="utf-8") as handle:
        for record in records:
            row = {
                "source_id": record.source_id,
                "lane": record.lane,
                "source_type": record.source_type,
                "org": record.org,
                "release_date": record.release_date,
                "priority": record.priority,
                "status": record.status,
                "openness": record.openness,
                "confidence": record.confidence,
                "path": rel(record.path),
            }
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_validation(issues: list[str], warnings: list[str]) -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    (GENERATED / "validation.json").write_text(
        json.dumps(
            {
                "issue_count": len(issues),
                "warning_count": len(warnings),
                "issues": issues,
                "warnings": warnings,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    lines = ["# Validation", ""]
    if not issues:
        lines.append("No validation issues.")
    else:
        lines.append(f"Issues: {len(issues)}")
        lines.append("")
        for issue in issues:
            lines.append(f"- {issue}")
    if warnings:
        lines.append("")
        lines.append(f"Warnings: {len(warnings)}")
        lines.append("")
        for warning in warnings:
            lines.append(f"- {warning}")
    (GENERATED / "validation.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_status(records: list[SourceRecord], issues: list[str], warnings: list[str]) -> None:
    GENERATED.mkdir(parents=True, exist_ok=True)
    lines = ["# Foundation Model Systems Status", ""]
    lines.append(f"Sources: {len(records)}")
    lines.append(f"Validation issues: {len(issues)}")
    lines.append(f"Validation warnings: {len(warnings)}")
    lines.append("")
    lines.append("## Sources")
    lines.append("")
    lines.append("| Source | Type | Priority | Status | Openness | Confidence |")
    lines.append("|---|---|---:|---|---|---|")
    for record in records:
        lines.append(
            f"| `{record.source_id}` | {record.source_type} | {record.priority} | {record.status} | {record.openness} | {record.confidence} |"
        )
    lines.append("")
    lines.append("## Recommended Next Step")
    lines.append("")
    if issues:
        lines.append("Fix validation issues before synthesis.")
    elif records and all(record.status in {"lens-ready", "compared"} for record in records):
        lines.append("Write or update comparison files, then decide the next source to add.")
    elif records and all(record.status in {"section-notes", "lens-ready", "compared"} for record in records):
        lines.append("Use the stage notes to write or revise the pilot comparison. Defer new lenses until a concrete cross-source question or at least 3 sources exist.")
    elif records and all(record.status in {"intake", "section-notes", "lens-ready", "compared"} for record in records):
        lines.append("Start section notes for the pilot sources, preserving source anchors.")
    else:
        lines.append("Fill source-bundle local PDF paths, then start section notes for the two pilot sources.")
    (GENERATED / "status.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def sync(_: argparse.Namespace) -> None:
    records = source_records()
    issues = (
        validate_sources(records)
        + validate_lenses(records)
        + validate_comparisons(records)
        + validate_citation_style()
    )
    warnings = validate_stage_notes(records)
    write_manifest(records)
    write_validation(issues, warnings)
    write_status(records, issues, warnings)
    print(f"wrote {rel(GENERATED / 'source-manifest.jsonl')}")
    print(f"wrote {rel(GENERATED / 'validation.md')}")
    print(f"wrote {rel(GENERATED / 'status.md')}")
    print(f"sources={len(records)} issues={len(issues)} warnings={len(warnings)}")


def validate(args: argparse.Namespace) -> None:
    sync(args)
    issues = json.loads((GENERATED / "validation.json").read_text(encoding="utf-8"))["issues"]
    if issues:
        print("\n".join(issues))
        raise SystemExit(1)


def status(args: argparse.Namespace) -> None:
    sync(args)
    print()
    print((GENERATED / "status.md").read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Maintain foundation model systems research artifacts.")
    sub = parser.add_subparsers(dest="command")

    sync_parser = sub.add_parser("sync", help="Regenerate manifest, validation, and status.")
    sync_parser.set_defaults(func=sync)

    validate_parser = sub.add_parser("validate", help="Regenerate artifacts and exit nonzero on issues.")
    validate_parser.set_defaults(func=validate)

    status_parser = sub.add_parser("status", help="Regenerate artifacts and print status.")
    status_parser.set_defaults(func=status)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        args = parser.parse_args(["status"])
    args.func(args)


if __name__ == "__main__":
    main()
