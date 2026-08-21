---
title: "DB-SpMSpV: Dual-View Blocked Sparse Matrix-Sparse Vector Multiplication for Dynamic GPU Workloads"
description: "Sparse Matrix-Sparse Vector Multiplication (SpMSpV) is a core primitive in graph traversal, sparse linear algebra, and sparse model inference."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.16308) · [PDF](https://arxiv.org/pdf/2608.16308)

## 一句话摘要

Sparse Matrix-Sparse Vector Multiplication (SpMSpV) is a core primitive in graph traversal, sparse linear algebra, and sparse model inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse Matrix-Sparse Vector Multiplication (SpMSpV) is a core primitive in graph traversal, sparse linear algebra, and sparse model inference. Its input vector is often dynamically sparse, so the best GPU execution path depends on both global sparsity and the local vector-block distribution. Existing GPU SpMSpV methods often bind storage layouts, push/pull traversal, and kernels together, making fine-grained adaptation difficult without extra storage or scheduling overhead. This paper presents DB-SpMSpV, a dual-view blocked SpMSpV framework for dynamic GPU workloads. DB-SpMSpV partitions the matrix into fixed-size 2D blocks, maintains block-level CSR/CSC views at the high level, and reuses a single low-level block payload to support both row-driven pull and column-driven push. At runtime, it selects the global traversal path based on input block sparsity, chooses block microkernels from the local matrix/vector block structure, and uses load balancing, asynchronous prefetching, and hierarchical writeback to reduce irregular memory accesses, writeback conflicts, and load imbalance. We further integrate the framework into DB-BFS and DB-Decoding. We evaluate DB-SpMSpV on NVIDIA A100 and RTX 4090 using SuiteSparse matrices, symmetric graphs, and three open-source LLMs. Across input sparsities, DB-SpMSpV achieves average speedups of 5.48$\times$--64.34$\times$ over cuSPARSE and 2.36$\times$--14.01$\times$ over TileSpMSpV on A100, with similar gains on RTX 4090. DB-BFS further improves end-to-end graph traversal by 2.66$\times$ over TileBFS on A100 and 3.60$\times$ on RTX 4090 on average, while DB-Decoding accelerates single-token linear layers by up to 4.50$\times$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xing Cong, Chenhao Xie, Rui Wang, Zhongzhi Luan, Yi Liu, Depei Qian
- 发布：2026-08-17；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
