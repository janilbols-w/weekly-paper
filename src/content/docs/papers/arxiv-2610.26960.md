---
title: "VS-Flash: Harnessing Vector Search with Computational Memory-Semantic Flash"
description: "As generative AI continues to evolve, retrieval-augmented generation (RAG) systems are driving rapid growth in vector database capacity requirements."
---

**评分：45/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.26960) · [PDF](https://arxiv.org/pdf/2610.26960)

## 一句话摘要

As generative AI continues to evolve, retrieval-augmented generation (RAG) systems are driving rapid growth in vector database capacity requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

As generative AI continues to evolve, retrieval-augmented generation (RAG) systems are driving rapid growth in vector database capacity requirements. As datasets outgrow host DRAM, vector databases rely on MMap-based serving over SSDs to extend capacity. However, high-fan-out ANN searches generate concurrent irregular accesses that contend for host memory and storage resources, degrading bulk throughput and inflating tail latency under mixed workloads. In this paper, we address these challenges through memory-semantic capacity and workload-aware compute placement. VS-Flash exposes flash as a large-capacity memory-semantic space and dynamically selects the execution engine according to runtime query and workload characteristics. It offloads throughput-oriented large-batch queries to a Computational Memory-Semantic Flash (CMS-Flash) device, while executing latency-sensitive small-batch queries on the host CPU. Both paths access the same resident segments, avoiding a separate host-DRAM replica. Across three billion-scale datasets, VS-Flash improves bulk-search throughput over vanilla Milvus by 36.8X on average, with up to a 57.4X improvement. Under mixed workloads, VS-Flash reduces the p99 latency of latency-sensitive requests by up to 24.8X while sustaining device-side bulk search. These results show that VS-Flash delivers scalable vector search beyond host DRAM capacity while jointly improving bulk throughput and small-request tail latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: tail latency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Donguk Kim, Sangjun Pae, Daeyoung Lee, Dong Kim
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
