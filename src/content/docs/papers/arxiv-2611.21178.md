---
title: "TRACK: Tool-Augmented Reasoning over Time Series for Fault Diagnosis in Power Management System"
description: "Fault diagnosis in power management systems running multiple loads relies on experts manually inspecting current and voltage waveforms, which fails to scale across deployed units."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2611.21178) · [PDF](https://arxiv.org/pdf/2611.21178)

## 一句话摘要

Fault diagnosis in power management systems running multiple loads relies on experts manually inspecting current and voltage waveforms, which fails to scale across deployed units.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fault diagnosis in power management systems running multiple loads relies on experts manually inspecting current and voltage waveforms, which fails to scale across deployed units. We present TRACK, which pairs a time series encoder with a Small Language Model to produce structured, physics-grounded diagnostic reports, calling tools for exact, verifiable calculations. It operates on-device, keeping proprietary sensor data local and avoiding expensive API calls. We introduce a rubric-based framework that evaluates these reports by scoring structure, signal fidelity, physics reasoning, diagnosis, and actionability through per-criterion verdicts. On a 15-class multi-load simulated benchmark, TRACK achieves over 95% fault-category accuracy and generalizes to out-of-distribution faults, whereas the best encoder-probing baseline reaches only 58% accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: power management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Erkan Bayram, Debanjan Ghosh, Li Zhu, Sambarta Dasgupta
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
