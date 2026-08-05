---
title: "EdgeCoInfer: Hierarchical Collaborative Inference for On-Device Multimodal Large Models"
description: "To deliver ubiquitous intelligence, modern mobile applications increasingly execute concurrent Multimodal Large Language Models (MLLMs) on edge devices, presenting severe challenges under multi-task concurrency and tight resource constraints."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.17143) · [PDF](https://arxiv.org/pdf/2607.17143)

## 一句话摘要

To deliver ubiquitous intelligence, modern mobile applications increasingly execute concurrent Multimodal Large Language Models (MLLMs) on edge devices, presenting severe challenges under multi-task concurrency and tight resource constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

To deliver ubiquitous intelligence, modern mobile applications increasingly execute concurrent Multimodal Large Language Models (MLLMs) on edge devices, presenting severe challenges under multi-task concurrency and tight resource constraints. To address this, we propose EdgeCoInfer, a hierarchical collaborative inference framework enabling efficient on-device MLLM inference through coarse-to-fine orchestration. Coarsely, EdgeCoInfer decomposes MLLMs into functional modules for inter-task sharing, avoiding redundant model loading. Finely, it partitions models at the neural network layer level and distributes segments across devices and servers. We jointly optimize layer partitioning, module sharing, and resource allocation under tight constraints. To tackle the non-differentiable combinatorial explosion, we propose a Hybrid Evolutionary Hierarchical Reinforcement Learning (HE-HRL) framework. HE-HRL synchronizes a gradient-free genetic algorithm for discrete partitioning and sharing decisions with a gradient-based soft actor-critic agent for continuous resource refinement. We further embed a constructive cut-step decoder with pre-act pruning and a two-phase curriculum to improve feasibility and accelerate convergence. Experimental results show that EdgeCoInfer breaks the edge memory wall and prevents catastrophic out-of-memory and task failures under high concurrency, reducing memory demand by 53.53\% and system cost by 59.86\% compared to existing methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lin Tan, Songtao Guo, Mingyan Li, David K. Y. Yau
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
