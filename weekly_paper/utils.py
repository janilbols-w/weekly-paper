from __future__ import annotations

import hashlib
import html
import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Union
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


SPACE_RE = re.compile(r"\s+")
TAG_RE = re.compile(r"<[^>]+>")
TRACKING_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}


def clean_text(value: Any, limit: int = 10000) -> str:
    text = html.unescape(TAG_RE.sub(" ", str(value or "")))
    return SPACE_RE.sub(" ", text).strip()[:limit]


def canonical_url(value: str) -> str:
    parts = urlsplit((value or "").strip())
    query = [
        (key, val)
        for key, val in parse_qsl(parts.query, keep_blank_values=True)
        if not key.lower().startswith("utm_") and key.lower() not in TRACKING_KEYS
    ]
    return urlunsplit(
        (parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), urlencode(query), "")
    )


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]", "", value.lower())


def iso_date(value: Any) -> str:
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, datetime):
        return value.date().isoformat()
    text = str(value or "")
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return "1970-01-01"


def week_id(value: Union[str, date, datetime]) -> str:
    day = date.fromisoformat(iso_date(value))
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


def edition_week_id(value: Union[str, date, datetime]) -> str:
    """Assign a paper to the Friday edition that first follows its publish date."""
    day = date.fromisoformat(iso_date(value))
    friday = day + timedelta(days=(4 - day.weekday()) % 7)
    return week_id(friday)


def edition_bounds(edition: str) -> tuple[str, str]:
    match = re.fullmatch(r"(\d{4})-W(\d{2})", edition)
    if not match:
        raise ValueError(f"invalid edition id: {edition}")
    friday = date.fromisocalendar(int(match.group(1)), int(match.group(2)), 5)
    return (friday - timedelta(days=6)).isoformat(), friday.isoformat()


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def stable_digest(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))
