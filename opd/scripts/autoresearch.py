#!/usr/bin/env python3
"""Minimal OPD paper-card registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from autoresearch_lib.registry import lookup, public_record, scan_cards, validate_cards


ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / "notes"


def status_cmd(_args: argparse.Namespace) -> None:
    result = validate_cards(NOTES)
    print(f"cards: {len(result.cards)}")
    print(f"errors: {len(result.errors)}")
    print(f"warnings: {len(result.warnings)}")


def validate_cmd(_args: argparse.Namespace) -> None:
    result = validate_cards(NOTES)
    for item in result.errors:
        print(f"ERROR: {item}")
    for item in result.warnings:
        print(f"WARN: {item}")
    print(f"cards: {len(result.cards)}")
    print(f"errors: {len(result.errors)}")
    print(f"warnings: {len(result.warnings)}")
    if result.errors:
        raise SystemExit(1)


def lookup_cmd(args: argparse.Namespace) -> None:
    cards = scan_cards(NOTES)
    records = [public_record(card, ROOT) for card in lookup(cards, args.query)]
    print(json.dumps({"query": args.query, "matches": records}, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read-only OPD card registry. Research judgments stay in Markdown and synthesis."
    )
    sub = parser.add_subparsers(dest="command")

    status_parser = sub.add_parser("status", help="Count formal cards and validation issues.")
    status_parser.set_defaults(func=status_cmd)

    validate_parser = sub.add_parser("validate", help="Check identity, source URLs, and duplicates.")
    validate_parser.set_defaults(func=validate_cmd)

    lookup_parser = sub.add_parser("lookup", help="Find an existing card by paper ID, URL, title, author, or slug.")
    lookup_parser.add_argument("query")
    lookup_parser.set_defaults(func=lookup_cmd)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        args = parser.parse_args(["status"])
    args.func(args)


if __name__ == "__main__":
    main()
