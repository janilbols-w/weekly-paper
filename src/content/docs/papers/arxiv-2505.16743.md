---
title: "TRIM: Achieving Extreme Sparsity with Targeted Row-wise Iterative Metric-driven Pruning"
description: "Large language models (LLMs) present substantial computational and memory challenges."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2505.16743) · [PDF](https://arxiv.org/pdf/2505.16743)

## 一句话摘要

Large language models (LLMs) present substantial computational and memory challenges.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) present substantial computational and memory challenges. Existing one-shot pruning methods often use a uniform sparsity target for all rows within a layer, which can be too coarse at high sparsity. This work introduces TRIM (Targeted Row-wise Iterative Metric-driven pruning), a forward-statistics-based wrapper that allocates different sparsity ratios to individual output rows while keeping model weights frozen. TRIM separates the choice of which weights to prune (scoring) from how many to prune in each row (allocation), and composes with existing scorers and layer-wise allocations. Across Qwen2.5, LLaMA-2, and OPT models, its largest gains occur at 70-80% sparsity. At 80%, adding TRIM to OWL reduces WikiText-2 perplexity from 348.48 to 180.67 for Qwen2.5-14B and from 6461.43 to 324.14 for OPT-13B. We conclude that fine-grained, row-wise allocation is an effective mechanism for substantially improving one-shot pruning quality in the extreme-sparsity regime. Code: https://github.com/flobk/TRIM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Florentin Beck, William Rudman, Carsten Eickhoff
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/flobk/TRIM](https://github.com/flobk/TRIM)
- 阅读深度：metadata
