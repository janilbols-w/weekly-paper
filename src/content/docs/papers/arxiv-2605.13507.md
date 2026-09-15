---
title: "Implementation of an Adaptive Transformer Accelerator for Accurate Outdoor Localization with Massive MIMO"
description: "We present a sparsity-aware FPGA implementation of an adaptive Transformer-based localization accelerator for 5G massive MIMO targeting sub-10\\,ms real-time positioning."
---

**评分：51/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2605.13507) · [PDF](https://arxiv.org/pdf/2605.13507)

## 一句话摘要

We present a sparsity-aware FPGA implementation of an adaptive Transformer-based localization accelerator for 5G massive MIMO targeting sub-10\,ms real-time positioning.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present a sparsity-aware FPGA implementation of an adaptive Transformer-based localization accelerator for 5G massive MIMO targeting sub-10\,ms real-time positioning. The architecture exploits propagation characteristics, where beam-delay channel representations exhibit sparsity, enabling a row-wise skipping mechanism that removes low-energy beam components with minimal control overhead. Transformer computations are mapped onto a heterogeneous vector processing engine with parallel processing elements and adder trees, using mixed input- and output-stationary dataflow execution for efficient matrix computation and reduced data movement. Environment-dependent processing is supported through a lightweight runtime model-switching mechanism, where temporally filtered outputs of a single-layer perceptron router enable selection between specialized models with reduced latency. Implemented on a Xilinx Zynq UltraScale+ FPGA and evaluated on real-world massive MIMO measurements, the design achieves up to 65\% row sparsity, yielding peak computational speedups of approximately 2x while limiting the average localization accuracy degradation to below 10\%, relative to the fixed-point baseline model. The accelerator attains below 1.15\,m localization accuracy across scenarios, with inference latency of 0.51-2.11\,ms and throughput of up to 1961 positions/s. These results demonstrate that propagation-aware sparsity, mixed dataflow execution, and efficient runtime model switching enable a scalable and low-latency hardware realization of adaptive Transformer-based localization for real-time 5G systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ilayda Yaman, Sijia Cheng, Ove Edfors, Liang Liu
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
