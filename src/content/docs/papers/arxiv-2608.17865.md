---
title: "ESR-HGNN: Eliminating Semantic Redundancy for Efficient Mini-batch HGNN Inference"
description: "Heterogeneous graph neural networks (HGNNs) are highly effective in processing heterogeneous graph data and have been widely adopted in critical domains."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.17865) · [PDF](https://arxiv.org/pdf/2608.17865)

## 一句话摘要

Heterogeneous graph neural networks (HGNNs) are highly effective in processing heterogeneous graph data and have been widely adopted in critical domains.

## 为什么值得关注

待编辑增强。

## 摘要原文

Heterogeneous graph neural networks (HGNNs) are highly effective in processing heterogeneous graph data and have been widely adopted in critical domains. As real-world graph data continues to scale, performing direct inference on entire graphs becomes increasingly infeasible, making mini-batch methods the standard approach. However, in end-to-end HGNN inference, metapath-based mini-batch sampling constitutes a significant performance bottleneck due to the extensive random memory accesses induced by the irregular traversal of graph structures. Existing sampling paradigms suffer from excessive redundant traversals caused by inherent semantic redundancy, severely degrading sampling efficiency and, consequently, leading to suboptimal mini-batch inference performance. In this work, we propose a redundancy-aware HGNN sampling paradigm that leverages a metapath trie to reuse traversal paths, effectively eliminating redundant memory accesses. We then map it onto a multi-channel hardware sampling unit denominated ESR-HGNN. Furthermore, we introduce a reusability-driven metapath grouping technique that optimally clusters metapaths to maximize reusable traversal paths within hardware channels, enhancing efficiency in scenarios with semantic parallelism. Extensive experimental results demonstrate that ESR-HGNN achieves an average sampling performance improvement of one order of magnitude over CPU and GPU, accompanied by significant energy savings. Additionally, it delivers substantial speedup in end-to-end mini-batch inference when integrated with GPU and state-of-the-art HGNN inference accelerator.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dengke Han, Mingyu Yan, Duo Wang, Wenming Li, Xiaochun Ye, Dongrui Fan
- 发布：2026-08-19；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
