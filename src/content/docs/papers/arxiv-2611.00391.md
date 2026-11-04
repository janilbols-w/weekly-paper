---
title: "Rethinking KV Cache Eviction for Agentic LLM Serving"
description: "Key-value (KV) caches impose substantial memory pressure on large language model serving systems, requiring cache eviction when capacity is insufficient."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.00391) · [PDF](https://arxiv.org/pdf/2611.00391)

## 一句话摘要

Key-value (KV) caches impose substantial memory pressure on large language model serving systems, requiring cache eviction when capacity is insufficient.

## 为什么值得关注

待编辑增强。

## 摘要原文

Key-value (KV) caches impose substantial memory pressure on large language model serving systems, requiring cache eviction when capacity is insufficient. Existing mechanisms typically evict KV from the ends of cached sequences to preserve prefix sharing across requests. However, agent workloads repeatedly reuse long histories across successive turns. Recomputing the KV cache for tokens near the end of a sequence is substantially more expensive than for earlier tokens because their attention computation involves longer histories. To address this problem, we propose preserving shared prefixes and evicting the KV cache from the beginning of the remaining history while retaining the cached suffix. We build Penelope around this strategy by co-designing the eviction policy, KV recomputation, and unified GPU-CPU cache management. Returning requests reuse the KV cache retained in GPU or CPU memory and recompute only missing segments while preserving reuse of the cached suffix. We implement Penelope in SGLang and evaluate it on three Qwen3 model sizes using real agent traces. Compared with SGLang, Penelope reduces mean time to first token by up to 60% and job completion time by up to 37% with a GPU-only cache, and by up to 76% and 60% with a two-tier GPU-CPU cache.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiakun Fan, Han Meng, Yuxuan Xia, Hao Mark Chen, Dong Li, Dimitrios S. Nikolopoulos
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
