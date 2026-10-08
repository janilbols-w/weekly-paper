---
title: "CM-DPO: Constraint-Margin Direct Preference Optimization for LLM Planning"
description: "Direct Preference Optimization (DPO) treats all constraint violations equally: a $1 budget overshoot and a $1,000 overshoot induce the same training signal."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.09219) · [PDF](https://arxiv.org/pdf/2610.09219)

## 一句话摘要

Direct Preference Optimization (DPO) treats all constraint violations equally: a $1 budget overshoot and a $1,000 overshoot induce the same training signal.

## 为什么值得关注

待编辑增强。

## 摘要原文

Direct Preference Optimization (DPO) treats all constraint violations equally: a $1 budget overshoot and a $1,000 overshoot induce the same training signal. It is also susceptible to length and style bias when preference pairs come from different model families. We introduce Constraint-Margin DPO (CM-DPO), which replaces DPO's binary preference signal with a continuous margin derived from a deterministic symbolic verifier and scaled by violation severity. Hard and soft constraints are separated through a lexicographic objective, ensuring hard constraints are never traded off against preferences. To supply CM-DPO with bias-reduced training pairs, we generate preference data through procedurally generated constraint profiles (DCCG) and minimal-edit distillation from a reasoning teacher (RT-MED), within a framework we call SynPlan-R. On TravelPlanner, NaturalPlan, and out-of-distribution PlanBench, an 8B model fine-tuned with CM-DPO achieves 89.2% pass rate and 93.4% solve rate, matching multi-agent systems at 13x lower latency while outperforming GPT-4o on unseen Blocksworld by 9.2 points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Rabimba Karanjai, Qun Gu, Hemanth Hegadehalli Madhavarao, Wenhuan Sun, Xiaojiao Yu, Suryabhan Singh Hada, Libin N. George, Uma Kona, Richard Williamson, Linsey Pang, Prakhar Mehrotra
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
