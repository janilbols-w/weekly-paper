---
title: "Trajectory Replay: Continuous-Time Mixture Transport for Lifelong Generative Models"
description: "Adapting pre-trained continuous-time generative models to sequentially incoming data without forgetting earlier tasks is a central challenge in lifelong learning."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.26749) · [PDF](https://arxiv.org/pdf/2610.26749)

## 一句话摘要

Adapting pre-trained continuous-time generative models to sequentially incoming data without forgetting earlier tasks is a central challenge in lifelong learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Adapting pre-trained continuous-time generative models to sequentially incoming data without forgetting earlier tasks is a central challenge in lifelong learning. A leading strategy, generative replay, uses a generative model trained on historical tasks to augment its own continual update with synthetic samples from experience. However, it requires full trajectory simulations at every training step, which accumulate discretization errors and can degrade the replayed historical distribution. Here, we propose trajectory replay, which bypasses sample generation by training an updated velocity field to match both a frozen historical velocity along its trajectories and the incoming task's velocity field, weighted by a stability-plasticity coefficient. Through the lens of continuous-time transport, we show the resulting optimum averages the two task velocities by their respective densities and generates the mixture of their probability paths. Combined with mean velocity distillation, trajectory replay accesses historical trajectories using only a few network evaluations per continual update. Empirically, it outperforms generative replay and distillation baselines on class-incremental image generation. In two biological case studies, trajectory replay extends generative perturbation models to new contexts and experimental batches across two data modalities while preserving treatment-effect prediction.

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

- 作者：Alessandro Palma, Charles Jones, Tristan Cinquin, Fabian J. Theis, Frederik Wenkel
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
