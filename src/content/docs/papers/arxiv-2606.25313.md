---
title: "Programmable Probabilistic Computer with 1,000,000 p-bits"
description: "Many problems in physics and machine learning require sampling the collective states of large numbers of interacting variables."
---

**评分：38/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2606.25313) · [PDF](https://arxiv.org/pdf/2606.25313)

## 一句话摘要

Many problems in physics and machine learning require sampling the collective states of large numbers of interacting variables.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many problems in physics and machine learning require sampling the collective states of large numbers of interacting variables. On modern graphics processors, repeated movement of interaction data between memory and compute units can limit how efficiently these calculations can scale. Here we demonstrate a programmable probabilistic computer with one million interacting probabilistic bits (p-bits) across 18 field-programmable gate arrays, sustaining $10^{12}$ probabilistic updates per second. Coupling weights remain beside the update circuits in on-chip memory, and only single-bit boundary states pass between devices. Experiments on three-dimensional and quasi-two-dimensional spin glasses show that the ratio of boundary-exchange frequency to local update frequency controls the effect of communication delays on optimization. A bound derived from the graph partition and interconnect identifies operating conditions that recover the residual-energy decay of an unpartitioned GPU reference. Infrequent exchange reduces the decay exponent, although faster local updates can shorten the time to reach a target energy. A cluster mean-field model reproduces this dependence, while ferromagnetic sampling experiments reveal a corresponding dependence of magnetization relaxation on the same frequency ratio. These results establish a million-p-bit computing architecture in which processing and local memory scale together, and provide a quantitative design principle for exploiting tolerance to communication delays in larger probabilistic computers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Navid Anjum Aadit, Xiuqi Zhang, Shuvro Chowdhury, Kevin Callahan-Coray, Kyle Lee, Saleh Bunaiyan, Sanjay Seshan, Clayton Thomas, Jason Twigg, Andrew Seawright, Forrest Brewer, Tathagata Srimani, Kerem Y. Camsari
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
