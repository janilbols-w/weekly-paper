---
title: "Edge AI and TinyML for Resource-Constrained Agriculture: Hardware Platforms, Model Optimization, and Deployment Strategies"
description: "Deploying artificial intelligence at the edge is increasingly important for systems that must operate under strict limits on memory, computation, energy, connectivity, and hardware cost."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.15085) · [PDF](https://arxiv.org/pdf/2603.15085)

## 一句话摘要

Deploying artificial intelligence at the edge is increasingly important for systems that must operate under strict limits on memory, computation, energy, connectivity, and hardware cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying artificial intelligence at the edge is increasingly important for systems that must operate under strict limits on memory, computation, energy, connectivity, and hardware cost. Tiny Machine Learning (TinyML) represents the most resource-constrained regime of this shift, enabling inference on microcontroller-class devices with tightly bounded flash and SRAM budgets. This study examines recent deployment trends in Edge AI and TinyML using precision farming as a representative real-world environment in which sensing nodes, gateways, UAVs, and embedded processors must often operate with intermittent connectivity and limited power. The analysis emphasizes the deployment stack rather than predictive accuracy alone, covering hardware classes, software toolchains, model- and system-level optimization, intelligence placement, and hardware-resource reporting. Across the analyzed studies, microcontroller-class platforms such as ESP32, STM32, and ATmega are prominent endpoint targets, while single-board computers and embedded accelerators support more compute-intensive workloads. Among the studies included in the optimization comparison, almost 50% report quantization, making reduced-precision inference the most frequently identified strategy within this subset. In contrast, structured pruning, hardware-aware neural architecture search, and coordinated cross-layer optimization remain comparatively limited. Resource profiling is also inconsistent as flash, peak RAM, MAC count, latency, and energy per inference are not reported uniformly, limiting reproducibility and comparisons across deployments. A recurring systems-level pattern is an inference-training asymmetry in which inference moves toward local devices while training and model lifecycle management remain predominantly centralized.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Riya Samanta, Bidyut Saha, Soumya Kanti Ghosh
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
