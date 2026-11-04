---
title: "C3: Speech-Guided KV Retrieval for Long-Context SpeechLLM Inference"
description: "Speech language models encode audio at a much higher rate than text, causing the KV cache to dominate the memory, bandwidth, and decoding cost of long-form generation."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.00333) · [PDF](https://arxiv.org/pdf/2611.00333)

## 一句话摘要

Speech language models encode audio at a much higher rate than text, causing the KV cache to dominate the memory, bandwidth, and decoding cost of long-form generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speech language models encode audio at a much higher rate than text, causing the KV cache to dominate the memory, bandwidth, and decoding cost of long-form generation. KV retrieval can reduce per-step access by attending to only a query-dependent subset of the cache, but existing methods are designed primarily for text and do not account for the structure of audio attention. We first show that retrieval errors may compound autoregressively into generation drift. We then analyze full audio attention during long-form generation and identify three properties relevant to retrieval: unequal attention concentration across query heads, non-contiguous audio support, and temporal continuity across decoding steps. Guided by these observations, we propose $C^3$(Cluster-Compete-Compete), which organizes audio KVs in a hierarchical key-space index, lets query heads sharing a KV head compete for a common retrieval budget, and adaptively reallocates retrieval resolution through paired split-merge updates. Across long-form speech recognition, translation, and summarization on four SpeechLLMs, $C^3$ achieves the strongest overall performance among retrieval methods under comparable final-KV access budgets, with particularly large gains in the tight-budget regime, while improving long-context decoding efficiency and accelerator-memory scaling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dancheng Liu, Markus M\"uller, Rupak Vignesh Swaminathan, Jing Liu, Srikanth Ronanki, Aram Galstyan
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
