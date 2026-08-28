---
title: "NestedKV: Nested Memory Routing for Long-Context KV Cache Compression"
description: "Long-context language models are limited by the memory footprint of the key-value (KV) cache."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.26678) · [PDF](https://arxiv.org/pdf/2605.26678)

## 一句话摘要

Long-context language models are limited by the memory footprint of the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context language models are limited by the memory footprint of the key-value (KV) cache. Existing training-free KV compression methods usually rank tokens by one importance signal -- attention, recency, layer-wise allocation, or key distinctiveness -- which becomes brittle when useful context is globally distinctive, locally episodic, or immediately relevant. We introduce NestedKV, a key-only KV cache compression method inspired by the Continuum Memory System in Nested Learning. NestedKV maintains global, block-level, and sliding-window key anchors, scores tokens by multi-time-scale cosine anomaly, and combines the resulting rankings with a training-free outer learner using head-adaptive mixing and surprise-gated token routing. The score is paired with adaptive per-head budgets and requires no training or LLM modification. Across RULER (4k--32k), LooGLE, LongBench, LongBench-E, InfiniteBench, and MMLU-Pro on Qwen3 and Llama-3.2 models, NestedKV is strongest when the retained cache is small. On Qwen3-4B, it improves over KeyDiff by up to 19.10 points on RULER and 19.29 on LongBench at $r=0.75$; at $r=0.95$, it retains 37.32 on LongBench versus 17.55 for KeyDiff.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hong Chen, Xiang Liu, Yubo Gao, Yuxuan Fan, Bo Wang, Yuanlin Chu, Yuanguo Lin, Xuming Hu
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
