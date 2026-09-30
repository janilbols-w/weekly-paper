---
title: "TempoKV: Timely Staging of LLM KV Caches for Memory-Semantic Flash"
description: "Reusable prefix key-value (KV) caches can outgrow GPU memory in large language model (LLM) serving."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2609.35065) · [PDF](https://arxiv.org/pdf/2609.35065)

## 一句话摘要

Reusable prefix key-value (KV) caches can outgrow GPU memory in large language model (LLM) serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reusable prefix key-value (KV) caches can outgrow GPU memory in large language model (LLM) serving. A memory-semantic flash hierarchy offers SSD-backed capacity with a limited fast tier, but a logical KV hit is not necessarily ready for GPU retrieval. Demand staging exposes SSD latency, whereas immediate staging can reserve fast-tier capacity long before retrieval begins. We present TempoKV, a timing-aware resource-commitment layer that separates early knowledge of reuse from the acquisition of staging resources. It records reusable-KV hits as metadata-only claims and requests commitment when the runtime-estimated time until retrieval falls to the storage-estimated time needed to make KV resident and protected against eviction. These estimates adapt to runtime progress and staging state, while commitment remains subject to available protected capacity. We implement TempoKV in vLLM and LMCache on an SSD-backed CXL memory device without changing request scheduling. Across two models and three prefix cache ratios, TempoKV reduces protected fast-tier byte-time per request by 63-91% versus immediate staging while retaining much of the serving benefit of advance staging. In a fast-tier capacity sweep, output throughput and p95 time to first token (TTFT) remain nearly unchanged as capacity decreases from 100 to 25 GiB. Compared with unmodified LMCache's Device-DAX L1 configuration, TempoKV reduces p95 TTFT by up to 48.0% and increases output throughput by up to 27.8%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: request scheduling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jay H. Park, Hyungjun Kim, Dong Kim
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
