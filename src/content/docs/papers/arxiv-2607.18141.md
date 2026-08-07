---
title: "A CXL Memory Rack for Multi-Turn LLM Serving"
description: "Long-context, multi-turn, and agentic LLM workloads increasingly reuse previously processed context, making KV-cache reuse essential for reducing redundant computation."
---

**评分：49/100** · AI 基础设施 > 集群与资源系统 > 资源解耦

[论文原文](https://arxiv.org/abs/2607.18141) · [PDF](https://arxiv.org/pdf/2607.18141)

## 一句话摘要

Long-context, multi-turn, and agentic LLM workloads increasingly reuse previously processed context, making KV-cache reuse essential for reducing redundant computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context, multi-turn, and agentic LLM workloads increasingly reuse previously processed context, making KV-cache reuse essential for reducing redundant computation. However, this reuse shifts the bottleneck to the memory tier that stores and serves reusable KV states at cluster scale. GPU HBM and host DRAM are too costly to scale to TB-scale shared context capacity, motivating remote tiers built from lower-cost, higher-capacity media. This paper presents HyMCache, a CXL memory rack for multi-turn LLM serving. We build the memory rack using cost-efficient CXL-hybrid memory (CXL-HM), which combines a small amount of in-device DRAM with large SSD-backed capacity behind a CXL interface. By exploiting the read-dominant, predictable, and append-only nature of multi-turn KV-cache access, HyMCache rethinks DRAM management within CXL-HM to efficiently support TB-scale SSD-backed KV reuse. It uses request-level prefix prefetching and opportunistic write buffering to stage latency-critical reads in device DRAM, enabling DRAM-scale KV-cache efficiency at SSD-level cost. We evaluate HyMCache on a real CXL-HM prototype under both single-aggregator and PD-disaggregated serving configurations. Under the same DRAM budget, HyMCache outperforms local LMCache by 3.0x in single-node serving and 1.45x in PD-disaggregated serving. Compared with 1 TB distributed-DRAM Mooncake, HyMCache incurs about 30% lower performance but uses 16x less DRAM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cxl memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hakbeom Jang, Inho Song, Hoshik Kim, Sam H. Noh, Jongryool Kim
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
