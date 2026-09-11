---
title: "FlexComp: One Model for Every Ratio in Context Compression"
description: "Soft context compression condenses a context into a few memory tokens that a frozen LLM consumes in place of the raw text, but existing compressors fix the compression ratio at training and inference: each deployed ratio requires a separately trained model, and the chosen ratio is applied uniformly to all inputs, whose actual needs vary drastically."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.11192) · [PDF](https://arxiv.org/pdf/2609.11192)

## 一句话摘要

Soft context compression condenses a context into a few memory tokens that a frozen LLM consumes in place of the raw text, but existing compressors fix the compression ratio at training and inference: each deployed ratio requires a separately trained model, and the chosen ratio is applied uniformly to all inputs, whose actual needs vary drastically.

## 为什么值得关注

待编辑增强。

## 摘要原文

Soft context compression condenses a context into a few memory tokens that a frozen LLM consumes in place of the raw text, but existing compressors fix the compression ratio at training and inference: each deployed ratio requires a separately trained model, and the chosen ratio is applied uniformly to all inputs, whose actual needs vary drastically. We propose FlexComp, a method-agnostic framework that decouples the ratio from both training and deployment: Matryoshka-style training samples the memory budget $K$ per instance, turning one model into an any-ratio compressor, and the budget is then chosen per input by: (1) confidence-based cascade routing or (2) a lightweight learned $K$ predictor. Across ICAE, 500xCompressor, and SAC on MRQA, a single FlexComp model matches separately trained fixed-ratio specialists with minimal degradation. Cascade routing preserves over 98% of the mildest ratio's accuracy at up to 266x average compression; the $K$ predictor, in a single compression-decoding pass, reaches 158-236x within 0.7 F1 of the mildest ratio. At serving-scale batch sizes, the $K$ predictor cuts context KV cache by 50% and improves decoding throughput by 47%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kaiyan Zhao, Zhongtao Miao, Akiko Aizawa, Yoshimasa Tsuruoka
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
