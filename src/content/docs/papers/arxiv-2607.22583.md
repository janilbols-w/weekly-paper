---
title: "Multi-Objective Structured Pruning of LLMs for Latency and Model Size Optimization"
description: "Large Language Models (LLMs) have achieved widespread adoption because of their strong reasoning and query-response capabilities."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.22583) · [PDF](https://arxiv.org/pdf/2607.22583)

## 一句话摘要

Large Language Models (LLMs) have achieved widespread adoption because of their strong reasoning and query-response capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have achieved widespread adoption because of their strong reasoning and query-response capabilities. However, deploying them in embedded and edge computing environments remains challenging because of strict latency, memory, and energy constraints. Their large parameter counts and computational demands hinder efficient execution on resource-constrained platforms. Although model pruning has emerged as a viable solution for reducing scale while preserving performance, jointly optimizing layers, attention heads, and Multi-Layer Perceptron (MLP) dimensions remains highly complex. Exhaustively exploring this combined design space is computationally expensive and often leads to local optima or unstable configurations. To address these limitations, we propose a hardware-aware, multi-objective structured pruning framework. The proposed two-stage method explicitly targets latency and model size for efficient deployment on edge devices. In the coarse-grained stage, multi-objective depth pruning removes entire attention and MLP blocks to reduce computational load and memory usage. In the subsequent fine-grained stage, Parallel Bayesian Optimization (PBO) searches for the optimal layer-wise pruning ratios for pruning under latency constraints, while importance-based strategies rank the specific components to be pruned within each layer's allocated budget. Experimental results show that our approach reduces model complexity with minimal impact on commonsense reasoning tasks and zero-shot performance. Our method achieves a favorable trade-off among accuracy, latency, and model size, making it suitable for edge deployment. Across multiple LLMs at 37.5% and 50% pruning ratios, the proposed approach achieves better performance on commonsense reasoning tasks than existing methods while significantly reducing inference cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Junaid Ali, Smail Niar, El-Ghazali Talbi
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
