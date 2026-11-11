---
title: "Jointly Optimizing Memory, Computing and Offloading for Energy-Efficient DNN Inference"
description: "In edge intelligence systems, computation offloading and dynamic voltage and frequency scaling (DVFS) are widely used to improve energy efficiency."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.11106) · [PDF](https://arxiv.org/pdf/2611.11106)

## 一句话摘要

In edge intelligence systems, computation offloading and dynamic voltage and frequency scaling (DVFS) are widely used to improve energy efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

In edge intelligence systems, computation offloading and dynamic voltage and frequency scaling (DVFS) are widely used to improve energy efficiency. However, as applications like deep neural network (DNN) inference evolve in complexity, their demands for memory resources have progressively increased, establishing memory as a critical bottleneck that impacts both latency and energy consumption. In this paper, we propose a joint optimization scheme integrating memory, computing and offloading for energy-efficient DNN inference. We formulate the energy minimization problem under deadline constraints as a mixed-integer nonlinear programming (MINLP) problem, where the main challenge arises from the coupling between offloading and resource optimization. To address this issue, we decompose the original problem into two subproblems under a fixed offloading policy. The local subproblem is transformed into an equivalent geometric programming (GP) problem to derive the optimal memory frequency and computing frequency, while the edge subproblem is solved via convex optimization. An efficient coordinate descent (CD) algorithm is further developed to jointly optimize all variables. Simulation results demonstrate that our proposed algorithm achieves near-optimal performance with the gap from the optimal policy being at most 9.3%, and reduces the energy consumption of devices by up to 16.1% compared with benchmarks without memory frequency optimization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yunchu Han, Zhaojun Nan, Sheng Zhou, Zhisheng Niu
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
