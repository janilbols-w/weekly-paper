---
title: "Checkpoint Selection and Evaluation in EEG Emotion Recognition"
description: "Checkpoint selection can improve an electroencephalography (EEG) emotion-recognition score without improving performance on other trials."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2607.27655) · [PDF](https://arxiv.org/pdf/2607.27655)

## 一句话摘要

Checkpoint selection can improve an electroencephalography (EEG) emotion-recognition score without improving performance on other trials.

## 为什么值得关注

待编辑增强。

## 摘要原文

Checkpoint selection can improve an electroencephalography (EEG) emotion-recognition score without improving performance on other trials. We compared selection and scoring on disjoint trial pools along fixed training trajectories. A same-session SEED study comprised 300 trajectories from 15 participants, two models and five trial-role rotations. Another 276 trajectories extended the comparison to separate training, validation and target sessions in SEED, SEED-IV and SEED-V, with 15, 15 and 16 participants, respectively. Increasing the candidate set from five to 80 checkpoints raised the same-session dynamical graph convolutional neural network (DGCNN) selection-pool score by 6.24 percentage points, while the other-pool change was -1.24 (descriptive 95% participant-bootstrap interval -2.67 to 0.26). Under the cross-session design, DGCNN retained gains of 4.47 [1.79, 7.25], 4.27 [2.00, 6.53] and 2.75 [0.79, 4.78] points across the three datasets. Multilayer perceptron results varied across datasets. Common-time-range analysis and trial-level scoring supported the respective patterns. Both target pools supplied labels for symmetric checkpoint selection; these results concern retention across trials, not evaluation without target labels. Complete policy curves and executable reconstruction support reporting selected-score improvements alongside performance on other trials, rather than assuming a universal penalty for checkpoint search.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hanting Suo, Hongxun Wang, Yuwen Li
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
