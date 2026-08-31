---
title: "Hardware-Software Co-Design for Event-Driven SNN Deployment on Low-Cost Neuromorphic FPGAs"
description: "Low-cost FPGA platforms can broaden access to neuromorphic systems research, but current spiking neural network (SNN) workflows remain divided between hardware-first implementations, which are difficult to integrate with PyTorch-style development, and software-first frameworks, which often stop at simulation or GPU execution."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2604.22179) · [PDF](https://arxiv.org/pdf/2604.22179)

## 一句话摘要

Low-cost FPGA platforms can broaden access to neuromorphic systems research, but current spiking neural network (SNN) workflows remain divided between hardware-first implementations, which are difficult to integrate with PyTorch-style development, and software-first frameworks, which often stop at simulation or GPU execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-cost FPGA platforms can broaden access to neuromorphic systems research, but current spiking neural network (SNN) workflows remain divided between hardware-first implementations, which are difficult to integrate with PyTorch-style development, and software-first frameworks, which often stop at simulation or GPU execution. This paper presents a semantics-preserving hardware-software co-design framework for the deterministic deployment of PyTorch-defined SNNs to event-driven FPGA execution. A single exported artifact carries weights, thresholds, connectivity descriptors, and grouped time-to-first-spike (TTFS) decoding metadata from software definition to board execution and is reused unchanged by both the software reference and the board runtime. A 10-class MNIST TTFS classifier implemented in the routed 80 MHz design achieves 87.40% accuracy and matches the software reference on all 10,000 test images. The programmable-logic path delivers a service latency of 0.1375 {\mu}s/image and an estimated dynamic energy of 31.6 nJ/image, while scope-aware comparisons with matched GPU and CPU baselines keep accelerator-only and system-level measurements distinct. These results show that low-cost event-driven FPGA hardware can provide a direct and reproducible software-to-board path for software-defined SNN models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 4 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiwoon Lee, Souvik Chakraborty, Syed Bahauddin Alam, Cheolsoo Park
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
