---
title: "Nebula: Distributed Position-Independent Caching for LLM Serving"
description: "Modern LLM workflows, such as retrieval-augmented generation (RAG) and LLM agents, build long prompts from multiple independent text segments, making prefill a major source of computation."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.09474) · [PDF](https://arxiv.org/pdf/2611.09474)

## 一句话摘要

Modern LLM workflows, such as retrieval-augmented generation (RAG) and LLM agents, build long prompts from multiple independent text segments, making prefill a major source of computation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern LLM workflows, such as retrieval-augmented generation (RAG) and LLM agents, build long prompts from multiple independent text segments, making prefill a major source of computation. Reusing KV caches is therefore important for reducing serving costs and latency: distributed caching systems spread KV cache across a cluster to increase aggregate capacity, while position-independent caching (PIC) enables reuse of recurring segments under different prefixes. However, existing systems distribute KV caches but still rely on prefix caching (PC), while existing PIC methods enable position-independent reuse without cluster-wide resource management. We present Nebula, the first distributed LLM serving framework to treat PIC segments as first-class citizens, enabling remote PIC reuse and parallel prefill. To track PIC's fine-grained, asynchronous state changes, Nebula combines optimistic accounting with event-driven updates to provide a timely and truthful cluster view for cache management and prefill scheduling. To accommodate diverse reuse patterns across workloads, Nebula leverages cluster-wide ghost-hit feedback to automatically tune the allocation of shared cache capacity between PC and PIC. Finally, Nebula incorporates queueing, computation, and KV transfer costs into a unified prefill completion time model to guide elastic parallelism adjustment and locality-aware compute placement. Across four models and four real-world RAG and agentic workloads, Nebula reduces median TTFT by an average of 61.4% compared with the strongest existing baseline and recovers an average of 76.1% of the tokens missed by prefix caching.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yifei Liu, Junbin Pan, Junhao Hu, Yang Liu, Junyi Chen, Juntong Wu, Chen Chen, Haiyuan Zhao, Xiaoxu Chen, Weihang Chen
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
