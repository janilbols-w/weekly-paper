---
title: "PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving"
description: "Repeated prompt prefixes are increasingly common in LLM serving workloads, appearing in system prompts, templated retrieval-augmented generation pipelines, agent frameworks, and multi-turn conversations."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.19657) · [PDF](https://arxiv.org/pdf/2609.19657)

## 一句话摘要

Repeated prompt prefixes are increasingly common in LLM serving workloads, appearing in system prompts, templated retrieval-augmented generation pipelines, agent frameworks, and multi-turn conversations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Repeated prompt prefixes are increasingly common in LLM serving workloads, appearing in system prompts, templated retrieval-augmented generation pipelines, agent frameworks, and multi-turn conversations. Modern inference runtimes such as vLLM and TensorRT-LLM provide mechanisms for reusing previously computed KV-cache state across requests, yet it remains unclear when prefix reuse materially improves serving performance on contemporary accelerators and when its benefits are limited by scheduling, cache granularity, concurrency, or memory pressure. This paper presents PrefixBench-H100, a reproducible benchmark and measurement framework for characterizing prefix reuse on a single NVIDIA H100. PrefixBench-H100 combines controlled synthetic traces with chat-style and retrieval-style workloads, and evaluates two widely used LLM serving runtimes under matched workload conditions. The benchmark varies shared-prefix length, suffix diversity, request arrival pattern, concurrency, output length, and cache configuration, while collecting time-to-first-token, inter-token latency, end-to-end latency, throughput, cache-hit statistics, GPU memory usage, and selected profiling traces. The goal of PrefixBench-H100 is not to introduce a new caching algorithm, but to expose the practical operating envelope of prefix reuse for H100-class LLM serving. The study identifies the regime where prefix reuse provides substantial first-token latency reductions and the regime where cache pressure erodes them, while showing that cache effectiveness itself is largely insensitive to concurrency and output length; the cross-runtime differences that remain arise above the cache, in the scheduling layer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav
- 发布：2026-09-17；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
