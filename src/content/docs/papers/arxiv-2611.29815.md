---
title: "Model Immunization Cannot Reliably Protect Models from Harmful Adaptation"
description: "Efficient fine-tuning techniques have substantially reduced the cost of adapting open-weight models, enabling malicious actors to readily fine-tune them toward harmful capabilities."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2611.29815) · [PDF](https://arxiv.org/pdf/2611.29815)

## 一句话摘要

Efficient fine-tuning techniques have substantially reduced the cost of adapting open-weight models, enabling malicious actors to readily fine-tune them toward harmful capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient fine-tuning techniques have substantially reduced the cost of adapting open-weight models, enabling malicious actors to readily fine-tune them toward harmful capabilities. In response, model immunization modifies a pretrained checkpoint to resist subsequent adaptation toward designated harmful capabilities while preserving its utility and adaptability for benign tasks. Furthermore, a few immunization methods have sought to keep their protection robust to some changes in the attacker's adaptation. However, fine-tuning offers attackers many more low-cost options, and we observe that existing methods still substantially overfit to the attacker configuration they are optimized against. Such overfitting stays hidden when immunization is evaluated under, or near, this configuration, so the reported protection may give a false sense of security. To rigorously evaluate model immunization, we conduct experiments, varying one component of this configuration at a time: the harmful data, the adaptation strategy, or the model initialization. Across four immunization methods on text-to-image generation and image classification, with additional results on language models, these variations substantially degrade the protection, and in many cases the immunized model relearns the harmful capability nearly as well as the un-immunized model. Existing immunization therefore cannot reliably protect models, leaving them vulnerable to harmful adaptation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tong Li, Chenru Wang, Chris Thomas, Shengwei An
- 发布：2026-11-22；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
