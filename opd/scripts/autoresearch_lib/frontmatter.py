from __future__ import annotations

import re
from typing import Any


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_scalar(value: str) -> Any:
    value = value.split("#", 1)[0].strip()
    if value == "":
        return ""
    value = strip_quotes(value)
    if value in {"true", "false"}:
        return value == "true"
    if value in {"null", "None"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [strip_quotes(part.strip()) for part in inner.split(",")]
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    return parse_frontmatter(parts[1]), parts[2]


def parse_frontmatter(raw: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        top = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        nested = re.match(r"^\s+([A-Za-z_][\w-]*):\s*(.*)$", line)
        item = re.match(r"^\s*-\s+(.*)$", line)
        if top:
            key, value = top.group(1), top.group(2)
            current = key
            if value.strip() == "":
                if key in {"decisions", "surveys"}:
                    data[key] = {}
                else:
                    data[key] = []
            else:
                data[key] = parse_scalar(value)
            continue
        if nested and current:
            key, value = nested.group(1), nested.group(2)
            if not isinstance(data.get(current), dict):
                data[current] = {}
            data[current][key] = parse_scalar(value)
            continue
        if item and current:
            if not isinstance(data.get(current), list):
                data[current] = []
            data[current].append(parse_scalar(item.group(1)))
    return data
