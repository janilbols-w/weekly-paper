---
title: "Learning When to Continue and When to Stop: Termination-Aware OPSD"
description: "On-Policy Self-Distillation (OPSD) improves language model reasoning by distilling from a frozen teacher initialized identically to the student and conditioned on privileged information."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.19925) · [PDF](https://arxiv.org/pdf/2611.19925)

## 一句话摘要

On-Policy Self-Distillation (OPSD) improves language model reasoning by distilling from a frozen teacher initialized identically to the student and conditioned on privileged information.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-Policy Self-Distillation (OPSD) improves language model reasoning by distilling from a frozen teacher initialized identically to the student and conditioned on privileged information. However, we identify an underexplored termination mismatch in OPSD: the student fails to reliably learn when to continue and when to stop. This mismatch manifests in two opposing failure modes-premature termination, where reasoning stops before sufficient progress is made, and repetition-driven over-generation, where the model continues generating after reasoning has stalled. Our analysis shows that the teacher-student discrepancy on EOS grows during OPSD training, while length-capped trajectories are frequently dominated by unproductive repetition. To address this issue, we propose TA-OPSD (Termination-Aware On-Policy Self-Distillation), which augments the original OPSD objective with two targeted objectives. Stop/Continue Distillation addresses premature termination by explicitly aligning the teacher and student on whether reasoning should continue, while Repetition-Aware Unlikelihood Training addresses repetition-driven over-generation by discouraging repetitive continuations in the student's failed trajectories. The resulting objective improves termination behavior from complementary directions: continuing when further reasoning is needed and stopping when reasoning becomes unproductive. Experiments on mathematical reasoning tasks with Qwen3 (1.7B/4B/8B) show that TA-OPSD consistently outperforms OPSD and other baselines across all three model scales. Beyond the performance gains, ablation and behavioral analyses show that the two proposed objectives effectively mitigate their corresponding termination failures, reducing both premature termination and repetition-driven over-generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Chaoqun He, Wannian Yi, Changyi Sun, Chaojun Xiao, Lijie Wen
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
