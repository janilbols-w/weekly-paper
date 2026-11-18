---
title: "MeltKV: Memory-Aligned KV Cache Compression via Variable-Bit Packed Vector Quantization for Long-Context LLMs"
description: "Large Language Models (LLMs) increasingly rely on long contexts, making Key-Value (KV) caches dominate memory usage and inference latency."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.18652) · [PDF](https://arxiv.org/pdf/2611.18652)

## 一句话摘要

Large Language Models (LLMs) increasingly rely on long contexts, making Key-Value (KV) caches dominate memory usage and inference latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) increasingly rely on long contexts, making Key-Value (KV) caches dominate memory usage and inference latency. Existing vector quantization (VQ) methods effectively compress KV caches to sub-4-bit levels but often overlook inefficiencies in memory alignment and decoding speed. This work introduces MeltKV, a memory-latency co-optimized KV cache quantization framework for long-context LLM serving. MeltKV employs a memory-aligned variable-bit index packing scheme that adaptively assigns bit-widths to grouped key channels and compactly stores indices within standard data-types, eliminating redundant bits. Additionally, head-wise codebook sharing reduces the total codebook size while maintaining accuracy. Experiments demonstrate that MeltKV effectively compresses KV representations to sub-4-bit levels down to 1 bit and, at comparable perplexity, achieves 48.1% lower memory usage and 52.9% lower latency than state-of-the-art VQ methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiyun Han, Seongjoon Cho, Seungkyu Choi
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
