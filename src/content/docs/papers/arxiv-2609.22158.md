---
title: "StepKV: Step-Aware KV Cache Compression for LLM Agents"
description: "Key-value (KV) caching is essential for efficient autoregressive large language model (LLM) inference, but the cache grows linearly with context length, increasing storage and decoding costs."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.22158) · [PDF](https://arxiv.org/pdf/2609.22158)

## 一句话摘要

Key-value (KV) caching is essential for efficient autoregressive large language model (LLM) inference, but the cache grows linearly with context length, increasing storage and decoding costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Key-value (KV) caching is essential for efficient autoregressive large language model (LLM) inference, but the cache grows linearly with context length, increasing storage and decoding costs. KV cache compression mitigates this cost by retaining only a subset of cached tokens. This challenge is particularly important for multi-step LLM agents, where a query expands into trajectories of reasoning, tool interactions, and retrieved observations. Existing pruning methods typically treat the cache as a flat token stream and rank tokens by recency or attention saliency. This creates a mismatch between the unit of compression and the unit of reasoning: token-level pruning removes individual entries, whereas useful information in multi-step agents is often organized into reasoning steps with uneven and delayed importance. Consequently, an early observation or intermediate decision may receive little recent attention yet remain essential for later evidence synthesis. We term this failure mode Reasoning Continuity Disruption.These observations motivate KV cache compression that jointly considers token- and reasoning-step-level information. StepKV addresses this goal by treating reasoning steps as first-class retention units. It associates cache entries with their generating steps, estimates step utility from trajectory-derived signals, and combines this utility with token-level saliency. The resulting scores globally rank prunable tokens, from which StepKV retains the top-scoring entries under a target budget. StepKV thus provides a step-centric perspective for agent KV cache compression. Across multi-hop QA and long-horizon web reasoning tasks, StepKV sustains accuracy under low KV budgets where token-level baselines degrade sharply, offering a more robust efficiency-accuracy trade-off for multi-step agent inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boyu Feng, Jiahong Liu, Yifan Li, Wenhao Yu, Zexuan Qiu, Yuliang Sun, Ming Shen, Xiang Li, Quanyu Dai, Irwin King
- 发布：2026-09-22；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
