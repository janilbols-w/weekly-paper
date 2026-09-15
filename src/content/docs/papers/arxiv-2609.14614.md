---
title: "SH-WRNN: Implicit Spherical Harmonics Weight Field Routing Neural Networks for Asymmetric Edge Intelligence"
description: "Deep learning architectures remain rigidly built upon traditional fully connected layers."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.14614) · [PDF](https://arxiv.org/pdf/2609.14614)

## 一句话摘要

Deep learning architectures remain rigidly built upon traditional fully connected layers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep learning architectures remain rigidly built upon traditional fully connected layers. While networks scale up, few challenge this foundational root. In this work, we reshape this paradigm by transforming the core synapse weight matrix from static, discrete parameters into a differentiable, continuous field governed by spherical harmonics functions. We introduce the Implicit Spherical Harmonics Weight Field Routing Neural Network (SH-WRNN), which constrains weight matrices within a continuous parametric field instead of optimizing millions of localized discrete weights. When retrieving the weight matrix of the current layer, connection parameters are localized using latitude and longitude on a rectangular plane mapped from the continuous field. The latitudinal coordinate is specified by activated neurons from the previous layer, while the longitudinal coordinate is determined by keys generated from previous layer activations via matrix multiplication. By evaluating intersections on this map, the network dynamically extracts its connection weights on-the-fly. Empirical validation on MNIST demonstrates that under compact configurations of (32, 10, 10) and (32, 3, 10), SH-WRNN achieves robust accuracies of 91.05% and 81.54% within a single training epoch. Furthermore, we propose an asymmetric Surface Baking scheme. Upon convergence, the continuous weight field is baked once into a static parametric surface. By eliminating analytical spherical harmonics calculations during inference and reducing dynamic matrix extraction to high-speed localized memory slicing, this scheme achieves asymmetric algorithmic acceleration with negligible accuracy degradation. This paradigm shift bypasses GPU memory-bandwidth monopolies, opening a novel path to reshape the advantages of CPU computing. Code is available at https://github.com/jzb1111/SphericalHarmonyRoutedNeuralNetWork.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhibin Jiao, Xiangjing An
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jzb1111/SphericalHarmonyRoutedNeuralNetWork](https://github.com/jzb1111/SphericalHarmonyRoutedNeuralNetWork)
- 阅读深度：metadata
