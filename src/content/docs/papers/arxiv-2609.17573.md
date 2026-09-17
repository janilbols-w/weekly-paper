---
title: "GroupKV: Hierarchical KV Cache Management for Long-Context Diffusion LLM Inference"
description: "Diffusion large language models (dLLMs) are emerging as a promising generative paradigm that complements autoregressive decoding."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.17573) · [PDF](https://arxiv.org/pdf/2609.17573)

## 一句话摘要

Diffusion large language models (dLLMs) are emerging as a promising generative paradigm that complements autoregressive decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion large language models (dLLMs) are emerging as a promising generative paradigm that complements autoregressive decoding. In long-context settings, KV cache bloat and offloading transfer overhead have become primary bottlenecks in inference systems. Meanwhile, the periodic full-sequence recomputation and localized token updates in dLLMs make the KV lifecycle substantially more dynamic, complicating cache management and prefetch scheduling while making heavyweight token-level indexing or clustering schemes harder to amortize effectively during decoding. To address these challenges, we present \textsc{GroupKV}, a lightweight hierarchical KV cache management system for long-context dLLM inference. We observe that under block-wise decoding, tokens within the same generation block tend to access highly overlapping and spatially concentrated context regions, making group-level sparse selection effective. Building on this observation, \textsc{GroupKV} partitions the context into contiguous groups and performs coarse-to-fine sparse selection. \textsc{GroupKV} further exploits cross-layer consistency to enable predictive prefetching, and incorporates a staleness correction mechanism to maintain cache coherence under dynamic KV updates. Additionally, \textsc{GroupKV} adopts streaming prefill to reduce peak memory consumption during prefilling. Experiments show that \textsc{GroupKV} extends the maximum serviceable context length by up to $48.00\times$ under constrained GPU memory, improves end-to-end inference performance by up to $3.73\times$ in offload-based long-context settings, and maintains competitive task accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinhao Wang, Zhexin Hu, Kangjie Zhou, Xin Zhou, Fangfang Liu
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
