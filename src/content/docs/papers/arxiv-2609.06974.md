---
title: "Train Overcomplete, Deploy Compact: Scaling Recovery Capacity for Structured LLM Pruning"
description: "Large language models achieve strong performance across diverse tasks, but deployment remains costly because of memory, latency, and energy demands."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06974) · [PDF](https://arxiv.org/pdf/2609.06974)

## 一句话摘要

Large language models achieve strong performance across diverse tasks, but deployment remains costly because of memory, latency, and energy demands.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models achieve strong performance across diverse tasks, but deployment remains costly because of memory, latency, and energy demands. Structured pruning reduces these costs by removing architectural components, yet its recovery stage is often limited by a mismatch between the recovery module's representational capacity and the complexity of the removed knowledge. We call this bottleneck the capacity-knowledge asymmetry and propose OverRep, an Overcomplete Reparameterization framework for structured LLM pruning. Following the principle of "train overcomplete, deploy compact", OverRep temporarily overparameterizes the recovery module during training to absorb complex knowledge distilled from the original model. After recovery, the overcomplete re-parameterization is algebraically merged into a mathematically equivalent compact module, preserving the pruned model's inference-time architecture and computational cost. OverRep further introduces an annealed activation that enables nonlinear training dynamics while converging to a linear regime for exact algebraic merging. Across three backbone families, OverRep improves retained reasoning performance over strong recovery baselines by up to 5.5 and 8.4 points at 25% and 50% pruning, respectively, while keeping memory usage and TFLOPs comparable to existing recovery methods. Our code is available at https://github.com/mmai-laboratory/OverRep.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Seungmin Oh, Donggeon Lee, Jongbin Ryu
- 发布：2026-09-07；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/mmai-laboratory/OverRep](https://github.com/mmai-laboratory/OverRep)
- 阅读深度：metadata
