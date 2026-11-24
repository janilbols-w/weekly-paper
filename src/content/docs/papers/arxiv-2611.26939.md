---
title: "Acceleration of Sparse and Irregular Workloads through Energy-Efficient Stream Extensions"
description: "The slowdown of Moore's law and Dennard scaling has motivated computer architects to uphold performance scaling through architectural specialization."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.26939) · [PDF](https://arxiv.org/pdf/2611.26939)

## 一句话摘要

The slowdown of Moore's law and Dennard scaling has motivated computer architects to uphold performance scaling through architectural specialization.

## 为什么值得关注

待编辑增强。

## 摘要原文

The slowdown of Moore's law and Dennard scaling has motivated computer architects to uphold performance scaling through architectural specialization. So far, most efforts have focused on highly regular workloads, which exhibit good data locality, ample reuse, and a data-independent execution flow. As this specialization hits diminishing returns, attention shifts towards sparse and irregular workloads, which are essential to applications like sparse neural networks, multiphysics simulations, and graph analytics. However, they lack the convenient properties of highly regular compute that modern architectures are optimized for, resulting in very low (<10%) functional unit utilization on traditional CPUs and GPUs. The most promising approaches to their general hardware acceleration leverage memory streams, which decouple data movement from execution. In this thesis, we explore energy-efficient hardware stream extensions that significantly accelerate sparse and irregular workloads in general-purpose systems without specializing to specific application domains or compromising on regular-workload performance. We design a flexible, core-coupled stream extension supporting affine and indirect streams as well as intersection and union of sparse tensors. We integrate it into an energy-efficient RISC-V compute cluster, achieving significant performance and energy efficiency benefits on general sparse linear algebra, and further use it to accelerate stencil computations, spiking neural network inference, and model-predictive control. We evaluate it at scale in a 432-core 2.5D RISC-V system fabricated in 12nm FinFET, achieving leading compute utilization and energy efficiency on sparse and irregular workloads while remaining competitive on regular workloads. Finally, we extend chip-level interconnects with end-to-end irregular streams, improving performance, energy efficiency, and bus utilization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Paul Scheffler
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
