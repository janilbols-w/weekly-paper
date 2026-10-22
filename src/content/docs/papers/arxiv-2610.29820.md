---
title: "UlaCache: Unified Logical Addressing for Sparse LLM Serving"
description: "Long contexts increase the memory cost of the key-value (KV) cache in large language model (LLM) inference."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.29820) · [PDF](https://arxiv.org/pdf/2610.29820)

## 一句话摘要

Long contexts increase the memory cost of the key-value (KV) cache in large language model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long contexts increase the memory cost of the key-value (KV) cache in large language model (LLM) inference. Sparse attention reduces attention computation and memory traffic by selecting historical tokens, but the retained KV cache must remain available for later decoding steps. We present UlaCache, a KV cache management system built around a unified logical address space spanning GPU KV pools and optional CPU memory. Stable logical references let the inference engine allocate and select KV independently of physical placement. Common allocation and sparse-access interfaces support data-parallel (DP) and tensor-parallel (TP) attention. For distributed storage, local GPU buffers retain selected KV across decoding steps, so only missing entries require transfers. When CPU storage is enabled, Parallel Bucketed LRU (PB-LRU) manages a GPU pool shared across requests. It updates recency metadata and selects eviction victims in parallel. UlaCache transfers KV and then updates the address mappings. With speculative decoding enabled under matched CPU and GPU memory budgets, UlaCache achieves peak decoding throughput speedups of 1.16 $\times$ (DP) and 1.70 $\times$ (TP) on H200, and 1.73 $\times$ (DP) and 2.51 $\times$ (TP) on B300, compared with the state-of-the-art baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine, llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Isaac Zhu, Alan Cao, Hugh Yin, Rocky Wang, Orion Wang, Hscos Zhang, Jack Li, Jason Zhao
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
