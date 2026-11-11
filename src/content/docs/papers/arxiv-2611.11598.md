---
title: "Perturbing Inputs Improves Pretraining Distillation"
description: "Knowledge distillation trains a student language model to match a teacher's predictions on the training text."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.11598) · [PDF](https://arxiv.org/pdf/2611.11598)

## 一句话摘要

Knowledge distillation trains a student language model to match a teacher's predictions on the training text.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation trains a student language model to match a teacher's predictions on the training text. We ask whether learning the teacher's behavior beyond the training text can further improve the student. We investigate this using three input perturbations: additive token noise, blending two documents, and blending neighboring tokens. Specifically, for an early part of pretraining we perturb the inputs and train the student to match the teacher on them, and we spend the rest of the same token budget on ordinary distillation. When pretraining from scratch, the best method improves on standard distillation at both scales we tried, by 0.025 nats at 135M parameters and by 0.020 nats at 0.5B (mean of three seeds). At 135M this is 1.45 times the gain that distillation itself provides over next-token training. We also observe promising downstream transfer: at 0.5B, the best variant improves average zero-shot accuracy by about one percentage point across seven tasks. It also retains its validation-loss advantage after low-bit weight quantization. We also test a data-limited setting in which training data must be reused, and find that the gains persist. Finally, ablations suggest that, for additive noise, perturbing the teacher's inputs contributes most of the gain, while perturbing only the student's inputs yields much less.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ziyang Cai, Yihe Dong, Dimitris Papailiopoulos, Shivam Garg
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
