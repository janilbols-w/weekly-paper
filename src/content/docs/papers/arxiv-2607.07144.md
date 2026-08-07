---
title: "Fractal KV-Cache Archives: Lossless Symbolic Storage with In-Place Retrieval for Long-Context LLM Inference"
description: "The key-value (KV) cache dominates the memory cost of long-context autoregressive inference, and a growing body of work compresses it through quantization, eviction, or offloading."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.07144) · [PDF](https://arxiv.org/pdf/2607.07144)

## 一句话摘要

The key-value (KV) cache dominates the memory cost of long-context autoregressive inference, and a growing body of work compresses it through quantization, eviction, or offloading.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache dominates the memory cost of long-context autoregressive inference, and a growing body of work compresses it through quantization, eviction, or offloading. We study a complementary question: once a position's KV state has been quantized to codebook indices, how should the resulting symbol stream be stored, and can the storage layer do more than store? A family of contractive iterated-map codes that serialize a symbol sequence into a sequence of low-dimensional real vectors is revisited, and it is shown that they form a natural archive format for a quantized KV cache with the following features. The method provides exactly the access pattern a growing cache requires. It is lossless, it runs in linear time, and supports O(1) random access and O(1) amortized append. A controlled study of the quantizer feeding this archive is conducted on GPT-2 with 1024-token contexts. Keeping a small exact window (4 attention sinks plus 32 recent tokens) and archiving the rest, per-head residual vector quantization reduces the archived cache by 36-54x relative to an fp16 cache at a perplexity cost of 11-15%, and we quantify a sharp key/value asymmetry - quantizing keys is roughly 4x more damaging than quantizing values, consistent with prior low-bit KV work - and use it to allocate bits in a hybrid scheme. Finally, we show the archive is simultaneously a search index: approximate substring queries execute directly on the stored vectors, and matched context is decoded from the matched vector without ever materializing the surrounding text. We further characterize the archive's operating range: truncating stored points yields a lossy regime whose distortion we localize, and probability-weighting the maps recovers arithmetic coding, exposing a trade-off between rate efficiency, random access, and memory. We release all code; every number reproduces on a laptop CPU.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Vladimir Gusev
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
