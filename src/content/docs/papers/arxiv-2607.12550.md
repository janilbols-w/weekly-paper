---
title: "A JoLT for the KV cache: Near-Lossless KV Cache Compression via Joint Rank-bit Allocation"
description: "The key-value (KV) cache is the dominant memory bottleneck in long-context language model inference."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.12550) · [PDF](https://arxiv.org/pdf/2607.12550)

## 一句话摘要

The key-value (KV) cache is the dominant memory bottleneck in long-context language model inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache is the dominant memory bottleneck in long-context language model inference. Existing compression methods apply low-rank factorization or quantization independently, without jointly allocating rank and precision under a shared storage budget. We introduce JoLT, a training-free compressor that treats grouped prefill caches as fourth-order tensors and applies partial Tucker decomposition along the token and feature modes, the two axes that carry low-rank structure, while leaving the head and layer modes intact. A rotated low-bit quantizer captures the truncation residual, and a single Lagrangian dual allocates per-group Tucker ranks and residual bit-widths under a global byte constraint. FlashJoLT replaces the exact token-mode SVD with a randomized approximation that matches JoLT within the free zone at a fraction of the compression cost, and a fused Triton decode kernel evaluates attention directly over the stored factors without materializing dense KV tensors. Across five models from four architecture families, covering multi-head attention, grouped-query attention, and mixture-of-experts architecture, JoLT achieves 2 - 3x compression with less than 0.2% perplexity degradation, without retraining. On RULER at 64K context with LLaMA-3.1-8B, retrieval accuracy remains near-lossless through 3x and declines by only 0.90 and 2.40pp at 4x and 5x, respectively. JoLT demonstrates that tensor-aware low-rank decomposition and quantized residuals, unified under a single storage budget, achieve near-lossless KV-cache compression across diverse model architectures without retraining.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rahul Krishnan, Volker Schulz
- 发布：2026-08-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
