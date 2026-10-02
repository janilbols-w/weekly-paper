---
title: "Capture the lifecycle: KV Cache management in ReAct Agents with KVTether"
description: "Efficient serving of long-context reasoning-and-acting (ReAct) agents relies on KV cache reuse to reduce large language model (LLM) prefill latency and monetary cost."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.39819) · [PDF](https://arxiv.org/pdf/2609.39819)

## 一句话摘要

Efficient serving of long-context reasoning-and-acting (ReAct) agents relies on KV cache reuse to reduce large language model (LLM) prefill latency and monetary cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient serving of long-context reasoning-and-acting (ReAct) agents relies on KV cache reuse to reduce large language model (LLM) prefill latency and monetary cost. However, a semantic gap exists between agent harnesses and the underlying serving stack. Through context mutation, tool execution, and subagent coordination, context messages may become actively engaged, permanently discarded, and temporarily unused, while the serving stack only observes accesses to the corresponding KV cache. This lifecycle blindness prevents recency-only policies such as LRU from reclaiming dead KV promptly and from preserving older KV that will be reused sooner than newer entries. We present KVTether, a lifecycle-aware KV cache management framework for ReAct agents. By tracing semantic primitives embedded in agent harnesses, KVTether captures runtime lifecycle semantics during highly dynamic execution. KVTether then translates message-level semantics into KV-level lifecycle states and uses these states to drive state-prioritized cache management without exposing physical complexities to agent harnesses. After reclaiming dead KV, KVTether preferentially preserves live-but-idle KV that is waiting for reuse, reducing premature eviction before reuse. Across agent benchmarks and production workloads, KVTether reduces end-to-end request latency by up to 26.3% and 17.4% relative to LMCache and MORI, respectively, and lowers estimated task cost by 40.0% and 33.2% on average.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaihua Fu, Yukun Zhou, Chaokun Chang, Yinghao Yu, Luping Wang, Guodong Yang, Jiuchen Shi, Quan Chen, Wei Wang
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
