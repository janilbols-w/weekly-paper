---
title: "Understanding Quantization of Optimizer States in LLM Pre-training: Dynamics of State Staleness and Effectiveness of State Resets"
description: "Quantizing optimizer states is becoming an important ingredient of memory-efficient large-scale pre-training, but the resulting optimizer dynamics remain only partially understood."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2603.16731) · [PDF](https://arxiv.org/pdf/2603.16731)

## 一句话摘要

Quantizing optimizer states is becoming an important ingredient of memory-efficient large-scale pre-training, but the resulting optimizer dynamics remain only partially understood.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantizing optimizer states is becoming an important ingredient of memory-efficient large-scale pre-training, but the resulting optimizer dynamics remain only partially understood. We study low-precision exponential moving average (EMA) optimizer states and show how quantization can cause many nominal updates to round back to the same stored value, making the state effectively stale and slowing adaptation beyond what the nominal decay would suggest. We then develop a simple predictive model of stalling that estimates one-step stalling probabilities and characterizes how stalling builds up over time after the initialization. This perspective provides a mechanistic explanation for why optimizer-state resets help in low precision: once a quantized EMA becomes effectively stale, resetting it can temporarily restore responsiveness. Motivated by this picture, we derive a simple theory-guided method for choosing useful reset periods, showing that in low precision the key question is not only whether resets help, but when they should be applied. Experiments in controlled simulations and LLM pre-training show that suitable reset schedules recover the performance lost to low-precision state storage while substantially reducing optimizer-state memory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kristi Topollai, Anna Choromanska
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
