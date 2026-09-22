---
title: "iSDFT: Information-Proximal Self-Distillation for Continual Learning in LLMs"
description: "On-policy self-distillation fine-tuning (SDFT) learns new skills from demonstrations while reducing forgetting, but it always distils toward the full demonstration-conditioned teacher."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.24646) · [PDF](https://arxiv.org/pdf/2609.24646)

## 一句话摘要

On-policy self-distillation fine-tuning (SDFT) learns new skills from demonstrations while reducing forgetting, but it always distils toward the full demonstration-conditioned teacher.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy self-distillation fine-tuning (SDFT) learns new skills from demonstrations while reducing forgetting, but it always distils toward the full demonstration-conditioned teacher. This fixes teacher influence at the full-teacher endpoint, providing no control over how much demonstration information should be transferred at each prediction state. We introduce Information-Proximal SDFT (iSDFT), which instead treats the teacher as a budgeted source of information. At each token, iSDFT selects the distribution closest to the current student that satisfies a prescribed teacher-information constraint, yielding a closed-form exponential target with a locally determined tilt. To control cumulative drift, we further anchor the student to its frozen base policy. Across four heterogeneous LLM backbones and two specialisation tasks, iSDFT improves vanilla SDFT in 7 of 8 model-task settings and matches it in the remaining one. It also provides tighter retention on the original SDFT benchmark suite, with 73% of evaluations remaining within 0.5 points of the base model versus 52% for the strongest baseline, while achieving the largest mean improvement on all ten additional mathematics, coding, and competition-mathematics benchmarks. These results show that controlling how much and when teacher information is introduced improves specialisation while preserving broader capability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ahmed Khaled Khamis, Xiaotong Ji, Hassan Jaber, Rasul Tutunov, Matthieu Zimmer, Jun Wang, Haitham Bou-Ammar
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
