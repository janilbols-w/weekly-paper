---
title: "Understanding KV Residency in Production-Scale Agentic LLM Workloads"
description: "Agentic large language model (LLM) applications turn one user request into a sequence of model and tool calls over a growing context."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.22863) · [PDF](https://arxiv.org/pdf/2610.22863)

## 一句话摘要

Agentic large language model (LLM) applications turn one user request into a sequence of model and tool calls over a growing context.

## 为什么值得关注

待编辑增强。

## 摘要原文

Agentic large language model (LLM) applications turn one user request into a sequence of model and tool calls over a growing context. Retaining this context's key-value (KV) state in GPU memory lets later calls reuse it instead of recomputing it, but at fleet scale this needs substantial memory. We characterize four production Microsoft M365 workload traces (Deep Research, Enterprise Assistant, Coding Agent and Enterprise Chat) spanning more than 121 million model calls. In Deep Research, the application issues 89% of model calls and the median context grows from about 10K to 68K tokens by the 30th call. About 80% of context tokens are served from the prefix cache. With the public Llama-2-70B KV layout standing in for confidential models, one 99th-percentile Deep Research session exceeds the 80 GB HBM of an NVIDIA H100, and holding all live sessions at their peak needs an estimated 501.8 TB of HBM, although inference occupies only 5.6% of that retention time. Trace-driven replay shows that a one-hour idle cap cuts this ceiling by 3.6x while raising the share of calls that recompute context only from 4.07% to 4.53%. Under tighter budgets, eviction alone is insufficient: at one tenth of the busiest hour's demand, LRU eviction makes 63% of Deep Research calls recompute and clairvoyant furthest-next-use 31%, whereas multi-resolution retention (MRR), which demotes the LRU session's KV state to int4, lowers this to 13.6%. Placement imposes a separate limit: when the next call reaches a different deployment, cached-context reuse drops from 89% to 29%, and treating KV state as deployment-local raises the recompute floor under unlimited memory from 5.4% to 20.2%. These findings motivate retention that changes the representation of KV state, together with deployment-aware routing or migration. We plan to release AgenticTraceSim, a parametric trace generator, and a residency replay framework.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mayank Arya, Agrim Bari, Anjaly Parayil, Yogesh Simmhan, Renee St. Amant, Victor R\"uhle, Saravan Rajmohan
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
