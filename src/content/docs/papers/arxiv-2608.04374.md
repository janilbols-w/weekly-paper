---
title: "FinReportBench: Measuring and Improving Institution-Grade Financial Report Generation"
description: "Large language models can produce fluent financial analysis, but fluency alone does not establish whether a report is suitable for institutional delivery."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2608.04374v1) · [PDF](https://arxiv.org/pdf/2608.04374v1)

## 一句话摘要

Large language models can produce fluent financial analysis, but fluency alone does not establish whether a report is suitable for institutional delivery.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models can produce fluent financial analysis, but fluency alone does not establish whether a report is suitable for institutional delivery. We introduce FinReportBench, an expert-grounded benchmark for measuring and improving institution-grade financial report generation. Expert review reveals recurring gaps in report identity, institutional components, source discipline, and visual delivery. We derive a 35-item rubric through expert partial orders, multimodal evidence, and audits of decision boundaries, covering deliverability, report identity, and institutional completeness. Starting from 10,000 balanced Chinese and English financial-research source records, we curate 244 bilingual tasks across three research objects and two input tiers. Each task separates the public query, reconstructed research trajectory, and hidden source packet. Three independent judge families reproduce the expert partial order at near-ceiling rates, showing that bounded, observable criteria support reliable evaluation. Across nine model families, basic deliverability is nearly saturated, while report identity and institutional completeness remain the primary bottlenecks. The largest cross-model gaps concern generation-trace control, information density, and data discipline rather than basic report framing. We then use benchmark-guided skill distillation to turn recurrent failures into reusable generation and self-review constraints. Across five model families, the evolved skill improves mean G1 by 33.85 points and mean G2 by 13.83 points over paired no-skill runs while preserving G0 for every pair. Code and benchmark artifacts are available at https://github.com/MisterBrookT/finreportbench.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yinghao Tang, Tan Zhenwei, Yiyao Wang, Wanli Gu, Xiaolu Zhang, Jun Zhou, Wei Chen
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/MisterBrookT/finreportbench](https://github.com/MisterBrookT/finreportbench)
- 阅读深度：metadata
