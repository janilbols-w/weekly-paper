---
title: "HBFlex: A Flexible Memory System for Bridging Fine-Grained LLM States and Coarse-Grained HBF Parallel Execution"
description: "Large language models (LLMs) require increasing memory capacity to accommodate growing model weights and KV caches."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.18675) · [PDF](https://arxiv.org/pdf/2609.18675)

## 一句话摘要

Large language models (LLMs) require increasing memory capacity to accommodate growing model weights and KV caches.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) require increasing memory capacity to accommodate growing model weights and KV caches. High-Bandwidth Flash (HBF) offers high memory density and aggregate read bandwidth through massive plane-level parallelism, making it an attractive option for LLM serving. However, serving LLMs entirely from HBF introduces three challenges: fine-grained KV reads create placement and access imbalance, incremental writes interfere with foreground reads, and mixed KV lifetimes amplify garbage collection. Hybrid HBM/HBF designs retain HBM to support dynamic KV management, but this allocation reduces the HBF resources available under a fixed packaging budget, limiting aggregate HBF bandwidth. We present HBFlex, a full-HBF memory system with coordinated optimizations for KV reads, writes, and reclamation. HBFlex balances KV placement and attention accesses to improve plane utilization. It aggregates incremental updates and schedules writeback within sufficiently long compute windows to reduce write--read interference. It also combines lifetime-guided block packing with deferred reclamation to reduce valid-page migration. We evaluate HBFlex through trace-driven simulation across different configurations. HBFlex achieves average throughput speedups of up to 1.58$\times$ over FlashAccel and 3.30$\times$ over H3, benefiting from higher HBF bandwidth and more efficient management of dynamic KV-cache reads, writes, and erases.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuzhang Zhong, Weikai Xu, Yifan Zhou, Tongbin Zhao, Tenghao Zhao, Yifei Kang, Cunyin Chang, Shu Li, Guangyu Sun, Meng Li
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
