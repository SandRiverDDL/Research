#!/usr/bin/env python3
"""Minimal autoresearch helper.

Codex makes research judgments. This script only handles hygiene, lookup,
audit, and bounded-input packs.
"""

from __future__ import annotations

import argparse

from autoresearch_lib.hygiene import audit_cmd, lookup_cmd, pack_cmd, print_status, sync_alias, validate_cmd


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Autoresearch helper. Codex makes research judgments; this script handles hygiene, lookup, audit, and bounded input packs."
    )
    sub = parser.add_subparsers(dest="command")

    status_parser = sub.add_parser("status", help="Print counts and next mechanical action.")
    status_parser.set_defaults(func=print_status)

    validate_parser = sub.add_parser("validate", help="Run lightweight hygiene validation.")
    validate_parser.set_defaults(func=validate_cmd)

    lookup_parser = sub.add_parser("lookup", help="Check whether a paper is already in queue/card/brief/PDF sources.")
    lookup_parser.add_argument("query", help="Title fragment, slug, or arXiv ID.")
    lookup_parser.set_defaults(func=lookup_cmd)

    audit_parser = sub.add_parser("audit", help="List mechanical gaps.")
    audit_parser.set_defaults(func=audit_cmd)

    pack_parser = sub.add_parser("pack", help="Show bounded input files for queued papers. Does not write cards.")
    pack_parser.add_argument("query", nargs="?", default="", help="Optional title fragment, slug, or arXiv ID.")
    pack_parser.add_argument("--limit", type=int, default=3, help="Maximum papers to include.")
    pack_parser.set_defaults(func=pack_cmd)

    sync_parser = sub.add_parser("sync", help="Compatibility alias for status + validate.")
    sync_parser.set_defaults(func=sync_alias)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        args = parser.parse_args(["status"])
    args.func(args)


if __name__ == "__main__":
    main()
