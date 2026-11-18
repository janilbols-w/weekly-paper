---
title: "IA-MoE: An Intensity-Aware Mixture of Experts for DNN Inference"
description: "With the ever-increasing parameter scale and structural complexity of deep neural network (DNN) models, traditional cloud-based inference encounters bottlenecks in performance, privacy protection, and energy efficiency."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2611.19669) · [PDF](https://arxiv.org/pdf/2611.19669)

## 一句话摘要

With the ever-increasing parameter scale and structural complexity of deep neural network (DNN) models, traditional cloud-based inference encounters bottlenecks in performance, privacy protection, and energy efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the ever-increasing parameter scale and structural complexity of deep neural network (DNN) models, traditional cloud-based inference encounters bottlenecks in performance, privacy protection, and energy efficiency. While edge computing and edge intelligence facilitate the migration of inference tasks to edge servers closer to the data source, existing end-edge-cloud collaborative inference still encounters critical challenges, such as sensitivity to heterogeneous resources, complexity in multi-objective optimization, and adaptability to dynamic workloads. To achieve the joint optimization of end-to-end latency and energy consumption under dynamic inference requests with multi-resource constraints, we propose IA-MoE, an intensity-aware Mixture of Experts (MoE) framework. By modeling the model partitioning problem as a bilateral matching problem between layer tasks and virtual machine resources for each inference request, IA-MoE dynamically partitions DNN models in an edge-cloud hybrid computing environment. We evaluate IA-MoE using three representative DNNs (i.e., AlexNet, VGG16, ResNet50) on two public inference datasets in an enhanced CloudSimSDN simulation environment. Experimental results demonstrate that IA-MoE outperforms baseline methods regarding weighted normalized metrics for end-to-end latency and energy consumption. To our knowledge, this is the first study to introduce the MoE paradigm for DNN partitioning and collaborative inference in hybrid computing environments, providing a practical solution for efficient inference in artificial intelligence applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Meiyan Zeng, Sasu Tarkoma, Xiaoli Liu
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
