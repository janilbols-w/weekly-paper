---
title: "FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models"
description: "Hybrid language models combine self-attention with recurrent layers whose in-place state updates restrict prefix reuse to exact saved positions."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2611.26020v1) · [PDF](https://arxiv.org/pdf/2611.26020v1)

## 一句话摘要

Hybrid language models combine self-attention with recurrent layers whose in-place state updates restrict prefix reuse to exact saved positions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid language models combine self-attention with recurrent layers whose in-place state updates restrict prefix reuse to exact saved positions. Saving states on a coarse grid wastes reusable prefixes, whereas existing fine-grained exact caches must cut the prefill forward pass at each mid-prompt checkpoint, adding scheduler steps that outweigh the reuse gains under load. We observe that across multi-turn chat, agent loops, document question answering, and tree search, prefix reuse almost always ends at structural boundaries predictable in advance, such as turn ends and known branch points. We present FrontierReplay, a prefix caching system that materializes exact checkpoints at these boundaries without cutting the prefill. While the forward pass runs uncut, FrontierReplay logs a short window of recurrent-layer inputs and invokes a cross-layer, state-only replay kernel to build the target state 6-37x cheaper per token than full recomputation without host synchronization. A frontier-aware retention policy prioritizes active anchors and proven branches while lending dead checkpoint slots to the attention KV cache. Across diverse hybrid architectures, model scales, and workloads, FrontierReplay delivers clear gains over existing exact caches, lowering median time to first token (TTFT) by 16-89% (up to 8.9x), raising 80% service-level objective (SLO) capacity by up to 1.73x, and improving goodput by up to 4.26x (3.67x at larger scales). Compared with approximate replay methods, FrontierReplay delivers up to 1.54x higher goodput while preserving exact task accuracy, avoiding the up to 17% accuracy drop suffered by approximation on long contexts.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zekun Wang, Yizhuo Wang
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
