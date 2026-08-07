---
title: "Efficiency and Cost Alignment in Batched LLM Serving via Resource-Fair Scheduling"
description: "This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.02244) · [PDF](https://arxiv.org/pdf/2608.02244)

## 一句话摘要

This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another.

## 为什么值得关注

待编辑增强。

## 摘要原文

This paper studies a resource-allocation inefficiency in batched large language model (LLM) serving: heterogeneous requests that share a decode batch impose max-driven computational costs on one another. Because the wall-clock cost of a batch step is largely governed by the largest active KV-cache footprint, a short request co-batched with a long request can experience latency and GPU-resource consumption disproportionate to its own token workload. We formalize this phenomenon as a resource-fair scheduling problem. We develop a mathematical scheduling model that connects within-batch resource fairness to system throughput. The proposed fairness constraint bounds the disparity in decode progress, equivalently KV-cache footprint, among co-batched requests. Based on this model, we design the Insert-Short-Jobs-with-Limit (ISJL) algorithm, a parameterized hybrid batching policy. We prove that ISJL achieves a global competitive-ratio lower bound of $3/4$. We further examine the profit implications of resource-fair scheduling under the token-metered pricing convention used by commercial LLM APIs. Numerical experiments show that ISJL occupies a favorable middle ground between FCFS, which has large batching externalities, and LJF, which is cost-aligned but sacrifices batching flexibility. Thus, ISJL provides a bi-criterion scheduling policy: it maintains high throughput while aligning max-driven batch cost with token-metered revenue.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dayi Yao, Zijie Zhou
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
