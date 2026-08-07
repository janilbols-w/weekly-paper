---
title: "Preserving Admission Responsibility in Multi-Tenant Large Language Model Prefix Caches"
description: "Shared prefix caching turns Graphics Processing Unit (GPU) memory into persistent state shared across Large Language Model (LLM) tenants."
---

**评分：39/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.01657) · [PDF](https://arxiv.org/pdf/2608.01657)

## 一句话摘要

Shared prefix caching turns Graphics Processing Unit (GPU) memory into persistent state shared across Large Language Model (LLM) tenants.

## 为什么值得关注

待编辑增强。

## 摘要原文

Shared prefix caching turns Graphics Processing Unit (GPU) memory into persistent state shared across Large Language Model (LLM) tenants. A group that materializes new Key-Value (KV) blocks can force another to lose reusable state, yet request-time schedulers account for transient service, replacement policies primarily rank object value, and static partitioning strands idle capacity. We call this mismatch the admission-responsibility gap. To close it, we propose PrefixShield, which meters newly materialized full KV blocks, carries responsibility across requests, gates reuse promotion while debt remains, and uses projected debt to select the group supplying eviction candidates. We implement PrefixShield in vLLM. In paired runs under one-touch pollution, PrefixShield improves victim cache hit ratio by 9.39 percentage points over the Least Recently Used (LRU) policy and 8.64 points over S3-FIFO, restoring the victim from 4.92% to 84.87% at 4096-block scale, and gains 2.00 points over S3-FIFO under two-pass replay. It preserves benign ShareGPT behavior and work-conserving access to idle capacity. Delayed replay yields a 35.16-point advantage while debt remains. These results show that object-value signals rank what to retain, while persistent responsibility determines which group bears reclamation pressure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiyu Wang, Rajkumar Buyya
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
