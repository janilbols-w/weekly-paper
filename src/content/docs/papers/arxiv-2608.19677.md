---
title: "CacheRoute: Planned Prefix-Affinity Routing for Large-Scale LLM Serving"
description: "Prefix caching avoids prefill only when a repeated request returns to a server that still holds the prefix KV."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.19677) · [PDF](https://arxiv.org/pdf/2608.19677)

## 一句话摘要

Prefix caching avoids prefill only when a repeated request returns to a server that still holds the prefix KV.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefix caching avoids prefill only when a repeated request returns to a server that still holds the prefix KV. Cache-blind balancing disperses that reuse; fixed affinity preserves it but can overload a server. CacheRoute resolves this tradeoff with a periodic routing plan. It admits high-rate keys to a stable warm set and places their assignments by expected load. Hot keys may use more than one destination, although every key in our primary semi-synthetic aggregate uses exactly one. On Llama-3.3-70B in fp8 across 60 H100 GPUs, CacheRoute sustains 176+/-11 QPS at a 3.5-s p99 SLO, 2.3x the strongest of five baselines. Served KV-cache hit rate rises from 64.1+/-1.3% under cache-blind balancing to 93.2+/-0.5%. A second semi-synthetic aggregate and controlled 8B and burst experiments separate the effects of affinity and placement. Two 32B workloads provide the counterexamples: when affinity recovers too little KV work, its residual load skew reduces or erases the improvement. We therefore recommend gating any deployment with a shadow replay rather than enabling affinity from workload statistics alone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Huang Cheng
- 发布：2026-08-20；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
