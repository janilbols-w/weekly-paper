---
title: "RAPID-LLM: Resilience-Aware Performance analysis of Infrastructure for Distributed LLM Training and Inference"
description: "RAPID-LLM is a unified performance modeling framework for distributed large language model (LLM) training and inference on GPU clusters, without relying on deployment-specific traces or expensive cycle-level simulation for exploration."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2512.19606) · [PDF](https://arxiv.org/pdf/2512.19606)

## 一句话摘要

RAPID-LLM is a unified performance modeling framework for distributed large language model (LLM) training and inference on GPU clusters, without relying on deployment-specific traces or expensive cycle-level simulation for exploration.

## 为什么值得关注

待编辑增强。

## 摘要原文

RAPID-LLM is a unified performance modeling framework for distributed large language model (LLM) training and inference on GPU clusters, without relying on deployment-specific traces or expensive cycle-level simulation for exploration. From a workload and hardware specification, it builds hardware-aware operator-level execution models that capture tiling, memory-hierarchy effects, communication, and memory feasibility under hybrid parallelism. Its backend simulates explicit multidimensional interconnects with congestion-aware routing and support for degraded and failed links, enabling scalable what-if analysis across topology, mapping, and hardware design choices. Across 124 evaluation cases spanning inference and dense, fully sharded, and mixture-of-experts training on A100 and H100 GPUs, RAPID-LLM achieves an overall mean absolute percentage error (MAPE) of 10.0\%. Its network predictions stay within 8\% of ns-3 on representative communication patterns. Case studies demonstrate how RAPID-LLM enables fast, systematic sweeps over hybrid-parallel configurations, quantifies sensitivity to link faults under realistic routing and congestion, and evaluates hypothetical GPU design variants including 3D-stacked HBM-on-GPU scenarios.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：George Karfakis, Lime Yao, Binglu Chen, Faraz Tahmasebi, Saptarshi Mitra, Tianyue Pan, Hyoukjun Kwon, Puneet Gupta
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
