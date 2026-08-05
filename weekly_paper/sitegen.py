from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List

from .models import Paper
from .storage import safe_id
from .utils import write_json


def _frontmatter(title: str, description: str = "") -> str:
    lines = ["---", f"title: {json.dumps(title, ensure_ascii=False)}"]
    if description:
        lines.append(f"description: {json.dumps(description, ensure_ascii=False)}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def _category_label(paper: Paper) -> str:
    path = paper.primary_category
    return " > ".join(
        filter(None, [path.get("domain_zh"), path.get("group_zh"), path.get("leaf_zh")])
    )


def _paper_markdown(paper: Paper) -> str:
    content = [_frontmatter(paper.title, paper.summary_zh or paper.summary_en)]
    content.extend(
        [
            f"**评分：{paper.score}/100** · {_category_label(paper)}",
            "",
            f"[论文原文]({paper.url})" + (f" · [PDF]({paper.pdf_url})" if paper.pdf_url else ""),
            "",
            "## 一句话摘要",
            "",
            paper.summary_zh or paper.summary_en or "暂无摘要。",
            "",
            "## 为什么值得关注",
            "",
            paper.why_it_matters_zh or "待编辑增强。",
            "",
            "## 摘要原文",
            "",
            paper.abstract,
            "",
            "## 质量评分",
            "",
            "| 维度 | 得分 |",
            "|---|---:|",
        ]
    )
    for key, value in paper.score_components.items():
        content.append(f"| {key.replace('_', ' ')} | {value} |")
    content.extend(["", "## 证据与限制", ""])
    for evidence in paper.score_evidence:
        content.append(f"- {evidence}")
    if paper.limitations_zh:
        content.append(f"- 限制：{paper.limitations_zh}")
    content.extend(["", "## 元数据", ""])
    content.append(f"- 作者：{', '.join(paper.authors) or '未知'}")
    content.append(f"- 发布：{paper.published}；更新：{paper.updated}")
    content.append(f"- 来源：{paper.source}；Venue：{paper.venue or paper.journal_ref or '未确认'}")
    content.append(f"- 代码：{f'[{paper.code_url}]({paper.code_url})' if paper.code_url else '未发现'}")
    content.append(f"- 阅读深度：{paper.reading_depth}")
    return "\n".join(content) + "\n"


def _week_markdown(week: Dict[str, Any], by_id: Dict[str, Paper]) -> str:
    title = f"论文周报 · {week['week']}"
    lines = [
        _frontmatter(title, f"{week['start_date']} 至 {week['end_date']}"),
        f"> 收录 {len(week['paper_ids'])} 篇，精选 {len(week['featured_ids'])} 篇。",
        f"> 数据版本：`{week['digest'][:12]}`",
        "",
        "## 本周精选",
        "",
    ]
    for paper_id in week["featured_ids"]:
        paper = by_id.get(paper_id)
        if not paper:
            continue
        lines.extend(
            [
                f"### [{paper.title}](../../papers/{safe_id(paper.id)}/)",
                "",
                f"**{paper.score}/100 · {_category_label(paper)}**",
                "",
                paper.summary_zh or paper.summary_en,
                "",
            ]
        )
    lines.extend(["## 其他收录", "", "| 论文 | 分类 | 评分 |", "|---|---|---:|"])
    featured = set(week["featured_ids"])
    for paper_id in week["paper_ids"]:
        if paper_id in featured or paper_id not in by_id:
            continue
        paper = by_id[paper_id]
        lines.append(
            f"| [{paper.title}](../../papers/{safe_id(paper.id)}/) | {_category_label(paper)} | {paper.score} |"
        )
    return "\n".join(lines) + "\n"


def _topic_markdown(leaf: Dict[str, Any], papers: List[Paper]) -> str:
    lines = [
        _frontmatter(leaf["name_zh"], leaf["name"]),
        f"三级分类：**{leaf['domain_zh']} > {leaf['group_zh']} > {leaf['name_zh']}**",
        "",
        f"累计收录 **{len(papers)}** 篇。",
        "",
        "| 论文 | 时间 | 评分 |",
        "|---|---|---:|",
    ]
    for paper in sorted(papers, key=lambda item: (item.published, item.score), reverse=True):
        lines.append(f"| [{paper.title}](../../papers/{safe_id(paper.id)}/) | {paper.published} | {paper.score} |")
    return "\n".join(lines) + "\n"


def build_site_data(root: Path, papers: List[Paper], weeks: List[dict], taxonomy: Dict[str, Any]) -> None:
    papers = sorted(papers, key=lambda item: (item.published, item.score), reverse=True)
    weeks = sorted(weeks, key=lambda item: item.get("week", ""), reverse=True)
    by_id = {paper.id: paper for paper in papers}
    paper_values = [paper.to_dict() for paper in papers]
    write_json(root / "src" / "data" / "papers.json", paper_values)
    write_json(root / "src" / "data" / "weeks.json", weeks)
    write_json(root / "src" / "data" / "taxonomy.json", taxonomy)
    write_json(root / "public" / "papers.json", paper_values)

    leaf_counts = Counter(paper.primary_category.get("leaf_id", "") for paper in papers)
    domain_counts = Counter(paper.primary_category.get("domain_id", "") for paper in papers)
    week_counts = {week["week"]: len(week["paper_ids"]) for week in weeks}
    stats = {
        "total_papers": len(papers),
        "total_weeks": len(weeks),
        "featured_total": sum(len(week.get("featured_ids", [])) for week in weeks),
        "code_available": sum(bool(paper.code_url) for paper in papers),
        "leaf_counts": dict(leaf_counts),
        "domain_counts": dict(domain_counts),
        "week_counts": week_counts,
    }
    write_json(root / "src" / "data" / "stats.json", stats)

    for directory in ("papers", "weekly", "topics"):
        generated = root / "src" / "content" / "docs" / directory
        generated.mkdir(parents=True, exist_ok=True)
        for path in generated.glob("*.md"):
            path.unlink()

    for paper in papers:
        path = root / "src" / "content" / "docs" / "papers" / f"{safe_id(paper.id)}.md"
        path.write_text(_paper_markdown(paper), encoding="utf-8")
    for week in weeks:
        path = root / "src" / "content" / "docs" / "weekly" / f"{week['week'].lower()}.md"
        path.write_text(_week_markdown(week, by_id), encoding="utf-8")

    papers_by_leaf: Dict[str, List[Paper]] = defaultdict(list)
    for paper in papers:
        papers_by_leaf[paper.primary_category.get("leaf_id", "")].append(paper)
    for domain in taxonomy["domains"]:
        for group in domain["groups"]:
            for leaf in group["leaves"]:
                enriched = dict(leaf)
                enriched.update(
                    {
                        "domain_zh": domain["name_zh"],
                        "group_zh": group["name_zh"],
                    }
                )
                path = root / "src" / "content" / "docs" / "topics" / f"{leaf['id']}.md"
                path.write_text(_topic_markdown(enriched, papers_by_leaf[leaf["id"]]), encoding="utf-8")
