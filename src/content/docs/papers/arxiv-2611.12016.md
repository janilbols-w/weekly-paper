---
title: "Speculative Self-Distillation enables Efficient Knowledge Internalization"
description: "Many real-world applications require language models to internalize knowledge that was absent from pretraining, to incorporate continually updated facts, or to learn new domain skills."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.12016) · [PDF](https://arxiv.org/pdf/2611.12016)

## 一句话摘要

Many real-world applications require language models to internalize knowledge that was absent from pretraining, to incorporate continually updated facts, or to learn new domain skills.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many real-world applications require language models to internalize knowledge that was absent from pretraining, to incorporate continually updated facts, or to learn new domain skills. Self-distillation has emerged as a natural approach for this task. A model conditioned on the source material acts as the teacher, and an unconditioned student is trained to reproduce the teacher's behavior closed-book. We propose Speculative Self-Distillation (SSD), an efficient per-token mixed-policy method for self-distillation. The student generates each rollout by default, while the teacher intervenes only at positions where its next-token distribution substantially diverges from the student's. Unlike off-policy distillation with teacher-generated prefixes, this design keeps training rollouts close to the student's test-time behavior, while avoiding the low-signal states that fully on-policy rollouts drift into. In effect, SSD lets the teacher steer the rollout exactly where the privileged context changes the prediction. On three closed-book QA benchmarks measuring fact recall, knowledge updates, and skill acquisition, SSD nearly matches on-policy distillation while using 38-69% fewer supervised tokens and consistently outperforms off-policy distillation on the held-out test set. On a forgetting stress test, SSD retains the most general capability while also achieving the best in-domain accuracy and using less supervision than the on-policy baseline. Overall, SSD establishes a new accuracy-efficiency-forgetting Pareto frontier for self-distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shayan Talaei, Agam Bhatia, Arshia Soltani Moakhar, Jonas H\"ubotter, Amin Saberi, Azalia Mirhoseini
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
