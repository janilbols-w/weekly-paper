---
title: "Q-PACE: Dynamic Precision Allocation for Quantization-Aware Training"
description: "Quantization-aware training (QAT) leverages lower-precision arithmetic to reduce the cost of LLM deployment, but aggressive quantization degrades final model performance."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.09183) · [PDF](https://arxiv.org/pdf/2610.09183)

## 一句话摘要

Quantization-aware training (QAT) leverages lower-precision arithmetic to reduce the cost of LLM deployment, but aggressive quantization degrades final model performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization-aware training (QAT) leverages lower-precision arithmetic to reduce the cost of LLM deployment, but aggressive quantization degrades final model performance. A common remedy is mixed-precision training, in which high precision is assigned to some of the layers to maintain performance while keeping the cost constrained. This approach then requires precision assignments for model layers during training. We provide a new approach, called Q-PACE, consisting of a second-order sensitivity model that predicts the loss increase as a sum of quantization noise MSE weighted by per-layer curvature coefficients. During training, we periodically re-compute these coefficients using perturbations across layers, and re-assign precision. Pretraining and supervised fine-tuning experiments on LLMs of up to 4B parameters show that Q-PACE consistently improves over existing mixed-precision training recipes, and achieves comparable loss at substantially lower total memory budgets. We further find that quantization sensitivity is highly predictable by depth and layer type, and its stability during training allows for infrequent, cheap recalibration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alexandra Volkova, Matin Ansaripour, Erik Schultheis, Christoph H. Lampert, Dan Alistarh
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
