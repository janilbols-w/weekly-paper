from __future__ import annotations

from typing import Any, Dict, List

from .event_models import EventPaper
from .models import Paper


def _summary(paper: Paper) -> str:
    return paper.summary_zh or paper.summary_en or paper.abstract[:300]


def render_weekly_report(
    week: str,
    papers: List[Paper],
    featured: List[Paper],
    metadata: Dict[str, Any],
) -> str:
    lines = [
        f"# LLM 高效推理与 AI Infra 论文周报 · {week}",
        "",
        f"> 覆盖：{metadata['start_date']} 至 {metadata['end_date']} · 收录 {len(papers)} 篇 · 精选 {len(featured)} 篇",
        "",
        "## 本周精选",
        "",
    ]
    if not featured:
        lines.append("本周没有论文达到精选质量线。")
    for index, paper in enumerate(featured, start=1):
        category = paper.primary_category.get("leaf_zh", paper.primary_category.get("leaf", "未分类"))
        lines.extend(
            [
                f"### {index}. [{paper.title}]({paper.url})",
                "",
                f"- **分类**：{category}",
                f"- **评分**：{paper.score}/100",
                f"- **摘要**：{_summary(paper)}",
                f"- **为什么值得关注**：{paper.why_it_matters_zh or '待编辑增强'}",
                f"- **主要限制**：{paper.limitations_zh or '需结合论文实验设置进一步核验'}",
                f"- **代码**：{paper.code_url or '未发现公开代码链接'}",
                "",
            ]
        )
    lines.extend(["## 其他收录论文", ""])
    featured_ids = {paper.id for paper in featured}
    remaining = [paper for paper in papers if paper.id not in featured_ids]
    if not remaining:
        lines.append("- 暂无")
    for paper in remaining:
        category = paper.primary_category.get("leaf_zh", paper.primary_category.get("leaf", "未分类"))
        lines.append(f"- [{paper.title}]({paper.url}) · {category} · {paper.score}/100")
    lines.extend(
        [
            "",
            "---",
            "",
            "评分与摘要由自动化流程生成，关键性能结论请以论文原文、硬件配置和实验负载为准。",
        ]
    )
    return "\n".join(lines) + "\n"


def render_wecom(week: str, featured: List[Paper], site_url: str) -> str:
    lines = [
        f"## LLM Efficient Inference & AI Infra · {week}",
        "",
        f"> 本周精选 {len(featured)} 篇论文",
        "",
    ]
    for index, paper in enumerate(featured, start=1):
        category = paper.primary_category.get("leaf_zh", "未分类")
        why = paper.why_it_matters_zh or paper.summary_zh
        lines.extend(
            [
                f"**{index}. [{paper.title}]({paper.url})**",
                f"> <font color=\"comment\">{category} · {paper.score}/100</font>",
                f"> {why}",
                "",
            ]
        )
    lines.append(f"[查看完整周报与知识地图]({site_url.rstrip('/')}/weekly/{week.lower()}/)")
    return "\n".join(lines)


def _event_snippet(value: str, limit: int = 180) -> str:
    value = " ".join(str(value or "").split())
    return value if len(value) <= limit else value[: limit - 1].rstrip() + "…"


def render_event_wecom(event: Dict[str, Any], papers: List[EventPaper], site_url: str) -> str:
    short_name = str(event.get("short_name") or event.get("name") or event["id"])
    lines = [
        f"## 会议专题 · {short_name}",
        "",
        f"> {event.get('start_date', '')} — {event.get('end_date', '')} · {event.get('location', '')}",
        f"> <font color=\"comment\">{event.get('status', '待跟踪')} · {event.get('trigger_type', 'update')}</font>",
        "",
    ]
    if event.get("summary_zh"):
        lines.extend([_event_snippet(str(event["summary_zh"]), 260), ""])
    if event.get("relevance_zh"):
        lines.extend(["**为什么值得关注**", f"> {_event_snippet(str(event['relevance_zh']), 300)}", ""])

    if event.get("collector") == "official_program":
        programs = event.get("key_programs", [])[:4]
        if programs:
            lines.extend([f"**重点议程 · {len(event.get('key_programs', []))} 项中精选**", ""])
        for item in programs:
            meta = " · ".join(part for part in (item.get("date", ""), item.get("location", "")) if part)
            lines.append(f"- [{item['title']}]({item.get('url', event.get('program_url', event['official_url']))})")
            if meta:
                lines.append(f"  > <font color=\"comment\">{meta}</font>")
            if item.get("focus_zh"):
                lines.append(f"  > {_event_snippet(str(item['focus_zh']))}")
    else:
        selected = sorted(
            [item for item in papers if item.selected],
            key=lambda item: item.paper.score,
            reverse=True,
        )
        if selected:
            lines.extend([f"**精选论文 · {len(selected)} 篇**", ""])
        for item in selected[:4]:
            paper = item.paper
            category = paper.primary_category.get("leaf_zh", "未分类")
            lines.extend(
                [
                    f"- [{paper.title}]({paper.url})",
                    f"  > <font color=\"comment\">{category} · {paper.score}/100</font>",
                    f"  > {_event_snippet(paper.why_it_matters_zh or item.selection_reason_zh or paper.summary_zh)}",
                ]
            )

    lines.extend(
        [
            "",
            f"[查看完整会议专题]({site_url.rstrip('/')}/events/{event['id']}/)",
        ]
    )
    return "\n".join(lines)
