---
title: "A Resource-Efficient and Precision-Scalable FPGA Accelerator for Spiking Neural Networks Using Minifloat Arithmetic"
description: "Spiking neural networks (SNNs) are well suited to event-driven edge intelligence, but the arithmetic complexity, memory footprint, and power consumption associated with conventional floating-point implementations can limit their deployment on resource-constrained hardware."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.32052) · [PDF](https://arxiv.org/pdf/2610.32052)

## 一句话摘要

Spiking neural networks (SNNs) are well suited to event-driven edge intelligence, but the arithmetic complexity, memory footprint, and power consumption associated with conventional floating-point implementations can limit their deployment on resource-constrained hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks (SNNs) are well suited to event-driven edge intelligence, but the arithmetic complexity, memory footprint, and power consumption associated with conventional floating-point implementations can limit their deployment on resource-constrained hardware. This paper presents a precision-scalable and resource-efficient SNN hardware accelerator architecture based on parameterized minifloat arithmetic. The proposed architecture implements recurrent leaky integrate-and-fire (LIF) neurons and leaky-integrator (LI) readout neurons using a unified minifloat datapath whose word length and mantissa width can be configured at synthesis time. A valid-driven arithmetic subsystem employs pipelined minifloat multiplication and addition, while time-multiplexed processing enables arithmetic resources to be shared across synaptic accumulation, neuron-state updates, recurrent connections, and output processing. This organization reduces replicated arithmetic hardware and provides a scalable design approach for different SNN sizes and precision requirements. The architecture supports E8M23, E5M10, E5M6, and E4M3 formats within the same RTL framework, allowing precision, memory capacity, timing, and power to be traded without modifying the underlying neuron architecture. FPGA implementation results demonstrate that reducing minifloat precision substantially decreases arithmetic-resource utilization and estimated dynamic power, while also reducing the theoretical storage requirement of synaptic parameters. A recurrent event-based classification network is used as a hardware validation case, demonstrating that substantial precision reduction can be achieved while retaining competitive inference accuracy. The results establish parameterized minifloat computation as an effective basis for scalable, low-resource, and energy-efficient FPGA SNN accelerators.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ali Mehrabi, Philip C. Jose
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
