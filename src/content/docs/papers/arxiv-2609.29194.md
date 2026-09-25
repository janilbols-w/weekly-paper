---
title: "Continuous Online Fault Detection for Mobile Robots via Adaptive Edge Models"
description: "Mobile robots require robust, real-time fault detection capable of continuous adaptation on constrained edge hardware."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.29194) · [PDF](https://arxiv.org/pdf/2609.29194)

## 一句话摘要

Mobile robots require robust, real-time fault detection capable of continuous adaptation on constrained edge hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mobile robots require robust, real-time fault detection capable of continuous adaptation on constrained edge hardware. While deep time-series models excel at unsupervised anomaly detection, their computational cost prohibits high-frequency onboard execution. This paper bridges this gap via a Teacher-Student distillation framework. An offline foundation model (TSPulse) generates pseudo-labels from unlabeled time series augmented with fault injections. A lightweight MiniRocket Student, adapted with a Recursive Least Squares estimator, approximates this complex decision boundary to execute real-time inference onboard. Evaluations on the TSB-AD benchmark and a physical mobile robot demonstrate the Student achieves a 4.30 ms CPU inference latency. During real-world domain shifts, online adaptation enables the Student to recover from unseen mechanical degradation, improving VUS-PR scores from 0.26 to 0.75 without catastrophic forgetting. Crucially, an uncertainty-guided active learning strategy minimizes operator cognitive load, requesting sparse interventions only when encountering novel fault distributions. These results validate the deployment of state-of-the-art anomaly detection on resource-constrained robotics through offline-to-online distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jordan Levy, Nicolas Verstaevel, Vincent Talon, Benoit Gaudou
- 发布：2026-09-25；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
