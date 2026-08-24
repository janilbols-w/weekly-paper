---
title: "TokenCake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications"
description: "Large Language Models (LLMs) are increasingly deployed in complex multi-agent applications that rely on external function calls."
---

**评分：50/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2510.18586) · [PDF](https://arxiv.org/pdf/2510.18586)

## 一句话摘要

Large Language Models (LLMs) are increasingly deployed in complex multi-agent applications that rely on external function calls.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are increasingly deployed in complex multi-agent applications that rely on external function calls. This workload creates severe performance challenges for the KV Cache: spatial contention leads to the eviction of critical agents' caches and temporal underutilization leaves the cache of agents stalled on long-running function calls idling in GPU memory. We present TokenCake, a KV-Cache-centric serving framework that bridges this gap by co-optimizing scheduling and memory management through an agent-aware design. TokenCake's Temporal Scheduler employs an event-driven, opportunistic policy to proactively offload idle KV Caches during function calls and uses predictive uploading to hide data transfer latency. TokenCake's Spatial Scheduler uses dynamic memory partitioning, guided by a hybrid priority metric combining graph structure and runtime state, to reserve GPU memory for critical-path agents. Our evaluation on representative multi-agent benchmarks shows that TokenCake reduces end-to-end latency by over 47.06% and improves effective GPU memory utilization by up to 16.9% compared to vLLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhuohang Bian, Feiyang Wu, Zhuoran Li, Teng Ma, Youwei Zhuo
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
