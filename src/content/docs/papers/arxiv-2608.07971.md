---
title: "ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters"
description: "Modern GPU clusters must simultaneously serve deep learning training and offline large language model inference workloads, yet existing schedulers treat these as isolated resource consumers with rigid, static allocations."
---

**评分：44/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2608.07971) · [PDF](https://arxiv.org/pdf/2608.07971)

## 一句话摘要

Modern GPU clusters must simultaneously serve deep learning training and offline large language model inference workloads, yet existing schedulers treat these as isolated resource consumers with rigid, static allocations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern GPU clusters must simultaneously serve deep learning training and offline large language model inference workloads, yet existing schedulers treat these as isolated resource consumers with rigid, static allocations. This leaves substantial GPU capacity underutilized: training jobs reserve entire devices despite periodic idle phases, while offline inference tasks over-provision GPUs despite bursty demand patterns. We present ElastiCo, an elastic co-location framework that enables training and inference workloads to safely share GPUs through three integrated mechanisms. First, Resource Shape Transformation exposes each job as a family of feasible resource-performance configurations. Second, Elastic Shadow Pricing decomposes the resulting multi-resource allocation problem into per-job configuration selection subproblems via dynamic per-resource shadow prices. Third, Interference-Aware Co-location uses a predictor trained on hardware-counter and task-level features to estimate pairwise performance degradation under GPU sharing. Implemented as native Kubernetes middleware requiring no user-code modifications, ElastiCo is evaluated on a 64-GPU testbed and through large-scale trace-driven simulations (up to 512 GPUs), reducing the average JCT by up to 2.94x, increasing the cluster throughput by 2.02x, and increasing the GPU utilization from approximately 25% to 46%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu sharing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jinghao Wang, Yihang Zhou, Xiaoyang Sun, Chunming Hu, Tianyu Wo, Xu Wang, Albert Y. Zomaya, Renyu Yang
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
