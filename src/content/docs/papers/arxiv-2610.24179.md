---
title: "KVCompass: A Discovery Plane for Internet-Scale Prefix Cache Sharing in LLM Serving"
description: "KV cache reuse is one of the most effective ways to reduce LLM inference cost, but today its benefits are largely confined to a single cluster."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.24179) · [PDF](https://arxiv.org/pdf/2610.24179)

## 一句话摘要

KV cache reuse is one of the most effective ways to reduce LLM inference cost, but today its benefits are largely confined to a single cluster.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache reuse is one of the most effective ways to reduce LLM inference cost, but today its benefits are largely confined to a single cluster. When a provider serves the same model across geographically distributed regions, each region may repeatedly prefill the same popular prefixes, wasting GPU time and increasing time-to-first-token (TTFT). Exploiting reuse across regions involves discovering which worker currently holds a reusable KV cache for each request's prefix. We show that this KV cache discovery problem is structurally harder than conventional object lookup. Unlike hash-placement mechanisms such as DHTs, where an object's location is a deterministic function of its key, KV caches are created on the workers that serve requests, and their holder sets change with subsequent requests and KV cache evictions. KV cache discovery therefore calls for decoupling KV cache identity from placement. We present KVCompass, a discovery plane for Internet-scale KV cache sharing. The discovery index supports variable-length prefix lookup with constant-time local table reads at the edge, allowing each request to be forwarded to the worker that best balances KV cache reuse against load and network distance. Evaluation includes a 64-worker geo-distributed simulation and a 14-worker three-continent real-machine testbed. Evaluation shows that KVCompass achieves $1.3-14\times$ lower P99 TTFT than the baselines, up to $3.7\times$ lower P99 end-to-end latency, up to $4.7\times$ the throughput, and a peak load factor within 2% of the Oracle floor.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shiyi Ling, Fei Fang, Chen Qian
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
