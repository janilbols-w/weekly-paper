---
title: "Bernoulli On-Policy Distillation: Don't Ignore High-Confidence Student Tokens"
description: "On-policy distillation (OPD) trains a student language model on its own trajectories using token-level supervision from a stronger teacher."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.02093) · [PDF](https://arxiv.org/pdf/2611.02093)

## 一句话摘要

On-policy distillation (OPD) trains a student language model on its own trajectories using token-level supervision from a stronger teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) trains a student language model on its own trajectories using token-level supervision from a stronger teacher. We show that standard sampled reverse-KL OPD systematically suppresses updates to high-confidence tokens, such that their weak gradient contribution does not necessarily imply weak or uninformative teacher supervision. We introduce Bernoulli On-Policy Distillation (Bernoulli OPD), which directly matches the teacher and student probabilities for that token. This yields a bounded probability space correction that preserves teacher-student disagreement while avoiding the additional confidence-dependent suppression induced by vanilla OPD. Fixed-rollout analyses show that Bernoulli OPD substantially restores optimization signal to high-confidence tokens while remaining sensitive to teacher-student disagreement. We further analyze the resulting model behavior through confidence distributions, answer calibration, policy movement, and training dynamics, showing that Bernoulli OPD's gains cannot be explained simply by longer reasoning, larger optimization steps, or more uniform imitation of the teacher. Code is available at https://github.com/duterscmy/Bernoulli-OPD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Mingyu Cao, Yaokai Jin, Shiwei Liu, Lu Yi
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/duterscmy/Bernoulli-OPD](https://github.com/duterscmy/Bernoulli-OPD)
- 阅读深度：metadata
