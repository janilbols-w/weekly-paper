---
title: "FlexSpIM: An Event-Based Digital Compute-In-Memory Accelerator with Flexible Operand Resolution and Layer-Wise Hybrid Stationarity"
description: "Compute-in-memory (CIM) accelerators for spiking neural networks (SNNs) offer a promising solution for achieving $\\mu$s-level inference latency and ultra-low energy in edge vision applications."
---

**评分：52/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.08446) · [PDF](https://arxiv.org/pdf/2609.08446)

## 一句话摘要

Compute-in-memory (CIM) accelerators for spiking neural networks (SNNs) offer a promising solution for achieving $\mu$s-level inference latency and ultra-low energy in edge vision applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compute-in-memory (CIM) accelerators for spiking neural networks (SNNs) offer a promising solution for achieving $\mu$s-level inference latency and ultra-low energy in edge vision applications. However, their limited flexibility at both circuit and system levels restricts their deployment across diverse workloads. This work introduces FlexSpIM, a digital CIM architecture supporting arbitrary operand resolution and shape within a unified storage for weights and neuron states (i.e., membrane potentials). These circuit-level capabilities enable a layer-level hybrid weight- and output-stationary dataflow, maximizing operand reuse and reducing costly on- and off-chip data movement during SNN execution. Measurement results from a fabricated FlexSpIM prototype in 40-nm CMOS demonstrate competitive 1-bit-normalized energy efficiency and higher throughput compared with prior fixed-precision digital CIM-based SNN accelerators, while providing bitwise resolution reconfiguration. Evaluated on the IBM DVS gesture dataset, FlexSpIM achieves 95.8% accuracy while enabling up to 45% energy and 52% latency reductions in large-scale systems compared with fixed stationarity approaches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nicolas Chauvaux, Adrian Kneip, Charlotte Frenkel
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
