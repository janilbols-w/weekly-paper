---
title: "Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems"
description: "More Electric Aircraft require fast and reliable monitoring of high-frequency electrical networks, yet most power quality disturbance and fault diagnosis methods are developed for conventional 50 or 60 Hz grids."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.10479) · [PDF](https://arxiv.org/pdf/2609.10479)

## 一句话摘要

More Electric Aircraft require fast and reliable monitoring of high-frequency electrical networks, yet most power quality disturbance and fault diagnosis methods are developed for conventional 50 or 60 Hz grids.

## 为什么值得关注

待编辑增强。

## 摘要原文

More Electric Aircraft require fast and reliable monitoring of high-frequency electrical networks, yet most power quality disturbance and fault diagnosis methods are developed for conventional 50 or 60 Hz grids. This work presents a hardware-aware deep learning framework for multiclass detection of electrical faults and power quality disturbances in a 400 Hz aerospace power system. A high-fidelity simulation model inspired by the Boeing 787 electrical architecture generates voltage and current waveforms for 21 normal, disturbance, switching, open-circuit, and short-circuit conditions. Two datasets, each containing 73,500 samples, are formed from one-dimensional time-series signals and short-time Fourier transform time-frequency representations. Signal-processing augmentation, domain randomization, and class-specific generative adversarial networks increase waveform diversity, and the time-series dataset is released through IEEE DataPort. We compare 1D and 2D convolutional neural networks, long short-term memory networks, CNN-LSTM hybrids, ResNet, MobileNet, and VGG models under common training conditions. A compact ResNet provides the best accuracy-complexity tradeoff, achieving 96.94 percent software test accuracy with 175,685 parameters. After 8-bit quantization and deployment on a Xilinx Zynq UltraScale Plus MPSoC ZCU102, the model achieves 95.87 percent accuracy and a measured mean neural-network accelerator latency of 6.90 ms per input record. The results establish simulation-based, accelerator-level feasibility for embedded edge AI in aircraft electrical health monitoring and motivate future end-to-end data acquisition and experimental validation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator, hardware-aware
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ian C. Guzm\'an, Radu Babiceanu, Berker Pek\"oz
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
