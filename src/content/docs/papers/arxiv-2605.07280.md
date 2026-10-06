---
title: "Mask2Cause: Temporal Causal Discovery Beyond Causality in Mean"
description: "One approach to discovering causal relationships in multivariate time series is to ask whether a variable's history improves prediction of another variable."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.07280) · [PDF](https://arxiv.org/pdf/2605.07280)

## 一句话摘要

One approach to discovering causal relationships in multivariate time series is to ask whether a variable's history improves prediction of another variable.

## 为什么值得关注

待编辑增强。

## 摘要原文

One approach to discovering causal relationships in multivariate time series is to ask whether a variable's history improves prediction of another variable. When this improvement is measured solely by reductions in optimal squared error, the criterion misses relationships that affect the target's conditional variance without changing its conditional mean. We propose Mask2Cause, an end-to-end Transformer framework for causal discovery through conditional mean and variance prediction. Each variable's history is embedded as a separate token, and a single learnable adjacency matrix, shared across layers and attention heads, controls information exchange between tokens. Gaussian negative log-likelihood and a sparsity penalty on this matrix jointly train the forecasting model and graph. Our population analysis connects the optimal log-loss reduction to causally conditioned directed information, providing an information-theoretic motivation for the training objective. We introduce Mixed Physics, a benchmark with separately controlled mean and variance dependencies, to evaluate recovery of mean-only and variance-only edges. In its pure-variance setting, Mask2Cause achieves 1.000 off-diagonal AUROC, compared with 0.521 for a corresponding squared-error model. Experiments on linear, chaotic, biological, and real-data-derived benchmarks demonstrate competitive graph recovery, while the inferred graphs support downstream tasks such as causal pruning for efficient forecasting and root-cause localization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Omar Muhammad, Pasupuleti Dhruv Shivkant, Deepak N. Subramani
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
