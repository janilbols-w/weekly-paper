---
title: "LoopKV: Loop-Aware KV Cache Compression for Serving Looped Transformers"
description: "Looped transformers apply a shared block several times per token to improve accuracy without adding parameters."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.04137) · [PDF](https://arxiv.org/pdf/2611.04137)

## 一句话摘要

Looped transformers apply a shared block several times per token to improve accuracy without adding parameters.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped transformers apply a shared block several times per token to improve accuracy without adding parameters. For models such as Ouro that keep a separate key-value (KV) cache per loop, cache memory limits the batch size that amortizes repeated weight reads. Uniform-bit quantization and fixed rules per loop do not allocate precision according to each layer's sensitivity in each loop. Measurements on Ouro show that quantization sensitivity varies across (loop, layer) cells, and the sum of individual cell damages approximates the overall output damage. Sharing damage also varies by cell, with later loops generally tolerating sharing better. Skipping low-attention values to save reads produces errors that compound across loops. LoopKV uses a one-time offline profile to choose 4-bit storage, 2-bit storage or reuse of the final loop's KV for each cell. The planner minimizes reads under budgets for predicted damage and storage. During decoding, each loop reads the high 2 bits of each 4-bit value and fetches the low bits only where its own attention weights require 4-bit precision. A single fused kernel in vLLM executes the plan. Serving Ouro-1.4B on one RTX PRO 6000, the memory-optimized LoopKV-M plan stores 35% less KV than uniform 4-bit quantization (KIVI-4) on the same fused kernel and CUDA graph. It sustains 1.7-2.2x KIVI-4's goodput under a latency service-level objective with a 16K-token maximum length. None of its averages on six public benchmarks falls significantly below BF16's.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tianle Zhou, Yang Zhang, Tianyu Wu, Zhuohan Wang, William Nixon, Juncheng Yang
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
