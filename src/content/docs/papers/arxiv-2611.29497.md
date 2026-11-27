---
title: "Gossamer: A Utility-Driven Architecture for Constant-Budget KV Cache Compression in Reasoning LLMs"
description: "Transformer-based large language models (LLMs) are increasingly applied to complex reasoning tasks, yet their inference efficiency is fundamentally constrained by the rapid growth of the KV cache."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.29497) · [PDF](https://arxiv.org/pdf/2611.29497)

## 一句话摘要

Transformer-based large language models (LLMs) are increasingly applied to complex reasoning tasks, yet their inference efficiency is fundamentally constrained by the rapid growth of the KV cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Transformer-based large language models (LLMs) are increasingly applied to complex reasoning tasks, yet their inference efficiency is fundamentally constrained by the rapid growth of the KV cache. As reasoning contexts extend to hundreds of thousands of tokens, the key-value (KV) cache becomes the dominant contributor to both memory footprint and bandwidth demand, tightly coupling computation with memory utilization and thereby limiting scalability. Existing compression methods, such as quantization and eviction, alleviate capacity pressure but remain purely algorithmic, often introducing additional passes and compute overhead that reduce system efficiency. This paper presents Gossamer, a KV cache compression architecture for reasoning LLMs that bridges the algorithm--system--hardware gap. Gossamer introduces a unified utility-based action framework that dynamically selects compression operations, quantization, merging, or eviction, under a constant KV cache budget. Through cross-domain co-design, we fuse cosine-similarity estimation directly into the attention computation, exploiting idle compute cycles to perform similarity evaluation without latency or bandwidth cost. We call this mechanism Free-Lunch Utilization. This enables real-time, fine-grained KV management with near-constant memory usage and negligible overhead. Under tight memory constraints, Gossamer sustains reasoning quality comparable to uncompressed inference while improving end-to-end throughput by up to 16.7$\times$ over uncompressed baselines, 5.5$\times$ and 4.9$\times$ over the quantization-based Oaken and Ecco, and 1.8$\times$ over the eviction-based R-KV.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 17 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Feng Cheng, Cong Guo, Junyao Zhang, Haoxuan Shan, Chiyue Wei, Hong Wang, Hai Li, Yiran Chen
- 发布：2026-11-22；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
