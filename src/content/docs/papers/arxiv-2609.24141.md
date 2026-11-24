---
title: "SAVOR: Score Once, Learn Deeper in On-Policy Distillation"
description: "On-policy distillation (OPD) trains a student on its own samples with token-level scores from a stronger teacher, and it effectively transfers reasoning ability to small language models."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.24141) · [PDF](https://arxiv.org/pdf/2609.24141)

## 一句话摘要

On-policy distillation (OPD) trains a student on its own samples with token-level scores from a stronger teacher, and it effectively transfers reasoning ability to small language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) trains a student on its own samples with token-level scores from a stronger teacher, and it effectively transfers reasoning ability to small language models. Each training step pays for student rollouts and teacher scoring, yet common OPD configurations make a single pass over the scored batch and then discard it. We observe that reusing the batch alone is not enough, because no single fixed teacher target suits every batch. In our runs, a fixed $\alpha$ of 0.3 exceeds a KL envelope at every training step, while 0.2 leaves over a quarter of it unused. We propose SAVOR, which selects for each batch the strongest teacher target inside the KL envelope, freezes the scored batch, and reuses it for a fixed number of student updates without further teacher calls. On five math reasoning benchmarks with a 1.7B student and a 30B-A3B teacher, SAVOR raises macro accuracy over TOP-D from 15.41 to 17.78 with two passes and to 19.36 with three passes at about the same teacher budget. With three passes, SAVOR nearly matches the final accuracy of TOP-D after one third of training while using 67.2% fewer teacher-scored tokens. These results suggest budgeting reuse depth explicitly in OPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Keye Zheng, Hanyu Li, Zhan Cheng, Yuan Gao
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
