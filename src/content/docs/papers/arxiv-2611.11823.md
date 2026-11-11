---
title: "AscSpMM: Efficient SpMM on Ascend NPUs via Pipelined Vector-Cube Collaboration"
description: "Neural processing units (NPUs) provide high compute density and energy efficiency through specialized matrix engines and software-managed on-chip memory."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.11823) · [PDF](https://arxiv.org/pdf/2611.11823)

## 一句话摘要

Neural processing units (NPUs) provide high compute density and energy efficiency through specialized matrix engines and software-managed on-chip memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Neural processing units (NPUs) provide high compute density and energy efficiency through specialized matrix engines and software-managed on-chip memory. However, their libraries primarily target dense computation. Sparse matrix-dense matrix multiplication (SpMM), a key kernel in graph analytics, sparse neural networks, and scientific computing, requires index-driven operand selection, indirect addressing, scattered memory accesses, and load balancing. These requirements conflict with the fixed shapes and contiguous layouts preferred by NPU matrix engines. GPU Tensor Core SpMM methods cannot be directly transferred to NPUs with decoupled vector and matrix engines. We present AscSpMM, which separates irregular operand preparation from regular matrix computation through a parameterized Vector-CSR representation. The vector engine decodes indices and gathers and reorganizes dense operands, while the Cube engine performs matrix multiply-accumulate operations. A double-slot ring buffer enables dependency-aware asynchronous pipelining, while operand reuse and runtime-adaptive tiling reduce cross-engine stalls. On an Ascend 910B3, AscSpMM achieves geometric-mean speedups of 2.36x over GEMM, 19.92x over an existing SpMM implementation, and 5.82x over cuSPARSE on an A100. It reduces matrix-input storage and peak HBM footprint by 48.24% and 22.98% on average, while remaining competitive with specialized GPU Tensor Core SpMM kernels. The code is available at https://github.com/LfLab-AI/Ascend-NPU-SpMM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Fei Li, Haoxin Li, Kehong Liu, Yanzi Zhou, Weiguo Wu, Shiqiang Nie, Jinyu Wang, Song Liu
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/LfLab-AI/Ascend-NPU-SpMM](https://github.com/LfLab-AI/Ascend-NPU-SpMM)
- 阅读深度：metadata
