from __future__ import annotations

from typing import Any, Dict, List

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

