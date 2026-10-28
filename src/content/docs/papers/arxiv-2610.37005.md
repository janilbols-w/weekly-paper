---
title: "Compote: Collapse-Resistant Multiple Hypothesis Learning For Sequential Recommendation"
description: "Next-item prediction is inherently ambiguous: a single interaction history often admits multiple plausible continuations across distinct catalogue regions."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.37005) · [PDF](https://arxiv.org/pdf/2610.37005)

## 一句话摘要

Next-item prediction is inherently ambiguous: a single interaction history often admits multiple plausible continuations across distinct catalogue regions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Next-item prediction is inherently ambiguous: a single interaction history often admits multiple plausible continuations across distinct catalogue regions. Standard sequential recommenders compress these alternatives into a single prediction, conflating user intents. We introduce COllapse-resistant Multiple hyPOThesis lEarning (COMPOTE), a multi-hypothesis transformer trained with an annealed objective that transitions from uniform supervision to a winner-takes-all assignment. This mechanism forces hypotheses to specialize into distinct catalogue regions, while inference relies on an efficient, normalizer-free max-similarity rule. Theoretically, we show that in the population case, the optimal solutions partition the conditional next-item distribution according to a max-entropy quantization principle, while pooled scores preserve the Bayes-optimal ranking. We also prove a generalization bound scaling logarithmically with the number of hypotheses. Across three Amazon Reviews 2023 benchmarks, COMPOTE outperforms strong ID-based, generative, and multi-interest baselines using item IDs alone. Matched-capacity ablations confirm that performance gains stem directly from the annealed objective, preventing the head collapse observed in conventional multi-head architectures, rather than added capacity, ensembling, or routing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Louis Castres Saint Martin, Clement Calauzenes, Alain Rakotomamonjy, Patrick Gallinari
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
