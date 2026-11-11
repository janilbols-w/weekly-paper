---
title: "GARDEN: Efficient GPU-Accelerated Billion-Scale GNN Training via Caching-Sampling-Batching Co-Design"
description: "Graph Neural Networks (GNNs) have shown impressive performance in diverse tasks such as social network analysis and recommendation systems."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.11043) · [PDF](https://arxiv.org/pdf/2611.11043)

## 一句话摘要

Graph Neural Networks (GNNs) have shown impressive performance in diverse tasks such as social network analysis and recommendation systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Graph Neural Networks (GNNs) have shown impressive performance in diverse tasks such as social network analysis and recommendation systems. However, scaling their training to billion-edge graphs is hindered by the memory wall: GPU memory capacity falls short of the massive storage requirements for node features and topology. Sampling-based GNN training frameworks mitigate this by streaming subgraphs from CPU to GPU, but they incur prohibitive PCIe data transfers and non-coalesced memory accesses, resulting in bandwidth underutilization and low compute efficiency. We propose GARDEN, a GPU-accelerated sampling-based system that co-designs caching, sampling, and batching to eliminate these bottlenecks. GARDEN introduces three key innovations: (1) an Adaptive High-Fidelity Cache Allocator (AHFCA) that combines offline reuse profiling and online hotness tracking to dynamically cache features and adjacency lists within a fixed GPU memory budget, avoiding static allocation waste; (2) a Grouping-based Parallel Sampler that reorders stochastic neighborhood accesses(GPS) to maximize warp occupancy and hide latency on power-law graphs; and (3) a Super-batch Degree Classifier(SDC) that fuses mini-batches into degree-homogeneous groups, enabling cache-friendly coalesced transfers and high GPU utilization. Evaluations on real-world billion-scale graphs demonstrate that GARDEN achieves 4.54x, 1.27x, and 2.97x end-to-end training speedups over DGL-UVA, DUCATI, and FastGL, respectively, while maintaining model convergence and accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Qingrui Zhu, Lei Liu, Yushu Cai, Kai Sheng, Zhiwen Chen, Xin He
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
