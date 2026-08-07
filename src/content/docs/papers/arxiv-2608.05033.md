---
title: "SparseDitto: Customizing GPU Kernels for Different Sparsity Patterns with LLM-Based Agentic System"
description: "Sparse matrix kernels are fundamental to scientific computing, graph analytics, and machine learning."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.05033) · [PDF](https://arxiv.org/pdf/2608.05033)

## 一句话摘要

Sparse matrix kernels are fundamental to scientific computing, graph analytics, and machine learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse matrix kernels are fundamental to scientific computing, graph analytics, and machine learning. Their GPU performance depends strongly on the input sparsity pattern and execution strategy. For the same SpMM on the same matrix, cuSPARSE exhibits a 350x performance gap between CSR and Blocked-ELL. Our study of multiple data formats, specialized systems, and sparse compilers shows that no single implementation consistently dominates across sparsity patterns and operators. This motivates a system that can adapt its representation, execution strategy, and hardware mapping to each workload and target GPU. We present SparseDitto, an LLM-based system that constructs a GPU kernel for each matrix, operator, and target GPU. SparseDitto supports SpMV, SpMM, and SpGEMM within a unified design framework. A lightweight additive model ranks established strategies using structural features of the input matrix. An architecture-aware planner then proposes several candidate designs. Coding and verification agents implement and refine them using measurements from the target GPU. Across three sparse operators and a diverse set of matrices, SparseDitto achieves a geometric-mean speedup of 2.68x over cuSPARSE on an NVIDIA RTX PRO 6000 GPU, with a maximum of 146.61x. On an NVIDIA H200 GPU, it achieves 2.79x, with a maximum of 78.5x. Its generated SpMM kernels also accelerate full-batch GCN training by up to 3.39x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shiyang Li, Guangyan Sun, Jinwei Tang, Yanzhi Wang, Mingyi Hong, Caiwen Ding
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
