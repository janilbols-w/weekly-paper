---
title: "Mitigating Fabrication in Multi-Stage LLM Pipelines for Hiring: An Empirical Evaluation of Prompt Guardrails and Human-in-the-Loop Checkpoints"
description: "Multi-stage LLM hiring pipelines (resume improvement, interview question generation, answer feedback) can fabricate credentials, inflate qualifiers, and invent experience."
---

**评分：40/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.26171) · [PDF](https://arxiv.org/pdf/2608.26171)

## 一句话摘要

Multi-stage LLM hiring pipelines (resume improvement, interview question generation, answer feedback) can fabricate credentials, inflate qualifiers, and invent experience.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-stage LLM hiring pipelines (resume improvement, interview question generation, answer feedback) can fabricate credentials, inflate qualifiers, and invent experience. We evaluate two mitigations, prompt guardrails and human-in-the-loop (HITL) checkpoints, against a fully automated baseline. In a controlled experiment (10 synthetic resumes x 2 job descriptions x 3 repetitions x 3 conditions; 180 runs), the baseline (C1) produced at least one unsupported claim in 96.7% of outputs (mean 6.80 findings/output). Prompt guardrails (C2) reduced finding density by 86% (6.80 to 0.92/output), but 50.0% of outputs still contained a fabrication, showing prompt-level mitigation alone is insufficient. A human checkpoint after resume improvement (C3) eliminated all identity fabrications, reduced finding density by 59% (6.88 to 2.82/output), reduced item-level fabrication from 96.7% to 75.0% (p=.022), and cut capture of JD-embedded trap requirements from 47% to 2% (vs. 5% under the guardrail). An exploratory analysis of multi-specialty resumes shows contamination rising monotonically with domain distance between specialties, suggesting career changers are especially exposed. The reviewer in this study caught all flagrant fabrications, but subtle qualifier drops and plausible new claims survived review roughly half the time (54.5% removal). Neither mitigation degraded the deliverable: claim retention exceeded 99% under both. The interventions are complementary: the guardrail eliminates unprompted additions and qualifier inflation cheaply, while the checkpoint gives near-categorical guarantees against the most severe failures, invented identities and JD-baited claims. These results support a layered architecture combining guardrails with a human checkpoint. A supplementary run with a newer-generation model (90.0% baseline fabrication rate) suggests the problem is not resolved by model progress alone.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hiroko Takano
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
