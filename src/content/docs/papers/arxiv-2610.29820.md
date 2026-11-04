---
title: "UlaCache: Unified Logical Addressing for Sparse LLM Serving"
description: "Long-context inference in large language models (LLMs) imposes substantial memory requirements for the key-value (KV) cache."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820)

## 一句话摘要

Long-context inference in large language models (LLMs) imposes substantial memory requirements for the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context inference in large language models (LLMs) imposes substantial memory requirements for the key-value (KV) cache. Token-selective sparse attention reduces attention computation and memory traffic, but KV entries must still be retained for future queries. KV storage capacity therefore remains a constraint on decoding concurrency. Combining GPU and CPU memory expands this capacity but requires efficient access across heterogeneous memory pools. We present UlaCache, a KV cache management system that provides unified logical addressing across GPU and CPU memory. Its logical-slot interface enables the inference engine to allocate, write, access, and release KV entries using stable identifiers across attention parallelism modes. UlaCache manages physical placement, residency, and transfers, updating address mappings after KV transfers. Parallel Bucketed LRU (PB-LRU) reduces the overhead of KV replacement by parallelizing recency updates and eviction-candidate selection within a GPU memory pool shared across requests. We evaluate UlaCache against state-of-the-art baselines. Under tensor-parallel attention (TP), UlaCache provides up to $11.4\times$ the usable KV cache capacity of HiSparse. For GLM-5.3 on eight H200 GPUs, UlaCache achieves peak decoding throughput of $1.10\times$ and $1.59\times$ that of HiSparse under data-parallel attention (DPA) and TP, respectively. For HY4 Preview on eight B300 GPUs, the corresponding throughput ratios are $1.27\times$ and $1.93\times$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine, llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Isaac Zhu, Alan Cao, Hugh Yin, Rocky Wang, Orion Wang, Hscos Zhang, Jack Li, Jason Zhao
- 发布：2026-10-22；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
