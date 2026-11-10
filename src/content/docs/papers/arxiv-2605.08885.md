---
title: "Compact SO(3) Equivariant Atomistic Foundation Models via Structural Pruning"
description: "SO(3) equivariant graph neural networks have become the dominant paradigm for atomistic foundation models, achieving high accuracy and data efficiency by building rotational symmetry directly into the architecture."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.08885) · [PDF](https://arxiv.org/pdf/2605.08885)

## 一句话摘要

SO(3) equivariant graph neural networks have become the dominant paradigm for atomistic foundation models, achieving high accuracy and data efficiency by building rotational symmetry directly into the architecture.

## 为什么值得关注

待编辑增强。

## 摘要原文

SO(3) equivariant graph neural networks have become the dominant paradigm for atomistic foundation models, achieving high accuracy and data efficiency by building rotational symmetry directly into the architecture. Yet the computational cost of their higher-order tensor operations creates a tough trade-off between model accuracy and inference efficiency. In this paper, we propose a structural pruning method for SO(3) equivariant atomistic foundation models to bridge this accuracy-efficiency gap. The pruning is applied along the channel and order dimensions, with each irreducible representation kept or removed as a complete block, thereby retaining SO(3) equivariance. Starting from a large checkpoint, the pruned model substantially reduces the inference cost while retaining higher accuracy than an independently trained small model. The pruned MACE-MP model outperforms the official from-scratch trained small model on 7 of 9 metrics on the Matbench Discovery leaderboard. In terms of efficiency, compressed MACE-MP and MACE-OFF models contain 1.5$\times$ to 4$\times$ fewer parameters and require 2.5$\times$ to 4$\times$ less pre-training compute than training a small model from scratch. For downstream applications, fine-tuning the pruned model reduces energy and force errors by 70.1% and 34.4% compared to training task-specific models from scratch across eight representative downstream datasets. We demonstrate that the method generalizes to other SO(3) equivariant architectures (SevenNet, eSCN) and can be combined with quantization and knowledge distillation for further gains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chen Wang, Siyu Hu, Guangming Tan, Weile Jia
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
