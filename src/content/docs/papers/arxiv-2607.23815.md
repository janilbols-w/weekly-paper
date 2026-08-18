---
title: "Kalypso: Relational LLM Serving"
description: "Large language models are increasingly used as semantic operators for filtering, extracting, ranking, joining, and transforming unstructured data."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.23815) · [PDF](https://arxiv.org/pdf/2607.23815)

## 一句话摘要

Large language models are increasingly used as semantic operators for filtering, extracting, ranking, joining, and transforming unstructured data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly used as semantic operators for filtering, extracting, ranking, joining, and transforming unstructured data. Existing semantic query processing systems invoke request-centric LLM serving systems that are unaware of the query plan, leaving substantial performance opportunities unused. This paper introduces relational LLM serving, an abstraction that makes LLM serving aware of semantic query structure while preserving query semantics and output accuracy. The key opportunity is pipelined execution across semantic operators: when intermediate tuples flow directly from one operator to the next, their KV-cache state can be reused instead of recomputed. We present Kalypso, a relational LLM serving system that exposes an API for semantic query plans and executes them using an adaptive, memory-aware scheduling algorithm. Kalypso addresses a new online scheduling problem in which pipelined operator execution is coupled with GPU memory pressure management to reuse KV-cache state in the serving engine before eviction. Its scheduler continuously adjusts memory allocations to balance upstream parallelism, downstream progress, and GPU utilization. Our evaluation shows that Kalypso improves query completion time over baselines using request-centric LLM serving, with speedups up to 4.57x across diverse workloads, demonstrating that query-aware LLM serving can substantially improve the efficiency of semantic query execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Hojae Son, Md Ashraful Islam, Huy Gia Cao, Hui Guan, Marco Serafini
- 发布：2026-08-17；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
