---
title: "Exploring Sparse Matrix Multiplication Kernels on the Cerebras CS-3"
description: "In recent years, novel AI accelerators have emerged as promising alternatives to GPUs for AI model training and inference."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.27985) · [PDF](https://arxiv.org/pdf/2604.27985)

## 一句话摘要

In recent years, novel AI accelerators have emerged as promising alternatives to GPUs for AI model training and inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

In recent years, novel AI accelerators have emerged as promising alternatives to GPUs for AI model training and inference. One such accelerator, the Cerebras CS-3, has demonstrated strong performance on machine learning as well as scientific applications, such as molecular dynamics and seismic simulations. While the benefits of Cerebras systems for dense workloads have been well demonstrated, their potential for sparse workloads is not yet understood, particularly for large matrices that cannot fit on the device when represented in dense format. Yet, many applications, such as linear solvers and graph neural networks, rely on large sparse matrices. In this work, we make a step toward a better understanding of the use of CS-3 platforms for sparse operations. To this end, we explore two key sparse linear algebra kernels, sparse-dense matrix multiplication (SpMM) and sampled dense-dense matrix multiplication (SDDMM), on the Cerebras CS-3. We propose low-level CS-3 designs for these operations and optimize them to improve I/O performance, memory footprint, and scalability to large matrices. We evaluate speedup relative to the CPU. The results show that our CS-3 kernels can outperform the CPU by up to 100$\times$ for SpMM on 90\% sparse matrices, with performance improving as matrix dimensionality increases. SDDMM on the CS-3 can outperform the CPU by up to 20$\times$ on 90\% sparse matrices. However, as sparsity increases beyond 99\%, our kernels suffer performance degradation, approaching the performance of state-of-the-art CPU libraries or even underperforming them.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Milan Shah, Sheng Di, Michela Becchi
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
