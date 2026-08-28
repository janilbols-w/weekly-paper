---
title: "DIAG: Diagnostic Iterative Alignment and Generation for Data-Efficient Mathematical Preference Distillation"
description: "Iterative preference optimization is essential for aligning Large Language Models on mathematical reasoning tasks, yet its efficiency is often throttled by signal scarcity: as the model improves, static problem sets become increasingly mismatched to the model's evolving competence, producing rollouts that are either too easy or too hard and therefore non-inf"
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.22806) · [PDF](https://arxiv.org/pdf/2608.22806)

## 一句话摘要

Iterative preference optimization is essential for aligning Large Language Models on mathematical reasoning tasks, yet its efficiency is often throttled by signal scarcity: as the model improves, static problem sets become increasingly mismatched to the model's evolving competence, producing rollouts that are either too easy or too hard and therefore non-inf

## 为什么值得关注

待编辑增强。

## 摘要原文

Iterative preference optimization is essential for aligning Large Language Models on mathematical reasoning tasks, yet its efficiency is often throttled by signal scarcity: as the model improves, static problem sets become increasingly mismatched to the model's evolving competence, producing rollouts that are either too easy or too hard and therefore non-informative, which leads to a scarcity of valid preference pairs. We propose DIAG, a Diagnostic Iterative Alignment and Generation framework that adaptively reshapes the practice distribution to increase informative supervision and focus training near the student's current competence boundary. DIAG consists of two phases: (1) diagnosing valid preference-pair yield to calibrate the exploration-exploitation trade-off and allocate topic quotas via an Empirical Bayes shrinkage estimator, thereby prioritizing high-yield concepts; and (2) generating targeted practice, where a teacher synthesizes variants from the student's failure traces. We further provide a theoretical view interpreting DIAG as a teacher-mediated approximation to KL-regularized reweighting of the practice distribution toward the student's competence boundary, where valid preference-pair yield is maximized. Experiments show that DIAG boosts yield across iterations and delivers stronger reasoning performance under an iso-effective training budget, demonstrating that it can distill more informative preference supervision for mathematical reasoning.

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

- 作者：Guhan Chen, Songtao Tian, Bohan Li, Hejin Wang, YeXin Xie, Zixiong Yu
- 发布：2026-08-24；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
