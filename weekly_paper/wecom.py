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


def send_wecom(
    markdown: str,
    config: Dict[str, Any],
    retries: int = 3,
    continuation_label: str = "周报续",
) -> None:
    webhook = os.getenv("WECOM_WEBHOOK_URL", "").strip()
    if not webhook.startswith("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?"):
        raise ValueError("WECOM_WEBHOOK_URL is missing or is not a recognized WeCom robot webhook")
    if retries < 1:
        raise ValueError("retries must be at least 1")
    for index, chunk in enumerate(split_markdown(markdown), start=1):
        content = chunk if index == 1 else f"**{continuation_label} {index}**\n{chunk}"
        last_error: Exception = RuntimeError("unknown WeCom error")
        for attempt in range(retries):
            try:
                response = requests.post(
                    webhook,
                    json={"msgtype": "markdown", "markdown": {"content": content}},
                    timeout=int(config["request_timeout_seconds"]),
                )
                if not response.ok:
                    raise RuntimeError(f"WeCom returned HTTP {response.status_code}")
                try:
                    result = response.json()
                except ValueError as exc:
                    raise RuntimeError("WeCom returned an invalid JSON response") from exc
                if result.get("errcode") != 0:
                    raise RuntimeError(
                        f"WeCom rejected message ({result.get('errcode')}): "
                        f"{result.get('errmsg', 'unknown error')}"
                    )
                break
            except requests.RequestException as exc:
                # requests exceptions may contain the full webhook URL, including
                # its secret key. Keep the diagnostic useful without leaking it.
                last_error = RuntimeError(f"WeCom request failed: {type(exc).__name__}")
                if attempt + 1 == retries:
                    raise last_error from exc
                time.sleep(2**attempt)
            except RuntimeError as exc:
                last_error = exc
                if attempt + 1 == retries:
                    raise last_error
                time.sleep(2**attempt)
