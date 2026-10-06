---
title: "MAGIC: Topology-Aware Analytic Graph Few-Shot Class-Incremental Learning"
description: "Graph few-shot class-incremental learning (GFSCIL) requires a model to continually recognize emerging classes from only a few labeled nodes while preserving previously acquired knowledge."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.04963) · [PDF](https://arxiv.org/pdf/2610.04963)

## 一句话摘要

Graph few-shot class-incremental learning (GFSCIL) requires a model to continually recognize emerging classes from only a few labeled nodes while preserving previously acquired knowledge.

## 为什么值得关注

待编辑增强。

## 摘要原文

Graph few-shot class-incremental learning (GFSCIL) requires a model to continually recognize emerging classes from only a few labeled nodes while preserving previously acquired knowledge. Beyond the catastrophic forgetting inherited from conventional graph continual learning, GFSCIL presents two distinctive challenges: extremely limited novel-class supervision causes severe overfitting, while cross-session edges---edges connecting newly arriving nodes with historical nodes---alter historical propagation neighborhoods and thereby induce representation drift. We propose MAGIC, a replay-free GFSCIL framework that combines a frozen graph representation backbone (e.g., an intrinsically parameter-free backbone such as SGC or a pretrained graph foundation model) with closed-form analytic continual learning. To alleviate novel-session overfitting, MAGIC learns a topological prior from the base graph that can characterize both homophilous and heterophilous relations, and injects this prior through Potts Markov random field inference to refine supervision for novel classes. To mitigate representation drift, MAGIC transfers previous predictions from the old representations of affected historical nodes to their updated representations through drift-aware analytic distillation. Experiments across five datasets and eight baselines demonstrate the effectiveness of MAGIC. Under the 5-shot setting, MAGIC improves Mean Accuracy and Final Accuracy by 5.48 percentage points and 9.33 percentage points on average, and reduces Performance Drop by 10.78 percentage points on average compared with the best baselines. MAGIC also shows clear advantages under the 1- and 3-shot settings, with larger gains as the number of supports increases. Moreover, MAGIC requires substantially less training time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junlin Chen, Yuhan Wang, Xuefei Wang, Xiao Wang, Ruijie Wang, Jianxin Li
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
