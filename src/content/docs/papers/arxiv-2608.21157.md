---
title: "HIERA: Workload-Aware Planning Across Implementation Spaces for GPU Kernel Optimization"
description: "High-performance GPU kernels underpin modern deep learning and scientific computing."
---

**评分：51/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2608.21157) · [PDF](https://arxiv.org/pdf/2608.21157)

## 一句话摘要

High-performance GPU kernels underpin modern deep learning and scientific computing.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-performance GPU kernels underpin modern deep learning and scientific computing. As workloads become increasingly diverse and GPU hardware evolves rapidly, developing efficient methods for automated GPU kernel generation and optimization has become increasingly important. Existing LLM-based methods typically optimize within a fixed implementation space, limiting either optimization flexibility or search efficiency. We propose \textsc{HIERA}, a hierarchical search-space planning framework for GPU kernel optimization. \textsc{HIERA} constructs contract-augmented task specifications, selects an appropriate implementation space across PyTorch operators, CUDA libraries, and custom CUDA kernels, and uses profiling feedback and expert knowledge to guide structured iterative refinement. Experiments on KernelBench across multiple various workload levels and base LLMs show that \textsc{HIERA} delivers stronger overall implementation validity, sample efficiency, and optimization performance than existing training-free methods, while remaining competitive with the training-based CUDA-L1 without additional model training. A case study on a specialized stencil operator from scientific computing further achieves a \(1.53\times\) speedup over cuDNN, demonstrating the potentiality of the general framework beyond standard machine-learning workloads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel generation, kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinghao Wang, Qiqi Gu, Chenpeng Wu, Jianguo Yao, Haibing Guan, Xijun Li
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
