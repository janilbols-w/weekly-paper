---
title: "TripleKV: Predict, Prefetch, Protect -- KV Cache Management for AI Agents"
description: "LLM agents alternate between inference and tool execution, repeatedly reusing their growing context across calls."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2611.25112v1) · [PDF](https://arxiv.org/pdf/2611.25112v1)

## 一句话摘要

LLM agents alternate between inference and tool execution, repeatedly reusing their growing context across calls.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents alternate between inference and tool execution, repeatedly reusing their growing context across calls. Under high concurrency, their combined key-value (KV) cache working set can reach hundreds of GiB, far exceeding GPU memory capacity. As idle KV cache blocks are evicted to slower storage tiers, returning agents incur expensive retrievals that stall inference. To address this problem, we present \emph{TripleKV}, a three-tier KV cache management system that hides the delays of these retrievals. %exploits tool execution to hide these delays. In agentic workloads, the KV blocks needed by the next inference request are known in advance; only the time of their reuse is uncertain. TripleKV uses a tool-aware latency predictor to estimate when each tool call will complete and prefetches the required KV blocks from SSD into host DRAM ahead of time. Unlike GPU prefetching, this avoids reserving scarce GPU memory and interfering with concurrent inference requests. To further improve DRAM utilization, TripleKV eliminates duplication of GPU-resident blocks in DRAM, and introduces a victim-cache mechanism that refills blocks from SSD upon their eviction from GPU memory. Across data, web, and coding agents, TripleKV reduces the fraction of requests requiring critical-path SSD reads from 45--76\% to under 10\%. It also reduces P95 time to first token (TTFT) by up to 49\% compared with vLLM extended with DRAM and SSD KV-cache tiers, and achieves 1.5-7$\times$ lower P95 TTFT than recent agent-aware systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shashwat Jaiswal, Chloe Alverti, Mengmei Ye, Chen Wang, Hubertus Franke, Fan Lai, Tianyin Xu, Josep Torrellas
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
