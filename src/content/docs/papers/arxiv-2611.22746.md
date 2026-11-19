---
title: "LaFlash: Capacity-Driven Acceleration for Coding Agent Workflows via QLC-HBF"
description: "As large language models (LLMs) evolve toward agentic AI, coding agents are emerging as memory-intensive workloads that repeatedly reuse persistent states, including contexts and KV caches."
---

**评分：47/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.22746) · [PDF](https://arxiv.org/pdf/2611.22746)

## 一句话摘要

As large language models (LLMs) evolve toward agentic AI, coding agents are emerging as memory-intensive workloads that repeatedly reuse persistent states, including contexts and KV caches.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) evolve toward agentic AI, coding agents are emerging as memory-intensive workloads that repeatedly reuse persistent states, including contexts and KV caches. Emerging agentic workflows, including Loop/Graph Engineering, cause state amplification through frequent active/dormant transitions, increasing memory pressure. Evicted states incur costly recomputation upon reactivation, particularly under long-context, short-decode workloads. This motivates Capacity-Driven Acceleration (CDA), which explicitly accounts for state amplification to allocate memory capacity between active concurrency and dormant-state retention, replacing recomputation with memory access. In this work, we propose LaFlash, a High-Bandwidth Flash (HBF) architecture that exploits the large capacity of Quad-Level Cell (QLC)-based flash to realize CDA. However, QLC's long read latency demands massive read parallelism under irregular state reactivation and varying context lengths, while limited write endurance constrains placement. LaFlash introduces Session Grouping to balance active request counts and aggregate context lengths across groups, sustaining read parallelism and block utilization through request-exclusive allocation. Furthermore, Fast-Page Allocation exploits QLC's read-latency heterogeneity to mitigate residual inter-group imbalance and sustain bandwidth utilization. On end-to-end coding agent workloads, LaFlash achieves 7.04$\times$ higher throughput and 10.96$\times$ higher energy efficiency over SLC-HBF with batch expansion, and 2.36$\times$ higher throughput over QLC-HBF with CDA. HBM buffering further reduces unnecessary NAND writes, improving QLC write endurance. These results demonstrate the benefits of jointly optimizing state retention and physical data placement for capacity-driven acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 17 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuseon Choi, Eunjong Lee, Sanghyeon Park, Seongyon Hong, Sangjin Kim, Thierry Tambe
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
