---
title: "When to Ponder: Adaptive Compute Allocation for Code Generation via Test-Time Training"
description: "Large language models apply uniform computation to all inputs, regardless of difficulty."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2601.00894) · [PDF](https://arxiv.org/pdf/2601.00894)

## 一句话摘要

Large language models apply uniform computation to all inputs, regardless of difficulty.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models apply uniform computation to all inputs, regardless of difficulty. We propose PonderTTT, a gating strategy using the TTT layer's self-supervised reconstruction loss to selectively trigger Test-Time Training (TTT) updates. The gating decision itself is training-free--requiring no learned classifier or auxiliary networks; only a single scalar threshold is initially calibrated on unlabeled data and continuously adapted via EMA to maintain target update rates. Our experiments with GPT-2 models (124M to 1.5B) on code language modeling (The Stack v2, teacher-forced perplexity) demonstrate that this signal is inference-compatible, requiring no ground-truth labels. Our Reconstruction Gating achieves 82-89% Oracle Recovery while being fully training-free, significantly outperforming Random Skip baselines (up to 16% lower loss on OOD languages).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gihyeon Sim
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
