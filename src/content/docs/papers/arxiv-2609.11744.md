---
title: "Building py-kvcache: A Performance Characterization of External KV Caching for vLLM with NVMe SSDs"
description: "Prefix caching can reduce the time to first token (TTFT) of long-context LLM requests by reusing previously computed key-value (KV) states, but for short prefixes or fast GPUs, recomputation can be faster than loading from an external cache."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.11744) · [PDF](https://arxiv.org/pdf/2609.11744)

## 一句话摘要

Prefix caching can reduce the time to first token (TTFT) of long-context LLM requests by reusing previously computed key-value (KV) states, but for short prefixes or fast GPUs, recomputation can be faster than loading from an external cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefix caching can reduce the time to first token (TTFT) of long-context LLM requests by reusing previously computed key-value (KV) states, but for short prefixes or fast GPUs, recomputation can be faster than loading from an external cache. We characterize this tradeoff in vLLM across GPU, CPU, and NVMe tiers using synthetic workloads, long-context benchmarks, production traces, and find that cache performance depends on transfer granularity, intermediate memory use, and when transfers enter the request schedule, not only on device bandwidth. These findings motivate py-kvcache, a vLLM KV Offload connector with asynchronous direct I/O, bounded shared staging, and scheduler-aware preloading, which starts disk reads while requests are still waiting, overlapping with compute. At 80k tokens, py-kvcache loading from disk is 2.0x faster than LMCache, with preloading contributing 1.34x. With GPU, CPU, and disk caching enabled, it is 1.23x faster than LMCache and within approximately 4% of the native vLLM KV Offload implementation. LongBench and SCBench show that these benefits extend to irregular prefix chains and multi-turn workloads. Bailian trace replays improve TTFT on a weaker GPU, but on an H100 the average request falls below the break-even point and GPU memory alone retains enough prefixes. External KV caching should therefore be treated as a setup specific admission decision. The py-kvcacheimplementation is available at: https://github.com/atlarge-research/py-kvcache.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Joseph Kanichai, Tiziano De Matteis, Animesh Trivedi
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/atlarge-research/py-kvcache](https://github.com/atlarge-research/py-kvcache)
- 阅读深度：metadata
