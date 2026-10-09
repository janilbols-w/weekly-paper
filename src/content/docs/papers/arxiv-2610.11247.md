---
title: "Why On-Policy Distillation Sometimes Fails: Vanishing Learning Signals"
description: "On-policy distillation (OPD) enables effective capability transfer between language models, yet the mechanisms underlying its failures are not fully understood."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.11247) · [PDF](https://arxiv.org/pdf/2610.11247)

## 一句话摘要

On-policy distillation (OPD) enables effective capability transfer between language models, yet the mechanisms underlying its failures are not fully understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation (OPD) enables effective capability transfer between language models, yet the mechanisms underlying its failures are not fully understood. Across code generation and mathematical reasoning, OPD with larger-scale teachers exhibits early loss plateaus, with an average final loss reduction of 25.1% after 200 updates, compared with 96.2% for self-RL teachers, obtained by further reinforcement learning (RL) training of the initial student. To understand this difference, we analyze OPD as an idealized continuous-time dynamical system in the small-learning-rate limit. Our training-log diagnostics associate these plateaus with an early decline in a gradient-based learning-signal proxy while substantial loss remains; these measurements do not establish why the underlying gradient weakens. We further prove a local recovery guarantee for teachers sufficiently close to the initial student in a shared parameterization under regularity conditions, offering a conditional explanation for the success of self-RL teachers in our experiments. Across runs with and without loss plateaus, we observe small relative parameter changes (0.025-0.098%) and high similarity between the student's representations before and after OPD (linear CKA $>0.98$ across layers). These observations suggest that limited representation adaptation may contribute to learning-signal collapse, a hypothesis that remains to be tested. Code is available at https://github.com/leizhao7/opd-learning-signals.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Lei Zhao, Qichao Zhao, Bowen Zuo, Qishi Zhan
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/leizhao7/opd-learning-signals](https://github.com/leizhao7/opd-learning-signals)
- 阅读深度：metadata
