---
title: "Stream-CQSA: Exact Out-of-Memory Recovery for Attention"
description: "Long-context large language models are limited not only by attention cost but also by out-of-memory (OOM) failures."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2604.20819) · [PDF](https://arxiv.org/pdf/2604.20819)

## 一句话摘要

Long-context large language models are limited not only by attention cost but also by out-of-memory (OOM) failures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context large language models are limited not only by attention cost but also by out-of-memory (OOM) failures. A selected attention call may not fit in available device memory even when the kernel is optimized. Exact and approximate attention methods reduce memory use, but every fixed implementation still has a device-specific capacity boundary. We introduce Stream-CQSA, an attention-level OOM recovery framework based on CQS decomposition, derived from the theory of cyclic quorum sets (CQS). Stream-CQSA recursively partitions an infeasible attention call into independent subsequence tasks, executes each with a compatible inner kernel, and recomposes the local statistics to recover the full attention output. This recovery is exact relative to the wrapped attention kernel, whether that kernel is exact or approximate. Compared with FlashAttention-2, the major baseline, our native Stream-CQSA kernel improves 16-bit forward-output error relative to a dense float64 reference and matches 16-bit backward-gradient error where FlashAttention-2 fits in the GPU memory. At the longest feasible baseline length, it costs $1.5$--$1.9\times$ the forward runtime and $2.1$--$2.4\times$ the forward--backward runtime. Beyond that sequence length boundary, our method continues to return an output while FlashAttention-2 OOMs. Stream-CQSA is therefore not a faster attention method. Instead, it converts memory-capacity failure into a recoverable execution path by trading extra compute, host-device transfer, and recomposition for completion.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiming Bian, Joshua M. Akey
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
