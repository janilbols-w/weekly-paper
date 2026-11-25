---
title: "Damped Atomic Wave Integration Neurons (DAWIN): A Universal Primitive for Continuous-Time Spatiotemporal Learning"
description: "Conventional artificial neurons separate spatial feature aggregation from continuous physical time, limiting their ability to model irregular observations."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.30025) · [PDF](https://arxiv.org/pdf/2611.30025)

## 一句话摘要

Conventional artificial neurons separate spatial feature aggregation from continuous physical time, limiting their ability to model irregular observations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Conventional artificial neurons separate spatial feature aggregation from continuous physical time, limiting their ability to model irregular observations. We introduce the Damped Atomic Wave Integration Neuron (DAWIN), a continuous-time primitive for replacing standard neural layers in MLPs, Transformers, and graph neural networks. DAWIN couples spatial projection with elapsed-time-dependent wave excitation and integrates it into a local complex state through closed-form damped evolution, avoiding numerical differential equation solvers. We show that DAWIN generalizes static sinusoidal and memoryless wave neurons on interval-augmented inputs, derive closed-form gradients, and establish bounded-input bounded-output stability for positive damping and sampling intervals bounded away from zero. An associative Triton prefix-scan implementation, DAWINLinear, uses FP32 accumulation and achieves O(log L) parallel depth for sequence length L. Across 11 parameter-matched tasks covering irregular oscillators, MuJoCo dynamics, pedestrian trajectories, and PhysioNet 2012 clinical sequences, DAWIN outperforms Neural CDE on 9 tasks and ReLU-MLP on 8. It achieves the lowest error on dense clinical dynamics (0.9531 NRMSE, winning across all 10 seeds) and ties for the best mortality prediction (0.9993 AUROC). Shuffling elapsed intervals increases error by 58.2%-77.4% on selected dynamics tasks, versus 0.06% on a time-irrelevant control, supporting reliance on physical timing. On NVIDIA B200 GPUs, parallel wave integration accelerates inference by up to 2,630 times over its serial implementation and reduces peak GPU memory by up to 97.6% relative to Mamba in the tested configurations.

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

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Byunggu Yu, Justin Kim
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
