---
title: "Non-intrusive appliance state detection in unseen homes using classical machine learning"
description: "Non-intrusive load monitoring (NILM) infers, from the aggregate signal of a single smart meter, when each appliance in a home is ON or OFF, offering significant potential to enhance energy efficiency."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.00920) · [PDF](https://arxiv.org/pdf/2611.00920)

## 一句话摘要

Non-intrusive load monitoring (NILM) infers, from the aggregate signal of a single smart meter, when each appliance in a home is ON or OFF, offering significant potential to enhance energy efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Non-intrusive load monitoring (NILM) infers, from the aggregate signal of a single smart meter, when each appliance in a home is ON or OFF, offering significant potential to enhance energy efficiency. Classical machine-learning detectors report F1 scores (the harmonic mean of precision and recall) from 0.53 to 0.98, but the causes of this spread are unseparated, so it is unclear which design choices matter. Real-world deployments, however, require detectors that work in houses never seen during training, whereas most studies test on houses used for training. To address this challenge, we propose a factorial analysis of variance design that separates the effects of classifier, feature set and class-imbalance strategy across five appliances (270 configurations), and a leave-house-out protocol with house-grouped model selection. Unlike studies that vary one factor at a time or pool houses, the approach attributes performance to each factor and measures it on unseen homes. Extensive experiments on REFIT, a public dataset of 20 UK households, show that the appliance explains 38 percent of F1 variance, the feature set 13 percent, the classifier 8 percent and the imbalance strategy 2 percent. Pooled testing overstates support-weighted F1 (0.548 versus 0.447 in unseen houses), class weighting gains grow from 32 percent to 69 percent, and feature engineering gives the same 52 percent gain in both protocols. House-grouped selection raises F1 for three of five appliances, by up to 0.110, and a convolutional neural network scores 0.450 (0.496 calibrated) against 0.447 for classical models. The findings guide appliance-level monitoring in smart-metering and energy-management systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zablon Ombiro
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
