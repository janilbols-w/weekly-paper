---
title: "LazyFlash: Forward-Dense, Backward-Sparse Attention for Accelerated Long-Context Fine-Tuning"
description: "As large language models (LLMs) process increasingly long sequences, attention becomes a major computational bottleneck."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.31911) · [PDF](https://arxiv.org/pdf/2610.31911)

## 一句话摘要

As large language models (LLMs) process increasingly long sequences, attention becomes a major computational bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) process increasingly long sequences, attention becomes a major computational bottleneck. Sparse attention mostly targets inference, yet many methods still train densely or cannot support sparse training, and their added complexity makes sparsity hard to turn into wall-clock speedups, leaving dense attention widely used in practice. This paper introduces LazyFlash, a forward-dense, backward-sparse attention method built on the observation that attention training is dominated by the backward pass. LazyFlash keeps the forward pass exactly dense, so the trained model remains a standard dense model that existing systems such as vLLM can serve without any change. For the backward pass, LazyFlash proposes a gradient-aware block sparsification design that ranks query blocks by their attention-output gradient norms and skips those contributing negligibly to parameter updates, turning the dense backward into a block-sparse one. A gradient-mass budget adapts the amount of skipped computation to each head and training step, while importance sampling preserves the dense gradient in expectation. These designs are implemented inside the tiled FlashAttention backward kernel, where skipped blocks are never loaded or computed, translating gradient sparsity into real wall-clock acceleration. Experiments on long-context text and speech LLMs show that LazyFlash maintains downstream performance while achieving up to 5.7x attention-backward speedup over FlashAttention and 1.7x end-to-end training speedup.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Keqi Deng, Ruchao Fan, Jinyu Li
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
