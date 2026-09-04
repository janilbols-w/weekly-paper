from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List

from .event_models import EventPaper
from .utils import read_json, write_json


def _frontmatter(title: str, description: str = "") -> str:
    lines = ["---", f"title: {json.dumps(title, ensure_ascii=False)}"]
    if description:
        lines.append(f"description: {json.dumps(description, ensure_ascii=False)}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def _category(item: EventPaper) -> str:
    path = item.paper.primary_category
    return " > ".join(filter(None, [path.get("domain_zh"), path.get("group_zh"), path.get("leaf_zh")]))


EVENT_STATUS = {
    "待跟踪": ("tracking", "🔵"),
    "即将举行": ("upcoming", "🟡"),
    "进行中": ("active", "🟢"),
    "已归档": ("archived", "⚪"),
}


def _status_badge(status: str) -> str:
    style, emoji = EVENT_STATUS.get(status, ("unknown", "⚪"))
    return (
        f'<span class="event-status event-status--{style}">'
        f'<span aria-hidden="true">{emoji}</span> {html.escape(status)}</span>'
    )


def _event_markdown(event: Dict[str, Any], papers: List[EventPaper]) -> str:
    program_briefing = event.get("collector") == "official_program"
    briefing_title_suffix = event.get("briefing_title_suffix_zh", "Workshop 议程观察")
    page_title = (
        f"{event['short_name']} · {briefing_title_suffix}"
        if program_briefing
        else f"{event['short_name']} · 高效推理与 AI Infra 精选"
    )
    program_link_label = event.get("program_link_label_zh", "官方 Workshop 公告")
    source_links = (
        f"[会议官网]({event['official_url']}) · [{program_link_label}]({event.get('program_url', event['official_url'])})"
        if program_briefing
        else f"[会议官网]({event['official_url']}) · [会议议程]({event.get('program_url', event['official_url'])}) · [官方录用列表]({event.get('accepted_papers_url', event['official_url'])})"
    )
    selected = sorted(
        [item for item in papers if item.selected],
        key=lambda item: item.paper.score,
        reverse=True,
    )
    counts = Counter(item.paper.primary_category.get("leaf_zh", "未分类") for item in papers)
    stats = event.get("official_totals", {})
    status_detail = (
        f"重点议程 {len(event.get('key_programs', []))} 项"
        if program_briefing
        else f"相关论文 {len(papers)} 篇 · 精选 {len(selected)} 篇"
    )
    lines = [
        _frontmatter(page_title, event.get("summary_zh", "")),
        f"> **{event['start_date']} — {event['end_date']} · {event['location']}**",
        f"> 状态：{_status_badge(event.get('status', '已归档'))} · {status_detail} · 更新于 {event.get('generated_at', '')[:10]}",
        "",
        source_links,
        "",
        "## 一分钟结论",
        "",
        event.get("summary_zh", ""),
        "",
        event.get("relevance_zh", ""),
        "",
    ]
    if program_briefing and event.get("current_stage_zh"):
        lines.extend(["## 当前阶段", "", event["current_stage_zh"], ""])
    event_stats = event.get("event_stats", [])
    if program_briefing and event_stats:
        lines.extend(["## 官方规模", "", "| 指标 | 官方数据 |", "|---|---:|"])
        for item in event_stats:
            lines.append(f"| {item['label']} | {item['value']} |")
        lines.append("")
    if stats:
        labels = {
            "submissions": "唯一投稿",
            "main_accepted": "Main 录用",
            "findings_accepted": "Findings 录用",
            "main_oral": "Main oral",
            "accepted_papers": "正式论文",
            "operational_systems_papers": "Operational Systems 论文",
            "best_paper_awards": "Best Paper",
            "distinguished_artifact_awards": "Distinguished Artifact Award",
        }
        hidden = {"main_acceptance_rate", "findings_acceptance_rate"}
        lines.extend(["## 会议规模", "", "| 指标 | 官方数据 |", "|---|---:|"])
        for key, value in stats.items():
            if key in hidden:
                continue
            if key == "main_accepted" and stats.get("main_acceptance_rate"):
                value = f"{value}（{stats['main_acceptance_rate']}）"
            if key == "findings_accepted" and stats.get("findings_acceptance_rate"):
                value = f"{value}（{stats['findings_acceptance_rate']}）"
            lines.append(f"| {labels.get(key, key.replace('_', ' ').title())} | {value} |")
        lines.append("")
    programs = event.get("key_programs", [])
    if programs:
        if program_briefing:
            lines.extend(["## 关键议程", "", "| 环节 | 日期 / 地点 | 工程观察 |", "|---|---|---|"])
            for item in programs:
                when = item.get("date", "待公布")
                if item.get("location"):
                    when += f"<br>{item['location']}"
                lines.append(
                    f"| [{item['title']}]({item['url']}) | {when} | {item.get('focus_zh', '待公布')} |"
                )
        else:
            lines.extend(["## 关键议程", "", "| 环节 | 日期 |", "|---|---|"])
            for item in programs:
                lines.append(f"| [{item['title']}]({item['url']}) | {item['date']} |")
        lines.append("")
    if not program_briefing:
        lines.extend(["## 精选论文", ""])
        for index, item in enumerate(selected, 1):
            paper = item.paper
            label = _category(item)
            award = f" · {' / '.join(item.awards)}" if item.awards else ""
            lines.extend(
                [
                    f"### {index}. [{paper.title}]({paper.url})",
                    "",
                    f"**{paper.score}/100 · {label} · {item.track}{award}**",
                    "",
                    paper.summary_zh or paper.summary_en,
                    "",
                    f"**为什么值得关注：** {paper.why_it_matters_zh or item.selection_reason_zh}",
                    "",
                    f"**边界：** {paper.limitations_zh or '当前为摘要级核验，部署结论仍需结合硬件、模型和工作负载复核。'}",
                    "",
                    f"[PDF]({paper.pdf_url})" + (f" · [代码]({paper.code_url})" if paper.code_url else ""),
                    "",
                ]
            )
        lines.extend(["## 技术分布", "", "| 三级技术路径 | 论文数 |", "|---|---:|"])
        for label, count in counts.most_common():
            lines.append(f"| {label} | {count} |")
        lines.extend(["", "## 全部相关论文", "", "| 论文 | Track | 分类 | 评分 |", "|---|---|---|---:|"])
        for item in sorted(papers, key=lambda value: (value.paper.score, value.paper.title), reverse=True):
            paper = item.paper
            lines.append(f"| [{paper.title}]({paper.url}) | {item.track} | {_category(item)} | {paper.score} |")
    if program_briefing:
        lines.extend(["## 来源与核验范围", ""])
        for source in event.get("sources", []):
            note = f"；{source['note_zh']}" if source.get("note_zh") else ""
            lines.append(
                f"- [{source['label']}]({source['url']})（核验于 {source.get('checked_at', event.get('generated_at', '')[:10])}{note}）。"
            )
        lines.extend(
            [
                "",
                f"- 触发类型：`{event.get('trigger_type', 'program_released')}`；来源摘要：`{event.get('source_digest', '')[:12]}`。",
            ]
        )
        methodology_notes = event.get(
            "program_methodology_notes_zh",
            [
                "本页记录的是 workshop 正式名单与主办方已公开议程，不把 workshop CFP 当作正式论文 proceedings。",
                "尚未公布的讲题、录用论文与最终日程明确标为待更新，不据此推断性能结论或奖项。",
            ],
        )
        lines.extend(f"- {note}" for note in methodology_notes)
    else:
        lines.extend(["", "## 来源与覆盖范围", ""])
        sources = event.get("sources", [])
        if sources:
            for source in sources:
                lines.append(
                    f"- [{source['label']}]({source['url']})（核验于 {source.get('checked_at', event.get('generated_at', '')[:10])}）。"
                )
        else:
            lines.append(
                f"- 官方事实：[{event['short_name']} 官网]({event['official_url']})、"
                f"[Program]({event.get('program_url', event['official_url'])})、"
                f"[Awards]({event.get('awards_url', event['official_url'])})。"
            )
        lines.extend(
            [
                f"- 论文元数据：{event.get('corpus_source', 'official proceedings')}；原始覆盖 {event.get('corpus_total', '未记录')} 篇，主题过滤后保留 {len(papers)} 篇。",
                f"- 触发类型：`{event.get('trigger_type', 'manual_backfill')}`；来源摘要：`{event.get('source_digest', '')[:12]}`。",
                "- 精选不是奖项预测；评分只反映本站主题相关性、证据完整性和潜在工程影响。",
            ]
        )
    return "\n".join(lines) + "\n"


def _index_markdown(events: List[Dict[str, Any]]) -> str:
    lines = [
        _frontmatter("会议与活动", "LLM 高效推理与 AI Infra 会议日历及独立精选"),
        "会议/活动使用独立研究流程；论文数量由质量阈值决定，不占普通周报 Top 5 名额。",
        "",
        "| 会议 | 日期 | 领域 / 社区 | 地点 | 状态 |",
        "|---|---|---|---|---|",
    ]
    for event in sorted(events, key=lambda value: value.get("start_date", ""), reverse=True):
        local = event.get("has_report", False)
        label = f"[{event['short_name']}](./{event['id']}/)" if local else f"[{event['short_name']}]({event['official_url']})"
        lines.append(
            f"| {label} | {event.get('start_date', '')} — {event.get('end_date', '')} | "
        f"{event.get('domain', '')} / {event.get('community', '')} | {event.get('location', '')} | {_status_badge(event.get('status', '待跟踪'))} |"
        )
    lines.extend(
        [
            "",
            "## 触发规则",
            "",
            "系统在录用列表、议程、会议周或奖项发布时生成独立调研；已归档内容只有在官方来源变化时才会更新。",
        ]
    )
    return "\n".join(lines) + "\n"


def build_event_site(root: Path, configured_events: Iterable[Dict[str, Any]]) -> None:
    events = [dict(value) for value in configured_events]
    data_root = root / "data" / "events"
    by_id = {value["id"]: value for value in events}
    for event_file in data_root.glob("*/event.json"):
        value = read_json(event_file, {})
        if value.get("id"):
            by_id[value["id"]] = value
    events = list(by_id.values())
    for event in events:
        event["has_report"] = (data_root / event["id"] / "papers.json").exists()
    write_json(root / "data" / "events" / "index.json", events)
    write_json(root / "src" / "data" / "events.json", events)

    output = root / "src" / "content" / "docs" / "events"
    output.mkdir(parents=True, exist_ok=True)
    for path in output.glob("*.md"):
        path.unlink()
    (output / "index.md").write_text(_index_markdown(events), encoding="utf-8")
    for event in events:
        paper_file = data_root / event["id"] / "papers.json"
        if not paper_file.exists():
            continue
        papers = [EventPaper.from_dict(value) for value in read_json(paper_file, [])]
        content = _event_markdown(event, papers)
        (output / f"{event['id']}.md").write_text(content, encoding="utf-8")
        report = root / "reports" / "events" / f"{event['id']}.md"
        report.parent.mkdir(parents=True, exist_ok=True)
        report.write_text(content, encoding="utf-8")
