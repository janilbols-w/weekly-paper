---
title: "Lonic: Algorithm-Hardware Co-Design for Energy-Efficient Fully Local Online SNN Training with INT4 Precision"
description: "Spiking neural networks (SNNs) have recently attracted increasing attention as an energy-efficient learning paradigm."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.12500) · [PDF](https://arxiv.org/pdf/2608.12500)

## 一句话摘要

Spiking neural networks (SNNs) have recently attracted increasing attention as an energy-efficient learning paradigm.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks (SNNs) have recently attracted increasing attention as an energy-efficient learning paradigm. Existing works also propose temporally and fully local online SNN training algorithms to address memory and computation overhead. However, they do not consider whether the algorithmic advantages can be effectively translated into real-device efficiency. To address this challenge, we present Lonic, an algorithm-hardware co-design for energy-efficient and scalable fully local online supervised SNN learning. On the algorithm side, we implement an INT4 low-precision training algorithm for fully local online SNN learning while maintaining accuracy. On the hardware side, to leverage the benefits of the proposed algorithm, we introduce reconfigurable multiplier-free integer PE arrays, dual-optimization zero-gating strategy, temporal prefix-accelerated local learning dataflow, and low-precision weight movement to significantly improve training efficiency. Compared to Apple M4 and Nvidia V100 GPUs, Lonic achieves average energy efficiency improvements of 17.44x and 66.28x, respectively, along with speedups of 3.25x and 1.02x, respectively. Moreover, Lonic achieves 15.95x (14.64x) and 1.52x (7.28x) energy efficiency (area efficiency) over ASIC TPU-like and H2Learn accelerators, respectively. The code for Lonic is available at https://github.com/peilin-chen/Lonic.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Peilin Chen, Xiaoxuan Yang
- 发布：2026-08-12；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/peilin-chen/Lonic](https://github.com/peilin-chen/Lonic)
- 阅读深度：metadata
