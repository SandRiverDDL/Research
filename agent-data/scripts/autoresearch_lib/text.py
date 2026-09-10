from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

from .config import ROOT


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def compact_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()
    return re.sub(r"\s+", "-", value).strip("-")[:80] or "unknown"
