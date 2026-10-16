---
title: "MCCL: Measurement-based Collective Communication Library"
description: "Collective communication is a critical performance bottleneck in large-scale distributed training."
---

**评分：49/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](http://arxiv.org/abs/2610.17091v1) · [PDF](https://arxiv.org/pdf/2610.17091v1)

## 一句话摘要

Collective communication is a critical performance bottleneck in large-scale distributed training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collective communication is a critical performance bottleneck in large-scale distributed training. Existing libraries and synthesis frameworks compute open-loop schedules once, assuming a static topology and peak link capacities. In production, however, persistent gray failures can silently degrade link throughput and latency for hours, causing pre-computed schedules to lose much of their efficiency during execution. In this paper, we present Measurement-based Collective Communication Library (MCCL), a collective communication library that closes the loop between runtime network measurement and dynamic schedule synthesis. MCCL passively measures GPU-to-GPU throughput, detects persistent degradation, re-synthesizes the affected communication-intensive schedules with warm-started synthesizers, and hot-swaps them without interrupting training. We validate the complete loop on a multi-node hardware prototype and use simulations to evaluate cluster-scale scenarios. In our experiments, MCCL incurs negligible overhead (<2%) while maintaining high measurement accuracy (<1.2% error) and low schedule hot-swap time (about 12 ms). Notably, under gray failures, MCCL reduces training time by up to 4.99x over static schedules on simulated training workloads for state-of-the-art LLMs such as Llama and DeepSeek.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Michele Ferrero, Gabriele Castellano, Paolo Medagliani, Sebastien Martin, Roberto Morabito, Massimo Gallo
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
