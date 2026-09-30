---
title: "Affix Cache for Diffusion Large Language Models"
description: "Diffusion Large Language Models (DLLMs) enable non-autoregressive decoding, but efficient inference support remains immature: unlike autoregressive models, whose requests reuse a shared prefix key-value (KV) cache, DLLMs use bidirectional attention, so a shared context's KV states depend on the tokens still being decoded, leaving directly reused caches stale"
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.26140) · [PDF](https://arxiv.org/pdf/2608.26140)

## 一句话摘要

Diffusion Large Language Models (DLLMs) enable non-autoregressive decoding, but efficient inference support remains immature: unlike autoregressive models, whose requests reuse a shared prefix key-value (KV) cache, DLLMs use bidirectional attention, so a shared context's KV states depend on the tokens still being decoded, leaving directly reused caches stale

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion Large Language Models (DLLMs) enable non-autoregressive decoding, but efficient inference support remains immature: unlike autoregressive models, whose requests reuse a shared prefix key-value (KV) cache, DLLMs use bidirectional attention, so a shared context's KV states depend on the tokens still being decoded, leaving directly reused caches stale and full recomputation necessary. We present ACache, a cross-request cache reuse mechanism for shared spans, or affixes, at any position: prefix, infix, or suffix. ACache measures the influence of affix tokens on the masked generation region to identify a small request-specific subset as Anchor Tokens, and recomputes only their KV states while reusing the remaining affix cache. Built on state-of-the-art intra-request caching mechanisms, ACache recovers most of the accuracy lost to direct affix-cache reuse on average when recomputing around 20% of affix tokens, and at that budget preserves more accuracy than selection criteria adapted from prior cross-request cache-reuse systems. We co-design ACache with a modern inference engine, whose attention reads each request's recomputed Anchor KV states alongside one affix cache shared across concurrent requests. Against the same system with only intra-request caching, ACache cuts recompute latency by up to 56.7%, translating to as much as 1.71$\times$ end-to-end throughput, while reducing peak KV cache memory by up to 45.8%.

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

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaihua Liang, An Zhong, Xin Tan, Zafar Ayyub Qazi, Hong Xu, Jian Weng, Marco Canini
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
