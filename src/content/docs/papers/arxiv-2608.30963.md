---
title: "A Universal Context-Reuse Layer for Cross-Model KV Sharing"
description: "Modern large language model (LLM) serving systems increasingly operate over repeated or shared context, yet each model typically performs its own prefill computation even when another model has already processed the same input."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.30963) · [PDF](https://arxiv.org/pdf/2608.30963)

## 一句话摘要

Modern large language model (LLM) serving systems increasingly operate over repeated or shared context, yet each model typically performs its own prefill computation even when another model has already processed the same input.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern large language model (LLM) serving systems increasingly operate over repeated or shared context, yet each model typically performs its own prefill computation even when another model has already processed the same input. Existing KV-cache reuse mechanisms substantially reduce redundant computation within a single model, but generally assume that the producer and consumer of a cache are identical. We study \emph{cross-model KV sharing}, which translates the KV state produced by a source model into a representation that can be consumed by a different target model, including models that differ in scale, architecture, attention configuration, tokenizer, and model family. We evaluate the approach in both within-family and cross-family settings. For Qwen2.5-7B $\rightarrow$ Qwen2.5-1.5B, translated KV states improve LongBench2 accuracy from 27.59\% to 34.48\%, a gain of 6.89 percentage points over the native 1.5B baseline, while reducing handoff cost relative to native target prefill. For the cross-family Qwen2.5-1.5B $\rightarrow$ Gemma-2-2B setting, KV handoff reduces target-side prefill cost by up to 67.05\% at 4K context length while maintaining decoding perplexity close to native-model baselines. In a more heterogeneous Llama3.1-70B $\rightarrow$ Qwen2.5-7B setting, cross-family handoff achieves 44.0\% accuracy compared with 45.7\% for native Qwen2.5-7B inference, while reducing measured latency from 899ms to 138ms. These results provide initial evidence that KV states can serve as transferable computational representations rather than strictly model-local caches, and motivate \emph{context mobility} as a systems abstraction for reducing redundant prefill across heterogeneous LLM and multi-agent inference workflows.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Li, Dongming Jiang, Yi Zhao, Bingzhe Li
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
