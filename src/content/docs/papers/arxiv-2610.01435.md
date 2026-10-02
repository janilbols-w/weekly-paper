---
title: "Distillation of Tabular Foundation Models into Efficient Predictors"
description: "Tabular foundation models (TFMs) achieve strong predictive performance through in-context learning, yet repeatedly conditioning on labeled data makes inference expensive."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.01435) · [PDF](https://arxiv.org/pdf/2610.01435)

## 一句话摘要

Tabular foundation models (TFMs) achieve strong predictive performance through in-context learning, yet repeatedly conditioning on labeled data makes inference expensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tabular foundation models (TFMs) achieve strong predictive performance through in-context learning, yet repeatedly conditioning on labeled data makes inference expensive. Knowledge distillation can reduce this cost by transferring their predictive ability to lightweight, dataset-specific students. However, the dependence of TFM predictions on both a labeled context and a query introduces two design questions: how to construct teacher supervision and whether expanding query coverage improves distillation. We examine these questions across two TFMs and both neural and tree-based students, and derive an effective distillation recipe. The recipe uses the full labeled training set as teacher context and trains students solely on teacher predictions for observed and synthetic queries. On TabArena, the resulting students outperform their supervised trained tuned-and-ensembled counterparts by 57-98 Elo points. Applied unchanged to TALENT, the same recipe improves matched default students on 236-258 of 300 datasets and reduces median primary error by 4.0-6.4%. The distilled students also achieve median inference speedups of 3.0-21.6 times over their teachers, offering a practical trade-off between predictive performance and repeated inference cost. Code is available at https://github.com/nums-ai/TFM_Distillation .

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Minho Jeong, Dooho Lee, Jinmo Lee, Jaemin Yoo
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/nums-ai/TFM_Distillation](https://github.com/nums-ai/TFM_Distillation)
- 阅读深度：metadata
