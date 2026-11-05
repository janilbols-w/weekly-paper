---
title: "ModelBlaster: Closing the Performance Gap through Learning-Augmented Agents Across Models, Kernels and Hardware Backends"
description: "Optimizing accelerator code across hardware architectures is difficult."
---

**评分：39/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.04104) · [PDF](https://arxiv.org/pdf/2611.04104)

## 一句话摘要

Optimizing accelerator code across hardware architectures is difficult.

## 为什么值得关注

待编辑增强。

## 摘要原文

Optimizing accelerator code across hardware architectures is difficult. ML compilers search predefined spaces of schedules and micro-kernels, while LLM-guided optimization can explore alternative algorithms, operator decompositions, and hardware-specific techniques. However, existing LLM agents typically target a single programming interface, toolchain, or accelerator family, focus on kernel-level optimization without model-level transforms, and offer limited reuse of experience across hardware targets. We present ModelBlaster, a Memory-Augmented In-Context Reinforcement Learning (MAIC-RL) framework for optimizing data-parallel kernels and whole models across heterogeneous SIMD and SIMT accelerators. Its mutable policy is a persistent knowledge base updated at inference time by Actor-Critic Textual Gradient Descent (AC-TGD). The knowledge base maps performance states to actions, outcomes, and constraints, enabling experience reuse across kernels, models, and hardware targets. A model-level optimizer uses kernel-level knowledge to inform whole-model decisions. The same optimization loop and knowledge schema support CUDA on NVIDIA GPUs, OpenCL on Qualcomm GPUs, and RVV intrinsics on RISC-V vector cores, with only lowering and measurement layers specific to each target. Compared with PyTorch, ModelBlaster achieves geometric-mean speedups of 1.85x, 5.58x, and 5.18x on KernelBench Levels 1, 2, and 3, and 1.69x on SOL-ExecBench Levels 1 and 2 on a B200 GPU. On Qualcomm Adreno GPUs, it achieves 5.8x over the vendor SDK and 1.7x over Apache TVM; on RISC-V vector cores, it achieves 2.7x over ExecuTorch with XNNPACK across 70 KernelBench problems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shengjun Kris Dong, Dima Nikiforov, Sahil Modi, Sana Damani, Edward C Lin, Siva Kumar Sastry Hari, Christos Kozyrakis
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
