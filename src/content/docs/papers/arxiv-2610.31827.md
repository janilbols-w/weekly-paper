---
title: "KVStream: Adaptive Parallel Storage Management for KV Caching in Large-Scale LLM Serving"
description: "Long-context LLM serving for agentic, coding, and document workloads reuses prefixes whose key-value (KV) cache outgrows GPU and host memory, putting storage I/O on the critical path of the inference step for retrieving prefixes."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.31827) · [PDF](https://arxiv.org/pdf/2610.31827)

## 一句话摘要

Long-context LLM serving for agentic, coding, and document workloads reuses prefixes whose key-value (KV) cache outgrows GPU and host memory, putting storage I/O on the critical path of the inference step for retrieving prefixes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM serving for agentic, coding, and document workloads reuses prefixes whose key-value (KV) cache outgrows GPU and host memory, putting storage I/O on the critical path of the inference step for retrieving prefixes. A single node-local NVMe absorbs all retrievals, while the parallel file system or cloud file store that nodes already mount carries almost no inference traffic. We cast prefix retrieval as aggregate-bandwidth scheduling across these tiers and present KVStream, a KV cache engine that batches a step's reads, defers writes behind the forward pass, replicates each chunk on every tier, and lets each tier adaptively claim the next unread chunks once it is free. Our performance model shows this routing attains the aggregate-bandwidth bound without prediction or tuning, whereas any static split misses it by a margin that grows as per-tier bandwidths drift or fluctuate. It also predicts that the time-to-first-token (TTFT) gain grows with load, as faster retrieval drains the queue, and disappears when host memory or arrival order keeps reuse in cache. Plugged into LMCache and evaluated on four models, six datasets, and up to 128 GPUs, KVStream retrieves within 5% of the bound, delivers up to 1.49$\times$ higher offline throughput than LMCache, and lowers mean TTFT by up to 6.1$\times$ under bursty arrivals.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Avinash Maurya, Jaiaid Mobin, Jie Ye, M. Mustafa Rafique, Franck Cappello, Bogdan Nicolae
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
