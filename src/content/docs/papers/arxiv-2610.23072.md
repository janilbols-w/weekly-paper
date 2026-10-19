---
title: "ScaleRAN: A Runtime for Elastic GPU Resource Management in AI-RAN"
description: "AI-RAN is driving the convergence of radio access network (RAN) processing and artificial intelligence (AI) workloads on GPU-enabled computing platforms, ranging from GPU-accelerated base stations to cloud-native infrastructures."
---

**评分：40/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.23072) · [PDF](https://arxiv.org/pdf/2610.23072)

## 一句话摘要

AI-RAN is driving the convergence of radio access network (RAN) processing and artificial intelligence (AI) workloads on GPU-enabled computing platforms, ranging from GPU-accelerated base stations to cloud-native infrastructures.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI-RAN is driving the convergence of radio access network (RAN) processing and artificial intelligence (AI) workloads on GPU-enabled computing platforms, ranging from GPU-accelerated base stations to cloud-native infrastructures. While GPU acceleration improves the efficiency of virtualized RAN functions, the computational demand of latency-critical baseband processing varies with traffic load, creating transient spare GPU capacity that can be reclaimed by co-located AI applications. Existing GPU-sharing mechanisms rely on coarse-grained hardware partitioning or static resource allocation, limiting their ability to adapt to slot-level workload fluctuations while preserving strict timing requirements. This paper presents ScaleRAN, a node-local runtime for elastic GPU resource management in AI-RAN. ScaleRAN leverages NVIDIA Green Contexts to dynamically partition Streaming Multiprocessors (SMs) between RAN and AI workloads through a ladder of pre-created GPU partitions, enabling low-overhead resource reallocation at RAN slot granularity. The proposed runtime naturally supports Open-RAN (O-RAN) O-Cloud deployments, one representative AI-RAN deployment scenario. To drive these reallocations, we propose a reactive controller inspired by Kubernetes autoscaling and a proactive controller based on quantile regression and conformal prediction. We also develop LDPCSim, a GPU-accelerated workload generator built on NVIDIA Aerial for reproducible evaluation. Results show that predictive fine-grained GPU partitioning satisfies slot-level RAN deadlines while increasing the GPU resources available to co-located AI workloads, demonstrating the practicality of elastic GPU sharing for future AI-RAN platforms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Arthur Hamard, J\'er\'emie Leguay, Gopalasingham Aravinthan, Alberto Conte, Julien Lallet, Abdelkader Outtagarts
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
