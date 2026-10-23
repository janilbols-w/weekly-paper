---
title: "Spike-Aware Gradient-Based Mixed-Precision Quantization of Spiking Neural Networks for Vision Applications"
description: "In recent years, Spiking Neural Networks (SNNs) have gained massive attention as an energy-efficient neural computing paradigm due to their event-driven and sparse computing capability."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.30339) · [PDF](https://arxiv.org/pdf/2610.30339)

## 一句话摘要

In recent years, Spiking Neural Networks (SNNs) have gained massive attention as an energy-efficient neural computing paradigm due to their event-driven and sparse computing capability.

## 为什么值得关注

待编辑增强。

## 摘要原文

In recent years, Spiking Neural Networks (SNNs) have gained massive attention as an energy-efficient neural computing paradigm due to their event-driven and sparse computing capability. However, maintaining accuracy under low-precision constraints, necessary for practical deployment, has been largely unexplored for SNN models. In addition, existing Hessian-based approaches for quantization, such as HAWQ-V2, incur significant memory and computational overhead due to temporal unrolling across multiple SNN timesteps. We propose a spike-aware gradient-based mixed-precision quantization framework for SNNs that adaptively assigns bit-widths using first-order gradient information, avoiding costly second-order Hessian computations. We evaluate our method across various SNN-based architectures, including VGG, ResNet, and Vision Transformer models obtained from both ANN-to-SNN conversion and direct training frameworks, on CIFAR10/100, ImageNet, and DVS-CIFAR-10 datasets. Notably, on ResNet-34 evaluated on ImageNet, our method achieves 73.30% accuracy at 4.78$\times$ compression, which is comparable to that provided by HAWQ-V2, while reducing memory consumption by 2.31$\times$ and bit-allocation runtime by 100$\times$. We also present an energy analysis for mixed-precision SNNs showing that the proposed quantization strategy enables energy-efficient deployment without compromising performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rajshekhar Rakshit, Devgokul B. V, Rakshitha Kalkura, Gopalakrishnan Srinivasan
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
