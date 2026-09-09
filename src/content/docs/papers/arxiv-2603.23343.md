---
title: "Numerical Kernels on a Spatial Accelerator: A Study of Tenstorrent Wormhole"
description: "As AI accelerators gain prominence, their potential for traditional scientific computing workloads remains unclear."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2603.23343) · [PDF](https://arxiv.org/pdf/2603.23343)

## 一句话摘要

As AI accelerators gain prominence, their potential for traditional scientific computing workloads remains unclear.

## 为什么值得关注

待编辑增强。

## 摘要原文

As AI accelerators gain prominence, their potential for traditional scientific computing workloads remains unclear. This paper explores Tenstorrent's Wormhole architecture, a spatial computing platform designed for neural network acceleration, by implementing three numerical kernels and composing them into a conjugate gradient solver. We present architecture-specific optimizations for sparse numerical algorithms, evaluate their performance against Nvidia GPUs, and expose both challenges and opportunities in porting numerical methods to spatial architectures. Our results demonstrate that AI accelerators merit consideration for workloads traditionally dominated by CPUs and GPUs, and more work should be invested in understanding the capabilities of these architectures and making them accessible to the scientific computing community.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Maya Taylor, Carl Pearson, Luc Berger-Vergiat, Giovanni Long, Jan Ciesko
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
