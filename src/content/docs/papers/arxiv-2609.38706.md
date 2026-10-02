---
title: "Preserving Provenance in Shared KV Caches for LLM Serving"
description: "Production LLM serving stacks combine an inference engine's local prefix cache with a shared KV-cache tier for fleet-wide reuse."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.38706) · [PDF](https://arxiv.org/pdf/2609.38706)

## 一句话摘要

Production LLM serving stacks combine an inference engine's local prefix cache with a shared KV-cache tier for fleet-wide reuse.

## 为什么值得关注

待编辑增强。

## 摘要原文

Production LLM serving stacks combine an inference engine's local prefix cache with a shared KV-cache tier for fleet-wide reuse. The local cache distinguishes requests by adapter, weight configuration and sharing domain, but the shared tier may key entries only by token content and coarse model metadata. This boundary erases provenance and lets identical tokens under incompatible computational or sharing contexts collide. We call this composition gap provenance-blind reuse and present its first systematic study. A source audit of three vLLM connectors confirms the structural omission, while runtime experiments reproduce it across vLLM and two SGLang releases, 12 models from 7 families (0.5 B-32 B), and over 160 configurations. Cross-adapter collisions reduce accuracy from 0.94 to 0.64, incompatible KV representations reduce reasoning accuracy to zero, and salt omission enables 93% prompt identification from timing. We formalize the missing guarantee as the KV provenance contract: for a declared dimension registry, shared keys must be injective over computational and sharing provenance, with identities stable across workers. Any dimension with a stable identity can therefore be added without connector-specific key logic. A canonical descriptor binds per-request and per-worker provenance into lookup and store keys, while a differential checker detects dimensions that change KV state without changing the key. Implemented in vLLM and SGLang 0.5.20 across three cache paths, provenance binding eliminates unsafe reuse while preserving legitimate sharing. Hit-path latency changes remain within 0.34 ms and below run-to-run variation; retention grows with provenance diversity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine, llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wei Song, Yuxin Cao, Xi Zheng, Leo Zhang, Xiao Cheng
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
