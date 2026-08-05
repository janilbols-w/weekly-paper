---
title: "Cloud to Edge: Benchmarking LLM Inference On Hardware-Accelerated Single-Board Computers"
description: "Large language models (LLMs) are becoming increasingly capable at small parameter scales."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.24785) · [PDF](https://arxiv.org/pdf/2604.24785)

## 一句话摘要

Large language models (LLMs) are becoming increasingly capable at small parameter scales.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are becoming increasingly capable at small parameter scales. At the same time, conventional cloud-centric deployment introduces challenges around data privacy, latency, and cost that are acute in operational technology and defence environments. Advances in model distillation, quantisation, and affordable edge accelerators now make local LLM inference on single-board computers feasible, but the high dimensionality of the configuration space makes identifying optimal deployments difficult without structured evaluation. Existing LLM-specific edge benchmarking efforts rely on CPU-only inference, poor coverage of genuine single-board computers, and generic evaluation tasks that lack multi-dimensional assessment of hardware effectiveness. This paper proposes a multi-dimensional benchmarking methodology that jointly evaluates inference performance and hardware efficiency across four IoT-suitable edge platform configurations testing single-board computers with the latest available hardware accelerators. Our results reveal the benefits of using hardware accelerators such as NPUs and GPUs, along with multi-dimensional evaluations quantifying the trade-offs between power efficiency, physical device size and token throughput; offering practical guidance for deploying generative AI in privacy-sensitive and connectivity-limited environments such as unmanned vehicles and portable, ruggedised operations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Harri Renney, Fouad Trad, Michael Mattarock, Jayden Evetts, Zena Wood
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
