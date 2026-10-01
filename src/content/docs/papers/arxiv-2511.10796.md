---
title: "Fast Generalized Neural Tangent Kernel Statistics via Trace Estimation"
description: "The empirical state-space Neural Tangent Kernel (NTK) describes the local learning geometry of a finite-width neural network, but computing it explicitly is almost always impractical in terms of computation and memory costs."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2511.10796) · [PDF](https://arxiv.org/pdf/2511.10796)

## 一句话摘要

The empirical state-space Neural Tangent Kernel (NTK) describes the local learning geometry of a finite-width neural network, but computing it explicitly is almost always impractical in terms of computation and memory costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

The empirical state-space Neural Tangent Kernel (NTK) describes the local learning geometry of a finite-width neural network, but computing it explicitly is almost always impractical in terms of computation and memory costs. Here, we show that many useful NTK statistics that characterize, for example, the dimensionality of learned updates or how two models or learning rules relate, can instead be efficiently approximated to very high accuracy via matrix-free products using randomized trace estimation. Namely, we use Hutch++ to estimate the NTK trace, Frobenius norm, effective rank, and alignment. Furthermore, we show that the positive-semidefinite structure of the NTK yields one-sided estimators that require only forward- or reverse-mode automatic differentiation. We validate these estimators across MLPs, recurrent GRUs, and a natural-language Transformer with up to 410 million parameters, in which the state-space contains high-dimensional four-tensors. We demonstrate orders-of-magnitude speedups, with the fastest estimator in a given application depending on the ratio of parameter and state dimensions. Equipped with these estimators, we examine rich and lazy RNN training using hidden-state NTK alignment and use NTK alignment as a regularizer for data-scarce knowledge distillation. We find that this regularization can modestly improve generalization, especially in very data-scarce settings. Together, these results suggest state-space NTK diagnostics are practical even at large scales.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：James Hazelden, Balaaji Reddy Nagireddy, Eric Shea-Brown
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
