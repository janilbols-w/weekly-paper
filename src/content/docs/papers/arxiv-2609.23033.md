---
title: "WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models"
description: "Looped language models repeatedly apply a weight-shared block to increase effective depth without increasing parameter count, but the resulting T sequential recurrent-block calls per generated token substantially increase decoding latency."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.23033) · [PDF](https://arxiv.org/pdf/2609.23033)

## 一句话摘要

Looped language models repeatedly apply a weight-shared block to increase effective depth without increasing parameter count, but the resulting T sequential recurrent-block calls per generated token substantially increase decoding latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models repeatedly apply a weight-shared block to increase effective depth without increasing parameter count, but the resulting T sequential recurrent-block calls per generated token substantially increase decoding latency. To address the issue, we introduce Wavefront Decoding (WFD), a training-free self-speculative decoding framework designed for looped language models. WFD exploits two properties of these architectures: intermediate recurrence outputs provide effective draft predictions, and weight sharing allows token states at different positions and recurrence depths to be processed in one batched recurrent-block call. WFD organizes these mixed-depth states into a diagonal wavefront, continuously drafting new positions at shallow depth while advancing earlier positions toward full-depth verification. Unlike the phase-separated draft-then-verify schedule, WFD therefore co-batches drafting and verification within the same recurrent calls, while rejected drafts are corrected using full-depth predictions. Across six Spec-Bench task categories, WFD achieves 2.42x speedup on Ouro-2.6B and 3.54x on Huginn-3.5B over autoregressive decoding, consistently outperforming draft-then-verify. Cross-recurrence KV sharing further reduces wavefront KV traffic and increases WFD's speedup to 4.81x on Huginn-3.5B.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hyeongju Ha, Jae-Joon Kim
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
