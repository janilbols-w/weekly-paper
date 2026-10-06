---
title: "Scaling Down the Scaling Laws: Parameter Efficiency and Compute-Optimal Training in Resource-Constrained Large Language Models"
description: "Large language models (LLMs) have achieved substantial performance gains through increases in model size, training data, and computational resources."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.06387) · [PDF](https://arxiv.org/pdf/2610.06387)

## 一句话摘要

Large language models (LLMs) have achieved substantial performance gains through increases in model size, training data, and computational resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have achieved substantial performance gains through increases in model size, training data, and computational resources. However, traditional scaling approaches produce diminishing returns, rising financial and environmental costs, and barriers to participation for researchers operating outside large industrial laboratories. This review examines the evolution of LLM scaling theory from empirical scaling laws to compute-optimal training, with particular emphasis on parameter efficiency, token utilization, data efficiency, and resource-constrained environments. Foundational work on scaling laws is synthesized alongside later research on compute-optimal training, data pruning, efficient architectures, quantization, low-rank adaptation, and edge-oriented optimization. The literature indicates a shift from scale maximization toward more deliberate allocation of parameters, tokens, compute, and hardware resources. At the same time, important empirical, theoretical, and methodological gaps remain regarding whether scaling principles established on enterprise-grade infrastructure generalize to smaller models and constrained computing environments. This review organizes these developments into a unified framework for resource-efficient LLM training and argues that future progress should evaluate efficiency not solely through model performance, but through the relationship among performance, parameter count, computational cost, token allocation, and hardware constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joe Dwyer
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
