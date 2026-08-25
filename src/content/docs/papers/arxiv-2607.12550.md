---
title: "A JoLT for the KV cache: Near-lossless KV cache compression via joint Lagrangian allocation of Tucker ranks and a rotated residual for llms"
description: "The key-value (KV) cache has become the dominant memory cost of transformer inference: it grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the throughput ceiling."
---

**评分：51/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.12550) · [PDF](https://arxiv.org/pdf/2607.12550)

## 一句话摘要

The key-value (KV) cache has become the dominant memory cost of transformer inference: it grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the throughput ceiling.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache has become the dominant memory cost of transformer inference: it grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the throughput ceiling. Existing reductions fall into two families. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither exploits the fact that the cache at a layer is naturally a third-order tensor whose three axes, the heads, the tokens, and the features, carry very different amounts of redundancy. We take this tensor view directly. Our method, JoLT (Joint Lagrangian Tucker), applies a partial Tucker decomposition that compresses only the token and feature axes while leaving the head and layer axes intact, then restores the energy that truncation discards with a rotated low-bit residual: a random orthogonal rotation followed by low-bit quantization. A single Lagrangian dual allocates the Tucker ranks and the residual bit-widths together, per layer group and separately for keys and values, under one byte budget. The result is a near-lossless 2-3x compression. Perplexity stays near-lossless on both a grouped-query-attention model (Mistral-7B-v0.3) and a multi-head-attention model (LLaMA-2-13B), and GSM8K accuracy and needle-in-a-haystack retrieval hold at the uncompressed baseline at 2x on both architectures and through 3x on the GQA model. At 2x, JoLT reconstructs the cache to relative Frobenius error 0.009 (K) and 0.006 (V) on both architectures. A randomized-SVD variant, FlashJoLT, delivers a 5-13x compression-time speedup at 1024-token context and matched quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rahul Krishnan, Volker Schulz
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
