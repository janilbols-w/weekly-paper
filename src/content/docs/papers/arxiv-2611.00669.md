---
title: "FPGA Acceleration of CNN-BiLSTM for EEG-Based Sleep Staging Featuring FFT-Based Non-Unit Stride Fast Convolution"
description: "Deep learning (DL) models for real-time wearable sleep staging often rely on long-kernel temporal convolutions, a requirement that current accelerators struggle to support efficiently."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.00669) · [PDF](https://arxiv.org/pdf/2611.00669)

## 一句话摘要

Deep learning (DL) models for real-time wearable sleep staging often rely on long-kernel temporal convolutions, a requirement that current accelerators struggle to support efficiently.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep learning (DL) models for real-time wearable sleep staging often rely on long-kernel temporal convolutions, a requirement that current accelerators struggle to support efficiently. To overcome this, we present an FPGA-based CNN-BiLSTM accelerator that incorporates several algorithm-hardware co-design techniques to enable efficient edge inference. Central to this design is an FFT-based non-unit stride fast convolution, which performs accumulation in the frequency domain to enable a single IFFT per block, reducing post-processing complexity to $O(N\log N)$. On the target long-kernel convolution layer, this yields a 20.5$\times$ reduction in arithmetic operations. Power-of-two quantization is applied across the pipeline, including FFT-based convolution and BiLSTM activations, with an average accuracy degradation of only 0.11% relative to the floating-point baseline across all subjects on the public MASS-SS3 dataset. Additional optimizations, including block convolution, depth-first execution, and hardware engine reuse minimize memory access and enhance resource utilization. The accelerator, implemented on a Xilinx Zynq-7000 FPGA, operates at 10 MHz and consumes 11 mW of dynamic power including data handling and configuration overhead from a microcontroller. The design achieves a DSP power efficiency of 0.91 GOPS/W/DSP using only 4 DSPs, demonstrating scalable and energy-efficient DL acceleration for sleep staging that can be extended to other wearable applications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aaron Zhou, Yaqian Xu, Chen Chen, James Yen, Weihang Zheng, Mark Zhao, Mingzhe Sun, Naize Yang, Andrew G. Richardson, Xilin Liu
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
