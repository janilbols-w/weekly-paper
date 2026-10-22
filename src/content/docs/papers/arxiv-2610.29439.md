---
title: "How Far Can Foundation Models Be Distilled for Efficient Jet Tagging?"
description: "Jet tagging is one of the most important applications of machine learning at the Large Hadron Collider."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.29439) · [PDF](https://arxiv.org/pdf/2610.29439)

## 一句话摘要

Jet tagging is one of the most important applications of machine learning at the Large Hadron Collider.

## 为什么值得关注

待编辑增强。

## 摘要原文

Jet tagging is one of the most important applications of machine learning at the Large Hadron Collider. Recent models build in more physics knowledge or rely on large-scale pretraining, but the experiments place strict limits on their inference cost. Knowledge distillation can transfer their performance to small students that are cheap to run. We ask which properties of a teacher help the student, how small a student can get and how close it can come to the state of the art. On a jet tagging benchmark, we distil six teachers that differ in architecture, symmetry and pretraining, including two foundation models, into five small students. Every teacher improves every student, and the gain depends mainly on the strength of the teacher. We then shrink our two strongest distilled students, Transformer and L-GATr-slim, in width and in depth. With 20 thousand parameters, a distilled L-GATr-slim outperforms every published jet tagger trained from scratch at a fraction of the inference cost of every teacher. Even with two thousand parameters, it matches ParT, a model with a thousand times as many parameters. We also study what the students learn from their teachers. Our benchmark of inference cost shows that students of the same size can differ by almost an order of magnitude in speed. We release the code and the weights of all trained models.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jay Agarwal, Siddharth Khare, Dhruv Kumar
- 发布：2026-10-22；更新：2026-10-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
