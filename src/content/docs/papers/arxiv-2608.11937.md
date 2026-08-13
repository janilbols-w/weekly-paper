---
title: "Distillation of Foundation Models for Time-dependent PDEs"
description: "Foundation models for time-dependent partial differential equations (PDEs) are trained on large and diverse collections of physical systems and can generalize effectively to new downstream tasks."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.11937) · [PDF](https://arxiv.org/pdf/2608.11937)

## 一句话摘要

Foundation models for time-dependent partial differential equations (PDEs) are trained on large and diverse collections of physical systems and can generalize effectively to new downstream tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Foundation models for time-dependent partial differential equations (PDEs) are trained on large and diverse collections of physical systems and can generalize effectively to new downstream tasks. After fine-tuning on only a few trajectories from a target domain, they can achieve strong accuracy in low-data regimes. However, these models are typically large and computationally intensive, limiting their usefulness as fast surrogates for numerical solvers. We propose Teacher Rollout Extension (TREX), a knowledge distillation framework that transfers the predictive capability of a pretrained foundation model into a compact and efficient student. Starting from a fine-tuned teacher, TREX augments limited downstream data by generating long synthetic trajectories through teacher rollouts, optionally with periodic noise injection. This procedure samples from the teacher-induced rollout distribution without requiring explicit knowledge of the initial-condition distribution, while exposing the student to long-horizon states and local recovery behavior around states encountered during autoregressive prediction. The student can further incorporate task-specific inductive biases, such as equivariance, that the teacher does not necessarily enforce. We evaluate TREX on multiple PDE benchmarks. The resulting students can match or surpass the teacher's accuracy while reducing the number of parameters by several orders of magnitude and achieving more than an order-of-magnitude speedup in inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Daniel Musekamp, Boshra Ariguib, Andrei Manolache, Mathias Niepert
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
