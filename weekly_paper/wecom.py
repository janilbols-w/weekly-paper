from __future__ import annotations

import os
import time
from typing import Any, Dict, List

import requests


def split_markdown(markdown: str, limit: int = 3900) -> List[str]:
    chunks: List[str] = []
    current = ""
    for line in markdown.splitlines():
        candidate = f"{current}\n{line}" if current else line
        if len(candidate.encode("utf-8")) <= limit:
            current = candidate
            continue
        if current:
            chunks.append(current)
        current = ""
        piece = ""
        for char in line:
            if len((piece + char).encode("utf-8")) > limit:
                chunks.append(piece)
                piece = char
            else:
                piece += char
        current = piece
    if current:
        chunks.append(current)
    return chunks


def send_wecom(markdown: str, config: Dict[str, Any], retries: int = 3) -> None:
    webhook = os.getenv("WECOM_WEBHOOK_URL", "").strip()
    if not webhook.startswith("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?"):
        raise ValueError("WECOM_WEBHOOK_URL is missing or is not a recognized WeCom robot webhook")
    for index, chunk in enumerate(split_markdown(markdown), start=1):
        content = chunk if index == 1 else f"**周报续 {index}**\n{chunk}"
        last_error: Exception = RuntimeError("unknown WeCom error")
        for attempt in range(retries):
            try:
                response = requests.post(
                    webhook,
                    json={"msgtype": "markdown", "markdown": {"content": content}},
                    timeout=int(config["request_timeout_seconds"]),
                )
                response.raise_for_status()
                result = response.json()
                if result.get("errcode") != 0:
                    raise RuntimeError(f"WeCom rejected message: {result.get('errmsg', 'unknown error')}")
                break
            except Exception as exc:
                last_error = exc
                if attempt + 1 == retries:
                    raise last_error
                time.sleep(2**attempt)

