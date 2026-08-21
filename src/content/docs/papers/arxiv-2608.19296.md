---
title: "HyperCut: Fast Inter-Layer Scheduling via Directed Hypergraph and Early Filtering"
description: "As deep neural networks (DNNs) continue to scale, inter-layer scheduling, which orchestrates the spatial allocation of compute resources and the temporal execution order across layers, has become a decisive factor in sustaining high utilization and energy efficiency on tiled accelerators."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.19296) · [PDF](https://arxiv.org/pdf/2608.19296)

## 一句话摘要

As deep neural networks (DNNs) continue to scale, inter-layer scheduling, which orchestrates the spatial allocation of compute resources and the temporal execution order across layers, has become a decisive factor in sustaining high utilization and energy efficiency on tiled accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

As deep neural networks (DNNs) continue to scale, inter-layer scheduling, which orchestrates the spatial allocation of compute resources and the temporal execution order across layers, has become a decisive factor in sustaining high utilization and energy efficiency on tiled accelerators. However, existing inter-layer schedulers defer cost feedback until a complete fine-grained intra-layer scheduling has been resolved. The resulting decoupled flow repeatedly explores sub-optimal or even infeasible inter-layer schedules, and the absence of early pruning during the inter-layer phase remains a critical bottleneck for design-space exploration (DSE) in DNN compilers. Our key observation is that the cost of an intra-layer scheduling can be tightly upper-bounded once the inter-layer cut fixes the sub-mesh shape, which lets us cost every inter-layer candidate without solving the intra-layer problem. Hence, we propose a hierarchical partitioning-and-mapping framework, HyperCut, that enables early filtering of inter-layer schedules based on hypergraph partitioning. Based on the directed hypergraph (DHG) abstraction of DNN, we introduce a unified representation, State, that jointly encodes the DHG partition, tile mesh allocation and tensor batch splitting. Thereby, partitioning and mapping are coupled into a union optimization object. For a DNN with N layers, the resulting theoretical design space is bounded by O(N), compared with O(9.899^N) for the state-of-the-art open-source scheduler SET. Across 10 evaluated cases, HyperCut achieves 2.0x performance improvement and 80.47% exploration time reduction over the SET baseline, measured by geometric mean.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ziang Wei, Zirui Xu, Sufeng Guo, Chuanchao Gao, Yiyang Gao, Arvind Easwaran, Yuxiang Fu
- 发布：2026-08-19；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
