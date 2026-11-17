---
title: "MineralExp: Benchmarking LLM Agents for Experimental Design in Real-World Mineral Exploration"
description: "In mineral exploration, verifying geological hypotheses relies on designing a variety of geochemical experiments."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.17931) · [PDF](https://arxiv.org/pdf/2611.17931)

## 一句话摘要

In mineral exploration, verifying geological hypotheses relies on designing a variety of geochemical experiments.

## 为什么值得关注

待编辑增强。

## 摘要原文

In mineral exploration, verifying geological hypotheses relies on designing a variety of geochemical experiments. While large language model (LLM) agents increasingly automate downstream geoscientific data analysis, a crucial upstream capability remains largely unexplored: automated geochemical experimental design, i.e., deciding which experiments to conduct before committing to costly laboratory work. Evaluating this capability of LLM agents is difficult for two reasons. First, geochemical experiments exhibit high methodological diversity and subjectivity: to test the same hypothesis, different geologists may choose different minerals and instruments, so no single protocol can serve as the reference answer. Second, open-ended experimental plans resist representation as structured labels, which makes objective scoring difficult. To address these challenges, we introduce MineralExp, a benchmark that reformulates geochemical experimental design as a hypothesis-based experiment selection problem, i.e., a multi-label classification problem. We abstract concrete instrument names and procedural details into a shared taxonomy of 19 experimental types across five mineral-system processes: Source, Transport, Deposition, Modification, and Preservation. This taxonomy yields deterministic multi-label targets while accommodating diverse experimental protocols. Constructed from published ore-deposit literature and verified by domain experts, MineralExp comprises 277 cases and 1,572 reference experimental plans. Given a geological hypothesis and initial context, an LLM agent selects the relevant tasks and generates concrete experimental plans, which are scored by multi-label classification metrics and an LLM-as-a-Judge metric. The experimental results show that current agents generally achieve high recall but low precision, tending to propose more experiments than are necessary to test the hypothesis.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bing Wang, Mingyang Wang, Yuanhang Mi, Yue Xu, Kaibo Su, Li'ang Xiao, Chunguo Wu, Changchun Li, Ximing Li, Kun-Feng Qiu, Bo Yang
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
