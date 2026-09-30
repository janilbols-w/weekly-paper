---
title: "Output-aware Residual Stream Pruning for Large Language Models"
description: "Residual stream pruning methods reduce inference cost by shrinking the model's hidden dimension, but existing approaches typically choose these dimensions by minimizing activation reconstruction error."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.35579) · [PDF](https://arxiv.org/pdf/2609.35579)

## 一句话摘要

Residual stream pruning methods reduce inference cost by shrinking the model's hidden dimension, but existing approaches typically choose these dimensions by minimizing activation reconstruction error.

## 为什么值得关注

待编辑增强。

## 摘要原文

Residual stream pruning methods reduce inference cost by shrinking the model's hidden dimension, but existing approaches typically choose these dimensions by minimizing activation reconstruction error. This criterion implicitly treats all perturbation directions as equally important, ignoring the sensitivity of downstream layers. We introduce a sensitivity-aware approach to residual-stream pruning that directly accounts for this direction-dependent sensitivity. Using a second-order approximation to the output KL divergence, we characterize the effect of a residual-stream perturbation through both its activation covariance and the local sensitivity of the model output. The resulting subspace selection objective couples these two quantities, but is difficult to optimize directly. We derive a tractable spectral upper bound that reduces subspace selection to an eigendecomposition of a sensitivity-weighted covariance matrix, retaining the efficiency and structural simplicity of rotation-based pruning methods. Across several instruction-tuned language model families, our method consistently reduces calibration KL divergence relative to activation-only pruning and improves perplexity and downstream task performance over a range of compression levels. Our results show that preserving activation energy alone is insufficient for residual-stream pruning, and that explicitly accounting for how perturbations propagate to the model output provides a more effective criterion for selecting dimensions to remove.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chayne Thrash, Kevin Chen, Soheil Kolouri
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
