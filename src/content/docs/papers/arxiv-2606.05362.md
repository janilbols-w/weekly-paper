---
title: "TESSERA: A Workload-Driven Simulation and Design-Space Exploration Framework for Heterogeneous NPUs"
description: "AI model architectures are diversifying rapidly."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.05362) · [PDF](https://arxiv.org/pdf/2606.05362)

## 一句话摘要

AI model architectures are diversifying rapidly.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI model architectures are diversifying rapidly. While CNNs and transformers rely on dense matrix multiplication, emerging architectures (state-space models, fast Fourier transform (FFT)-based long convolutions, Kolmogorov-Arnold networks, and spiking networks) are not multiply-accumulate (MAC) dominated; they spend much of their computation on vector and non-MAC primitives that homogeneous, MAC-centric neural processing units (NPUs) serve poorly. This motivates heterogeneous NPUs (HPUs) built from non-identical tiles. However, prior designs vary only one or two architectural dimensions and target narrow workloads, while existing frameworks lack support for jointly exploring fine-grained tile-level heterogeneity. We present TESSERA, an analytical simulator and design-space-exploration (DSE) framework for HPU microarchitecture design. TESSERA jointly explores tile-type composition (large Big, small Little, and non-MAC Special-Function tiles), MAC array size, precision, dataflow, sparsity mode, MAC engine type, and special-function units for FFT, spiking-integrate, and polynomial operators. Unlike prior simulators that assume a single homogeneous tile type, TESSERA provides dedicated energy, area, and timing models for non-MAC tiles and maps operators across heterogeneous tiles with a heterogeneity-aware compiler. A multi-seed DSE pipeline combines stratified sampling with genetic-algorithm refinement to identify Pareto-optimal designs. Cost models are calibrated to a 7 nm node and cross-validated against NVIDIA's Deep Learning Accelerator (NVDLA). Across a 20-workload suite, the best general-purpose HPU found by TESSERA (~200 mm^2, Big+Little+Special-Function) achieves 46.91% mean energy savings over the best iso-area homogeneous baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Arghadip Das, Hoseok Kim, Soomin Lee, Arnab Raha, Deepak A Mathaikutty, Vijay Raghunathan
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
