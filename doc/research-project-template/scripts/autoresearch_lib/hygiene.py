from __future__ import annotations

import argparse
import json

from .config import GENERATED
from .pack import audit_data, format_pack, lookup_data, pack_rows, status_payload, write_audit
from .text import rel
from .validate import validate_project, write_validation


def print_status(args: argparse.Namespace) -> None:
    payload = status_payload()
    GENERATED.mkdir(parents=True, exist_ok=True)
    (GENERATED / "status.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print("# autoresearch status")
    print("")
    for key in [
        "formal_cards",
        "queue_rows",
        "paper_briefs",
        "survey_briefs",
        "pdfs",
        "off_scope",
        "validation_errors",
        "validation_warnings",
    ]:
        print(f"{key}: {payload[key]}")
    if payload["validation_errors"]:
        print("next_action: run validate and fix hygiene errors")
    elif payload["queue_rows"]:
        print("next_action: run pack --limit 3, then let Codex decide what to read/write")
    else:
        print("next_action: write synthesis or run a narrow recall audit")


def validate_cmd(args: argparse.Namespace) -> None:
    result = validate_project()
    write_validation(result)
    print(f"errors: {len(result.errors)}")
    print(f"warnings: {len(result.warnings)}")
    print(f"wrote: {rel(GENERATED / 'card-validation.md')}")
    if result.errors:
        raise SystemExit(1)


def lookup_cmd(args: argparse.Namespace) -> None:
    print(json.dumps(lookup_data(args.query), ensure_ascii=False, indent=2))


def audit_cmd(args: argparse.Namespace) -> None:
    data = audit_data()
    write_audit(data)
    print(json.dumps(data["summary"], ensure_ascii=False, indent=2))
    print(f"wrote: {rel(GENERATED / 'hygiene-audit.md')}")


def pack_cmd(args: argparse.Namespace) -> None:
    limit = int(getattr(args, "limit", 3) or 3)
    query = str(getattr(args, "query", "") or "")
    print(format_pack(pack_rows(limit, query)))


def sync_alias(args: argparse.Namespace) -> None:
    print_status(args)
    result = validate_project()
    write_validation(result)
    print(f"validation: {'failed' if result.errors else 'ok'}")
    if result.errors:
        raise SystemExit(1)
