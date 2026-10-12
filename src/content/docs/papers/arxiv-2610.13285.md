---
title: "BoundaryEvo: Data-Model Co-Evolution at the Capability Boundary for Long-Chain Reasoning Distillation"
description: "Distilling long-chain reasoning trajectories from large teacher models provides an effective way to improve the reasoning ability of small language models."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.13285) · [PDF](https://arxiv.org/pdf/2610.13285)

## 一句话摘要

Distilling long-chain reasoning trajectories from large teacher models provides an effective way to improve the reasoning ability of small language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distilling long-chain reasoning trajectories from large teacher models provides an effective way to improve the reasoning ability of small language models. However, existing methods typically select a fixed training set before distillation, overlooking that the usefulness of a reasoning example changes as the student evolves. This mismatch becomes especially costly when only a small number of teacher trajectories can be used for training. Besides, examples already mastered provide little new supervision, while examples far beyond the capability of student may be difficult to learn from. Training data should therefore adapt as model capability evolves, yet reliable data selection is difficult when the student is initially weak. To address these challenges, our key idea is to first establish the basic reasoning capability and then adapt the training data to the evolving capability boundary of the student. We propose BoundaryEvo, a two-stage data--model co-evolution framework. In Capability Priming, we directly distill a small set of teacher-generated long reasoning trajectories without using a separate model to judge and filter them, allowing the student to acquire an initial reasoning capability before capability-aware data selection. In Capability-Boundary Co-Evolution, we repeatedly select questions that the current student has not mastered but the expert can reliably solve, and update the training data as the student evolves. With only 1,000 training examples, BoundaryEvo consistently outperforms static and dynamic data selection baselines across 11 reasoning benchmarks, raising the original Qwen3.5-4B accuracy from 62.9 to 75.3 on IMO-AnswerBench and from 26.8 to 46.0 on AMO-Bench. The code and data will be made publicly available.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaming Su, Suorong Yang, Xudong Li, Tengchao Yang, Peng Ye
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
