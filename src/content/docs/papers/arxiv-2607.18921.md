---
title: "Circuit Claims Depend on What Is Extracted and How It Is Compared"
description: "Circuit extraction identifies model components whose presence preserves a target behavior under ablation, but preserving behavior does not single out one circuit."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2607.18921) · [PDF](https://arxiv.org/pdf/2607.18921)

## 一句话摘要

Circuit extraction identifies model components whose presence preserves a target behavior under ablation, but preserving behavior does not single out one circuit.

## 为什么值得关注

待编辑增强。

## 摘要原文

Circuit extraction identifies model components whose presence preserves a target behavior under ablation, but preserving behavior does not single out one circuit. We study this in a synthetic Lean tactic-prediction benchmark with fixed proof rules and randomized surface form. Across dense and weight-sparse checkpoints of the same transformer, evaluated on atomic and compositional proofs, we vary which extracted object is reported: a compact prediction-preserving circuit, a broader graph retaining surrounding read, write, and routing structure, or a subgraph extracted with a post-ablation loss budget. First, overlap between groups of component-to-component connections is low, sometimes close to a random baseline. Overlap is much higher for selected attention-head sets under deterministic selection, but falls sharply when selection among equally scored heads is randomized. Second, the normalized graph-size ranking of conditions that differ in which supervised checkpoint initializes reinforcement learning (RL) agrees between repeated extractions of the compact circuit and between joint and separate query/key representations of each of the other two graphs. For the loss-budgeted graph, query/key ordering agreement persists through the budget sweep. Finally, across those same conditions, the largest exact-match accuracy gains from RL on compositional proofs come with the largest proportion of components in the compositional circuit that lie outside the corresponding atomic circuits. Ablating these additional components in the sparse RL model reduces compositional accuracy while largely preserving accuracy on the corresponding atomic tasks. A circuit-level claim therefore requires specifying which circuit is reported and how it is extracted and compared; behavior alone does not determine its interpretation. We distill these requirements into a reporting practice for circuit-extraction studies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yang Sheng, Jie Fu
- 发布：2026-10-16；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
