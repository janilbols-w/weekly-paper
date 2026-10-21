---
title: "OPDArena: Understanding Learning and Forgetting in On-Policy Distillation"
description: "On-policy distillation (OPD) is increasingly used for language model post-training, yet how teacher supervision shapes learning and forgetting remains unclear."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.25651) · [PDF](https://arxiv.org/pdf/2610.25651)

## 一句话摘要

On-policy distillation (OPD) is increasingly used for language model post-training, yet how teacher supervision shapes learning and forgetting remains unclear.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) is increasingly used for language model post-training, yet how teacher supervision shapes learning and forgetting remains unclear. We present OPDArena, a framework comparing supervised fine-tuning (SFT), reinforcement learning with verifiable rewards (RLVR), and OPD across five pretrained models and diverse teacher sources. It jointly evaluates mathematical learning, general capability retention, and predictive distribution changes. Teacher choice strongly shapes retention: students of RLVR-trained teachers improve on the target task while retaining prior capabilities, whereas students of SFT-trained teachers incur greater capability loss. Across post-training methods, out-of-domain (OOD) distribution change shows a more consistent positive association with forgetting than in-domain change. To understand how teacher choice affects these changes, we examine the additional information teachers provide relative to the student's pretrained model. Controlled teacher comparisons show that the task-specific preferences teachers acquire through post-training make student updates more concentrated in-domain.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuanze Xu, Tianzhu Ye, Hui Sun, Wenhui Wang, Li Dong, Furu Wei
- 发布：2026-10-20；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
