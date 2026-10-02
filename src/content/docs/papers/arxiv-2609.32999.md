---
title: "Tessera: Demand-Driven KV Cache Management for Retrieval-Augmented LLM Serving"
description: "RAG and retrieval-based agent memory both inject retrieved content into LLM prompts, as document chunks and recalled memory records, respectively."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2609.32999v1) · [PDF](https://arxiv.org/pdf/2609.32999v1)

## 一句话摘要

RAG and retrieval-based agent memory both inject retrieved content into LLM prompts, as document chunks and recalled memory records, respectively.

## 为什么值得关注

待编辑增强。

## 摘要原文

RAG and retrieval-based agent memory both inject retrieved content into LLM prompts, as document chunks and recalled memory records, respectively. The same content can recur across requests at different prompt positions or after different preceding contexts, preventing reuse through conventional prefix caching. Our characterization finds that records recurring outside the matching prefix account for over 70% of injected memory tokens in agent-memory workloads. Composable KV-reuse methods enable reuse in such cases, but online serving introduces a management problem: a recurring unit's KV states may not yet exist, may have been evicted, or may reside on another node. We present Tessera, a disaggregated serving system that makes retrieval the control plane for KV reuse. By exposing the context units needed before model execution, retrieval allows Tessera to combine current demand with retrieval history, KV residency, and generation load to coordinate cache management and request routing. Generation nodes concurrently prepare locally cached, remotely cached, and missing states, while retaining newly computed states off the request's critical path. Across RAG and agent-memory workloads, Tessera lowers mean TTFT by up to 3.6x over SGLang and LMCache with EPIC at matched request rates, and sustains low TTFT at rates where the baselines saturate, while matching the answer quality of the underlying composition policy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Fei Fang, Chung-Hsiang Lo, Yi Liu, Yifan Hua, Chen Qian
- 发布：2026-09-26；更新：2026-09-26
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
