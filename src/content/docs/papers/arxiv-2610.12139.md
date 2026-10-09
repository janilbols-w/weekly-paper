---
title: "Toward Intelligent Networks via AI-Aware GPU-Native Packet Processing"
description: "The integration of inline Artificial Intelligence (AI) models into critical network infrastructure is fundamentally bottlenecked by the high latency and synchronization overhead of CPU-mediated packet processing."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.12139) · [PDF](https://arxiv.org/pdf/2610.12139)

## 一句话摘要

The integration of inline Artificial Intelligence (AI) models into critical network infrastructure is fundamentally bottlenecked by the high latency and synchronization overhead of CPU-mediated packet processing.

## 为什么值得关注

待编辑增强。

## 摘要原文

The integration of inline Artificial Intelligence (AI) models into critical network infrastructure is fundamentally bottlenecked by the high latency and synchronization overhead of CPU-mediated packet processing. While legacy GPU offload and recent CPU-bypass frameworks attempt to bridge this gap, they remain trapped in proprietary ecosystems or still rely on the host CPU and coarse-grained batching to coordinate stateful telemetry and AI pipeline execution. In this paper, we propose AGP, a novel framework that promotes the GPU from a passive accelerator to a primary data-path controller, answering what changes architecturally when the GPU autonomously owns the complete packet-to-inference pipeline. By enabling GPU-native packet processing, contention-free in-GPU stateful aggregation, and a persistent mega-kernel for continuous AI inference, AGP removes the CPU from the critical path. Our evaluation demonstrates that native in-GPU packet processing sustains line-rate throughput while being over 6.1x more power-efficient. Furthermore, our integrated Intrusion Detection System (IDS) stress test eliminates the legacy CPU-GPU synchronization tax, reducing end-to-end latency by 7.9x (up to 35x p99) and accelerating whole-system inference throughput by 9.3x using only ~2% of the GPU's thread capacity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Seyed Mohammad Mehdi Mirnajafizadeh, Yiwen Hu, Rhongho Jang
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
