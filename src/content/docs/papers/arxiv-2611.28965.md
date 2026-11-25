---
title: "MolReJev: Decision Models Are In-Context Molecular Predictors"
description: "Molecular prediction helps prioritize compounds for screening."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.28965) · [PDF](https://arxiv.org/pdf/2611.28965)

## 一句话摘要

Molecular prediction helps prioritize compounds for screening.

## 为什么值得关注

待编辑增强。

## 摘要原文

Molecular prediction helps prioritize compounds for screening. Specialized predictors are trained for a fixed set of tasks, limiting cross-task generalization. Language models can condition on task descriptions and have recently shown promise in molecular prediction. However, generating answers token by token adds inference cost, and general-purpose models often lack task-specific molecular knowledge. We thus propose MolReJev, which combines Jev-style candidate scoring with in-context learning (ICL) on a language model. MolReJev retrieves similar labeled examples from existing task data and scores candidate labels jointly in one forward pass. ICL improves predictions from the released general-purpose Kev checkpoint and the separately trained MolReJev. For the trained model, gains span all evaluation groups, including held-out tasks, and extend to compounds absent from training. MolReJev generally outperforms MolecularGPT on matched evaluations and nearest-neighbor prediction with the same examples. With four examples, MolReJev and a trained text baseline achieve similar ROC-AUC, with higher measured throughput for MolReJev. These results show that decision models can serve as in-context molecular predictors for compounds, drug pairs, and reactions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaiyuan Lu, Jiatong Li, Yatao Bian
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
