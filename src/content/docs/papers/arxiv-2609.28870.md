---
title: "When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse"
description: "Long-running LLM applications and autonomous agents repeatedly send growing context, making prefix caching critical for reducing prefill cost."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.28870) · [PDF](https://arxiv.org/pdf/2609.28870)

## 一句话摘要

Long-running LLM applications and autonomous agents repeatedly send growing context, making prefix caching critical for reducing prefill cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-running LLM applications and autonomous agents repeatedly send growing context, making prefix caching critical for reducing prefill cost. This raises a fundamental question: do decades of traditional cache-management techniques transfer directly to agentic and conversational LLM serving? We analyze production traces comprising over 20 billion processed tokens and evaluate 14 eviction algorithms across capacity-constrained HBM and large memory-pool settings. We find that simple Least Recently Used (LRU) is surprisingly robust, offering competitive performance against sophisticated traditional policies, though substantial headroom to Belady's optimum remains. The reason is structural: prefix reuse is dominated by the steady pacing of active sessions, making recency an unusually strong predictor for eviction. Nevertheless, prefix caching diverges from traditional workloads in ways that recency ignores, notably the prevalence of single-turn requests, extreme session footprint skew, and highly non-uniform miss costs because attention computation scales with token depth. To close the gap to optimality, we establish several design principles for prefix-cache management: keeping recency as the baseline while incorporating quick demotion to filter one-hit prompts, compute-aware eviction to prioritize expensive misses, and capacity-adaptive eviction granularity. Our traces and simulator are publicly available.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiyu Liu, Minlan Yu, Juncheng Yang
- 发布：2026-09-25；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
