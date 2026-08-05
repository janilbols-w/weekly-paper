from __future__ import annotations

from io import BytesIO
from typing import Any, Dict, List, Tuple

import requests
from pypdf import PdfReader

from .models import Paper


TARGET_TERMS = ("experiment", "evaluation", "results", "limitation", "benchmark", "ablation")


def extract_targeted_context(
    paper: Paper, global_config: Dict[str, Any], max_chars: int = 24000
) -> Tuple[str, str]:
    if not paper.pdf_url:
        return "", "metadata"
    response = requests.get(
        paper.pdf_url,
        headers={"User-Agent": global_config["user_agent"]},
        timeout=int(global_config["request_timeout_seconds"]),
    )
    response.raise_for_status()
    if len(response.content) > 25 * 1024 * 1024:
        raise ValueError("PDF exceeds 25 MiB safety limit")
    reader = PdfReader(BytesIO(response.content))
    pages: List[Tuple[int, str]] = []
    for index, page in enumerate(reader.pages):
        text = (page.extract_text() or "").strip()
        if text:
            pages.append((index, text))
    selected_indexes = set(range(min(3, len(pages))))
    selected_indexes.update(range(max(0, len(pages) - 2), len(pages)))
    for position, (_, text) in enumerate(pages):
        lower = text.lower()
        if any(term in lower for term in TARGET_TERMS):
            selected_indexes.add(position)
    chunks: List[str] = []
    for position in sorted(selected_indexes):
        page_number, text = pages[position]
        chunks.append(f"\n--- PDF page {page_number + 1} ---\n{text}")
        if sum(len(chunk) for chunk in chunks) >= max_chars:
            break
    return "".join(chunks)[:max_chars], "targeted-pdf"

