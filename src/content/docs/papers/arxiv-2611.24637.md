---
title: "Hypnos: A Dual-Phase End-to-End Platform for Scalable Continual Learning at the Edge"
description: "Continual learning (CL) enables neural networks to adapt to non-stationary data streams by mitigating catastrophic forgetting, offering a path to robust, private, and adaptable edge devices."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.24637) · [PDF](https://arxiv.org/pdf/2611.24637)

## 一句话摘要

Continual learning (CL) enables neural networks to adapt to non-stationary data streams by mitigating catastrophic forgetting, offering a path to robust, private, and adaptable edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continual learning (CL) enables neural networks to adapt to non-stationary data streams by mitigating catastrophic forgetting, offering a path to robust, private, and adaptable edge devices. Yet, porting CL to real-world edge devices remains challenging for two reasons: (i) online operation, where sensor data arrives one sample at a time and the device must adapt on-the-fly, and (ii) the low footprint of edge devices, which makes traditional error backpropagation training prohibitive. Inspired by the brain's wake and sleep cycles, the former for rapid adaptation with minimal resources and the latter for long-term consolidation, we introduce Hypnos, an open-source dual-phase platform for efficient CL at the edge. In the wake phase (e.g., daily operation), Hypnos relies on a low-footprint system-on-chip with a RISC-V microcontroller unit (MCU) targeting efficient inference and supporting lightweight gradient-free prototype updates. In the sleep phase (e.g., night-time charging), where wall-plug energy and larger memory budgets are available, a smart charger performs rehearsal-based gradient updates for consolidation. Deployed on a ZCU104 field-programmable gate array (FPGA) and synthesized in a 28-nm process, Hypnos is benchmarked on the CORe50 NICv2-391 protocol. It sets a new state-of-the-art accuracy of 78.6%-81.6% for edge CL systems, with an on-device latency of 7.79s-10.54s per sample depending on activation precision, and requires $3.8\times$ fewer learning steps and $22\times$ less learning compute than quantized latent replay at higher accuracy and comparable latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Guilherme Guedes, Marco Apolinario Lainez, Charlotte Frenkel
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
