---
title: "When Fancy Eviction Fails: Rethinking Cache Replacement For LLM Prefix Reuse"
description: "Long-running LLM applications repeatedly send growing context, making prefix caching critical for reducing prefill cost."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.28870) · [PDF](https://arxiv.org/pdf/2609.28870)

## 一句话摘要

Long-running LLM applications repeatedly send growing context, making prefix caching critical for reducing prefill cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-running LLM applications repeatedly send growing context, making prefix caching critical for reducing prefill cost. Yet prefix-cache behavior under agentic workloads remains poorly understood. We study production traces from two companies and evaluate 14 eviction algorithms across HBM-constrained and large memory-pool settings. Despite a large gap to Belady, sophisticated policies designed for traditional caches provide little benefit over LRU. The reason is structural: prefix reuse is dominated by the regular pacing of active sessions, making recency unusually predictive. Prefix caching nevertheless introduces new challenges, including heavy-tailed session footprints and highly variable miss costs as attention computation grows with sequence length. We introduce the compute-savings ratio and two offline oracles to quantify these effects. Our results show that effective prefix-cache management should retain recency as its foundation while selectively adding quick demotion for one-hit prefixes, compute-aware partial eviction for expensive misses, and capacity-dependent eviction granularity. We will release the traces and simulator to support future research.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiyu Liu, Minlan Yu, Juncheng Yang
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
