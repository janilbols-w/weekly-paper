---
title: "One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation"
description: "On-policy distillation trains a language model on its own generations while a teacher scores them token by token."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.25936) · [PDF](https://arxiv.org/pdf/2608.25936)

## 一句话摘要

On-policy distillation trains a language model on its own generations while a teacher scores them token by token.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation trains a language model on its own generations while a teacher scores them token by token. It combines the dense supervision of imitation learning with the on-policy sampling of reinforcement learning. But it requires a second, larger model to act as teacher. On-Policy Self-Distillation (OPSD) removes that cost. The teacher is the model itself, conditioned on privileged information the student will not have at test time, such as a reference solution, a plan, or environment feedback. The teacher is no stronger than the student, only better informed. Early results were promising, with accuracy comparable to reinforcement learning at a fraction of the generated tokens. But the same asymmetry that produces the signal also biases it. One failure mode now dominates the field: collapse, the progressive narrowing of the set of reasoning paths the model can produce. Collapse is not specific to OPSD, though privileged information aggravates it. This review treats collapse as a symptom governed by three levers: (i) where the signal is applied, that is, how tokens are weighted; (ii) what the teacher is shown, that is, the nature of the privileged information; and (iii) when the signal changes, that is, the teacher's dynamics and the decay of guidance. We restrict our scope to mathematical reasoning, where the method originated and where its failure modes are best documented. We report no new experiments. The contribution is structural: a shared vocabulary for phenomena named differently across papers, and a clear line between what is settled and what is still disputed.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Justin Robert, Raheel Qader
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
