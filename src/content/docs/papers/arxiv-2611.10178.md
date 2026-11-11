---
title: "The Storage View Of KV Cache: Characterizing Cache Behavior Across LLM Workloads"
description: "Modern LLM serving increasingly extends KV caches beyond GPU memory into host DRAM, SSDs, and remote storage, yet these stores remain largely governed by workload-agnostic policies such as LRU and fixed TTLs."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.10178) · [PDF](https://arxiv.org/pdf/2611.10178)

## 一句话摘要

Modern LLM serving increasingly extends KV caches beyond GPU memory into host DRAM, SSDs, and remote storage, yet these stores remain largely governed by workload-agnostic policies such as LRU and fixed TTLs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLM serving increasingly extends KV caches beyond GPU memory into host DRAM, SSDs, and remote storage, yet these stores remain largely governed by workload-agnostic policies such as LRU and fixed TTLs. We ask what execution context is needed by storage to make retention, reclamation, and placement decisions across heterogeneous workloads. We characterize KV-cache reuse, lifetime, and footprint at block granularity across 11 production and public traces spanning chat, API serving, RAG, coding agents, tool-using agents, and multi-lineage workflows. We examine reuse sources, recurrence timing and frequency, useful lifetimes, and storage consumption. Across workloads, KV state takes two recurring forms. Single-session state is reused within one execution: its footprint grows as sessions deepen and accumulates across concurrent sessions; it can remain useful through long idle periods but loses value at session completion. Multi-session state recurs across sessions of the same workload, outlives individual sessions, and spans hot prefixes and a large infrequent tail. While prior systems often exploit application-, agent-, or workflow-specific knowledge, our results suggest that three generic signals (a workload identifier, a session identifier, and session completion) expose much of the structure needed for KV-storage management. Trace-driven comparisons show that workload-specific recurrence estimates retain up to 22% more within-session hits and reduce dead state by up to 40%; a session completion signal eliminates the fundamental idle-time reclamation tradeoff for single-session state; and session-aware reuse classification identifies shared state 4-700x more selectively than request-level access counts. These results motivate a small cross-layer interface for workload-aware KV storage without application-specific semantics.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Talia Q. Chen, Daniel Waddington, Narangerelt Batsoyol, Vijay Chidambaram
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
