---
title: "Scaling Fourier-Based Sparse Matrix Analysis on GPUs"
description: "Sparse computations are important workloads in applications such as scientific computing, graph neural networks (GNNs), and machine learning."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.20483) · [PDF](https://arxiv.org/pdf/2609.20483)

## 一句话摘要

Sparse computations are important workloads in applications such as scientific computing, graph neural networks (GNNs), and machine learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse computations are important workloads in applications such as scientific computing, graph neural networks (GNNs), and machine learning. While many sparse operations can benefit from modern GPUs, the sparsity pattern remains important to performance because it affects memory coalescing, block organization, and load balancing. Previous studies show that spectral signatures can help analyze the global structure of sparse matrices. The fast Fourier transform (FFT) is commonly used to extract spectral signatures, and efficient GPU FFT libraries are available. However, sparse matrices, especially adjacency matrices for large graphs, tend to be very large and sparse. Existing dense-matrix-based FFT implementations are difficult to scale up, making the spectral patterns of these matrices difficult to obtain. We therefore propose a three-fold research approach comprising a lossless Binary-Sparse FFT (BS-FFT) and two compression methods: Elastic BS-FFT, which reuses the BS-FFT pipeline on a sampled frequency grid, and density-map-based spatial compression. Experiments show that BS-FFT reduces GPU memory use by 2.9--11.6 times relative to dense cuFFT and completes all 15 GNN adjacency matrices where dense cuFFT completes 6 on a 40 GB A100. Elastic BS-FFT and Density Map compression reduce GPU computation time by 2.0--1466.4 times relative to BS-FFT with spectral feature error of only 0.16% to 11.56% across the sampling rates from 6.25% to 0.0061%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ruifeng Zhang, Sai Krishna Teja Varma Manthena, Jiajia Li, Xipeng Shen
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
