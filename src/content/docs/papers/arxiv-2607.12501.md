---
title: "Gauge-Fixing the Forward-Forward Objective: A Whitened Goodness Derived from a Likelihood-Ratio Account"
description: "The Forward-Forward algorithm trains each layer locally, so that a scalar goodness - the sum of squared activations - is high on real inputs and low on contrastive ones."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.12501) · [PDF](https://arxiv.org/pdf/2607.12501)

## 一句话摘要

The Forward-Forward algorithm trains each layer locally, so that a scalar goodness - the sum of squared activations - is high on real inputs and low on contrastive ones.

## 为什么值得关注

待编辑增强。

## 摘要原文

The Forward-Forward algorithm trains each layer locally, so that a scalar goodness - the sum of squared activations - is high on real inputs and low on contrastive ones. Under an explicit generative model this goodness is the sufficient statistic of a likelihood-ratio test, and the pairwise form of the objective admits a gauge: a layer can lower its loss by inflating the scale of its weights rather than by separating the two populations. The analysis prescribes the repair - a whitened, scale-invariant goodness trained online within each layer - which we evaluate as a training procedure. Across three corpora, three depths and a fourfold range of layer width (13 seeds per cell), it raises linear-probe accuracy over the standard pairwise objective in every measured cell - by 4 to 7 points on eight of nine corpus-depth combinations - and closes 16-61% of the gap to end-to-end backpropagation. A control isolates the mechanism: Hinton's fixed-threshold loss also bounds the runaway, to a factor of 1.4 against 133, yet tracks the unmodified baseline - invariance to the gauge, not a bound on it, is what pays. Against the strongest published alternative - a sparse, top-k goodness - the derived objective is statistically indistinguishable on two corpora of three, yet only it removes the runaway: sparsity and gauge-invariance are independent axes, and the published variant recovers accuracy while leaving the pathology in place. We state the boundaries we measured, and every prediction was recorded before its experiment with the refutations reported.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Paolo Giannitrapani
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
