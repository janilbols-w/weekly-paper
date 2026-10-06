---
title: "FedUHD: Unsupervised Federated Learning using In-Memory Hyperdimensional Computing"
description: "Unsupervised federated learning (UFL) enables privacy-preserving distributed training without data labeling, yet practical deployment remains challenging due to non-IID data, high computational and communication costs at edge devices, and sensitivity to communication noise."
---

**评分：50/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2508.12021) · [PDF](https://arxiv.org/pdf/2508.12021)

## 一句话摘要

Unsupervised federated learning (UFL) enables privacy-preserving distributed training without data labeling, yet practical deployment remains challenging due to non-IID data, high computational and communication costs at edge devices, and sensitivity to communication noise.

## 为什么值得关注

待编辑增强。

## 摘要原文

Unsupervised federated learning (UFL) enables privacy-preserving distributed training without data labeling, yet practical deployment remains challenging due to non-IID data, high computational and communication costs at edge devices, and sensitivity to communication noise. We propose FedUHD, the first UFL framework based on Hyperdimensional Computing (HDC). On the client side, FedUHD employs kNN-based cluster hypervector removal to mitigate non-IID effects by filtering detrimental local outliers. On the server side, cluster-aware HDC aggregation leverages cluster-level statistics to stabilize learning across heterogeneous clients. To further improve efficiency, we design a compute-in-memory (CIM) accelerator based on a novel phase-change memory (PCM) device, integrated with lightweight ASIC digital modules to execute the client-side HDC pipeline within the accelerator. The intrinsic robustness of HDC to low precision and device variations enables efficient mapping onto analog PCM crossbars, exploiting massive parallelism while minimizing data movement. Experimental results show that FedUHD achieves comparable accuracy to state-of-the-art neural network-based UFL methods across all datasets. On HAR and CIFAR10/100, FedUHD delivers an average 2,239x speedup and 1,542x higher energy efficiency on GPU. In addition, FedUHD reduces communication cost by up to 176x on HAR and CIFAR10/100 and demonstrates greater robustness than Orchestra under communication noise. Compared to GPU implementation of FedUHD, the proposed PCM-based accelerator provides an additional 4.07x speedup and three orders of magnitude higher energy efficiency on average. Furthermore, the results demonstrate the benefit of PCM over RRAM as a CIM substrate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：You Hak Lee, Keming Fan, Xiaofan Yu, Quanling Zhao, Tianqi Zhang, Flavio Ponzina, Tajana Rosing
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
