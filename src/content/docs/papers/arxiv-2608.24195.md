---
title: "A Heterogeneous Mixture of Experts Framework for Interpretable Machine Learning"
description: "Mixture-of-Experts (MoE) models provide a flexible framework for partitioning complex prediction problems into simpler local learning tasks through an input-dependent gating mechanism."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2608.24195) · [PDF](https://arxiv.org/pdf/2608.24195)

## 一句话摘要

Mixture-of-Experts (MoE) models provide a flexible framework for partitioning complex prediction problems into simpler local learning tasks through an input-dependent gating mechanism.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models provide a flexible framework for partitioning complex prediction problems into simpler local learning tasks through an input-dependent gating mechanism. Existing interpretable MoE approaches, such as Mixture of Decision Trees (MoDT), achieve transparency by employing homogeneous decision-tree experts, but this restricts the model to a single inductive bias across all regions of the feature space. We extend the MoDT framework by introducing heterogeneous expert families comprising decision trees, linear support vector machines, and quadratic discriminant analysis under a common probabilistic gating mechanism. To ensure coherent likelihood-based inference, non-probabilistic experts are calibrated to produce conditional class probabilities, allowing parameter estimation within the generalized Expectation-Maximization framework of MoDT. We further establish theoretical monotone ascent guarantees for the proposed heterogeneous gating updates, providing a justification for the optimization procedure. Experiments on a diverse collection of synthetic and real-world benchmark datasets demonstrate that the proposed framework adaptively specializes experts according to local data geometry, yielding interpretable expert assignments while achieving predictive performance competitive with homogeneous MoDT and Random Forests. The proposed approach combines interpretability, adaptive inductive bias selection, and probabilistic coherence within a unified mixture-of-experts framework.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Soham Chatterjee, Rwitobroto Dey, Smarajit Bose
- 发布：2026-08-25；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
