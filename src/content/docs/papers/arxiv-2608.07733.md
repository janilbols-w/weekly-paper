---
title: "LGNNIC: Acceleration of Large-Scale GNN Training using SmartNICs"
description: "Graph Neural Networks (GNNs) are widely used across domains such as natural sciences, social network analysis, chip design, and recommendation systems."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.07733) · [PDF](https://arxiv.org/pdf/2608.07733)

## 一句话摘要

Graph Neural Networks (GNNs) are widely used across domains such as natural sciences, social network analysis, chip design, and recommendation systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

Graph Neural Networks (GNNs) are widely used across domains such as natural sciences, social network analysis, chip design, and recommendation systems. However, as graph sizes grow, storing and processing them entirely on a single-node CPU-GPU system becomes increasingly impractical. A promising approach is to distribute the graph across multiple remote memory nodes, though this introduces a major bottleneck: inter-node network congestion during training. To address this, we propose LGNNIC, a novel inter-node system architecture that leverages SmartNICs co-located with remote memory nodes-a configuration already available in modern systems-to reduce communication overhead in distributed GNN training. LGNNIC offloads key preprocessing tasks to SmartNICs, reducing the volume of data transferred to computational (training) nodes and alleviating network congestion. We introduce two complementary techniques executed on the SmartNICs during the preprocessing phase: Neighbor Sampling, which performs mini-batch sampling, and Quantization of the sampled batches. To evaluate LGNNIC under different communication infrastructures, we designed both an optimized low-overhead DMA-based synchronization mechanism and a high-overhead socket-based alternative used as a benchmark. We evaluate the core SmartNIC offloading mechanisms across standard GNN workloads and sampling hyperparameters using a proof-of-concept (PoC) system comprising one remote-memory node with an NVIDIA BlueField-2 SmartNIC and one compute node with an A100 GPU. Both Neighbor Sampling and Quantization on the remote node demonstrated substantial training speedups in most configurations. Neighbor Sampling achieved up to 62.4x and 17.5x speedups with Sockets and DOCA-DMA, respectively, primarily due to reduced data transaction time. Quantization provided additional speedups of up to 3.6x and 1.3x, respectively, by reducing data transfer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Liad Gerstman, Aditya Dhakal, Dejan Milojicic, Avi Mendelson
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
