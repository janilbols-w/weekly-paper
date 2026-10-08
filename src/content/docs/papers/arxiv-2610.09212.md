---
title: "CurveTQ: Rotation-Free Trellis Quantization of LLM Weights via Curvature-Weighted Search"
description: "The best two-bit weight quantizers for large language models, such as QTIP and Proteus, rotate each weight matrix by a random orthogonal transform, which must be undone at every decoding step, then encode it with a trellis or lattice code under a Euclidean search; the layer Hessian enters only through error feedback between coding blocks."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.09212) · [PDF](https://arxiv.org/pdf/2610.09212)

## 一句话摘要

The best two-bit weight quantizers for large language models, such as QTIP and Proteus, rotate each weight matrix by a random orthogonal transform, which must be undone at every decoding step, then encode it with a trellis or lattice code under a Euclidean search; the layer Hessian enters only through error feedback between coding blocks.

## 为什么值得关注

待编辑增强。

## 摘要原文

The best two-bit weight quantizers for large language models, such as QTIP and Proteus, rotate each weight matrix by a random orthogonal transform, which must be undone at every decoding step, then encode it with a trellis or lattice code under a Euclidean search; the layer Hessian enters only through error feedback between coding blocks. We show that this leaves part of the Hessian unused. Error feedback turns the loss into a weighted sum of per-coordinate rounding errors whose weights, the diagonal of the Hessian's LDL factorization, existing quantizers compute but never read. We put these weights into the Viterbi branch metric, so the search follows the curvature within each coding block. This also explains the rotation: it removes this within-block variation, so weighting in the native basis and rotating are substitutes. On three models the weighted native search matches a full-dimension randomized Hadamard to within about one point of downstream accuracy, and weighting after the rotation gains little. Around this search we build CurveTQ, a trellis codec with no rotation, which handles the weights' amplitude and marginal shape with a factored scale field and a closed-form quantile table, and stores a start state per coding block so the trellis can adapt to the residual that error feedback carries into it. At two bits CurveTQ is 1-3 points higher in mean downstream accuracy than QTIP and Proteus on three 4-8B Instruct models, even after both are given our start state, which alone lifts either baseline by 1-3 points. It also leads on a 35B mixture of experts, to our knowledge the first trellis-coded result on such a model. With no rotation to undo, our decoder is the fastest of the three at all tested batch sizes and bit widths.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guanhua Ding, Zi Wang, Ruichao Li, Jack Liu
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
