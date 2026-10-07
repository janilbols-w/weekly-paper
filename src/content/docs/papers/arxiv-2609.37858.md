---
title: "Storage Is Not Strategy: State-Conditioned Support Control for LLM Unlearning"
description: "Many localized large language model (LLM) unlearning methods select a small parameter subset from a localization signal and keep it fixed during optimization."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.37858) · [PDF](https://arxiv.org/pdf/2609.37858)

## 一句话摘要

Many localized large language model (LLM) unlearning methods select a small parameter subset from a localization signal and keep it fixed during optimization.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many localized large language model (LLM) unlearning methods select a small parameter subset from a localization signal and keep it fixed during optimization. The parameters most associated with a target, however, need not be the best ones to update, and candidate interventions can change value as optimization proceeds. In a controlled experiment, a storage-localization score reaches an area under the receiver operating characteristic curve (AUROC) of 0.981, yet storage identity agrees with the better intervention on only 17/36 targets, while low-rank adaptation (LoRA) wins 35/36. We introduce Intervention Score, which ranks editable groups by the predicted effect of the actual unlearning update while accounting for collateral damage, and use it to form the static intervention-value baseline (Static-IV). We then introduce selective dynamic intervention re-ranking (DIR-R), which revisits that subset only when a calibrated probe justifies the comparison. On the Natural-TOFU dataset, our method has positive descriptive margins in 19/20 comparisons between methods and objectives, although several are near zero. On the LACUNA localization-precision benchmark, our mean terminal utility is higher in all six negative preference optimization (NPO) and SimNPO comparisons: NPO margins range from +0.431 to +0.848, and SimNPO margins range from +0.503 to +0.571. The gradient-difference (GradDiff) objective reveals substantial field dependence. Relative to Static-IV, the primary four-field GradDiff evaluation has six wins, six ties, and no losses, with mean and median paired gains of +0.165 and +0.0025. The evidence supports separating localization, initial intervention selection, and checkpoint-dependent support revision.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Qian, Ziming Hong, Chongyang Gao, Kezhen Chen, Lixu Wang
- 发布：2026-09-29；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
