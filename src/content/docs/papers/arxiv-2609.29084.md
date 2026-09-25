---
title: "A Rapid Pipeline for Training and Deploying ML Models on WeBe Band"
description: "Developing optimized machine-learning algorithms for edge devices with limited computational and memory resources is challenging, time-consuming, and highly dependent on device-specific constraints."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.29084) · [PDF](https://arxiv.org/pdf/2609.29084)

## 一句话摘要

Developing optimized machine-learning algorithms for edge devices with limited computational and memory resources is challenging, time-consuming, and highly dependent on device-specific constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Developing optimized machine-learning algorithms for edge devices with limited computational and memory resources is challenging, time-consuming, and highly dependent on device-specific constraints. In this work, we streamline an edge ML workflow to enable rapid development, optimization, and deployment of machine-learning (ML) models directly on the WeBe Band, a wrist-worn wearable device designed for multimodal physiological data monitoring. The proposed system automatically generates hardware-efficient ML models that can be easily integrated into the WeBe core firmware, supporting AutoML, hardware-aware quantization, and performance profiling to build models that meet desired latency targets while remaining compatible with device memory and power limitations. The proposed framework tightly integrates the open-source Piccolo AI ecosystem with an automated pipeline that generates deployable firmware artifacts, performs hardware-aware model compilation, and supports over-the-air (OTA) deployment. The system supports multiple lightweight model classes, including classical machine-learning algorithms and neural networks, and provides built-in on-device profiling tools to evaluate inference latency and memory footprint under realistic execution conditions. Experimental results demonstrate clear trade-offs between model complexity and deployability on a microcontroller, showing that classical models offer strong real-time performance while lightweight neural networks require careful resource management. Rather than proposing new learning architectures, the current work mainly focuses on system-level automation, deployability, and enabling researchers and developers to rapidly iterate on models and evaluate them directly on target hardware. Although demonstrated on the WeBe Band platform, the workflow is designed to be extensible to other ML-powered edge devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ehsan Kourkchi, Asmita Asmita, Houman Homayoun, Mahdi Eslamimehr
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
