from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Iterable, List

from .models import Paper
from .utils import now_utc_iso, read_json, write_json


SAFE_RE = re.compile(r"[^a-zA-Z0-9._-]+")


def safe_id(value: str) -> str:
    return SAFE_RE.sub("-", value).strip("-").lower()


def load_papers(root: Path) -> Dict[str, Paper]:
    output: Dict[str, Paper] = {}
    for path in sorted((root / "data" / "papers").glob("*.json")):
        paper = Paper.from_dict(read_json(path, {}))
        if paper.id:
            output[paper.id] = paper
    return output


def save_papers(root: Path, papers: Iterable[Paper]) -> None:
    values = list(papers)
    directory = root / "data" / "papers"
    directory.mkdir(parents=True, exist_ok=True)
    expected = {f"{safe_id(paper.id)}.json" for paper in values}
    for path in directory.glob("*.json"):
        if path.name not in expected:
            path.unlink()
    for paper in values:
        write_json(root / "data" / "papers" / f"{safe_id(paper.id)}.json", paper.to_dict())


def load_weeks(root: Path) -> List[dict]:
    return [read_json(path, {}) for path in sorted((root / "data" / "weeks").glob("*.json"))]


def save_week(root: Path, value: dict) -> None:
    value.setdefault("generated_at", now_utc_iso())
    write_json(root / "data" / "weeks" / f"{value['week']}.json", value)
