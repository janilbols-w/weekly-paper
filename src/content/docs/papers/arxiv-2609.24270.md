---
title: "Dissecting How Die Scaling Breaks GPU Fine-grained Scheduling"
description: "Modern GPUs are no longer physically symmetric."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.24270) · [PDF](https://arxiv.org/pdf/2609.24270)

## 一句话摘要

Modern GPUs are no longer physically symmetric.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern GPUs are no longer physically symmetric. Die scaling leads to both manufacturing-driven floorsweeping and cache and memory partitioning. The former creates chip-specific compute topologies, while the latter causes non-uniform memory access. These asymmetries are substantial. Topology-oblivious compute unit allocation can lead to up to 1.33x performance variation, while remote accesses increase HBM latency by up to 67% and nearly double L2 latency. However, these asymmetries are hidden behind the GPU's logical resource abstractions and can vary across chips. We develop lightweight characterization methods to uncover per-chip compute topology and memory affinity. We then use the discovered information to make existing fine-grained scheduling asymmetry-aware, considering not only how many resources are allocated but also which physical resources are assigned. Across full-GPU kernel execution, intra-application multiplexing, and inter-application co-location, asymmetry-aware scheduling improves mainstream kernels by up to 1.22x, multiplexed LLM inference by up to 14.3%, and avoids up to 1.33x performance variation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiaoze Fan, Jianhao Wang, Weihao Cui, Han Zhao, Zhuobin Huang, Yangjie Zhou, Yuxian Qiu, Shixuan Sun, Bingsheng He, Quan Chen, Minyi Guo
- 发布：2026-09-21；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
