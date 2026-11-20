---
title: "GLiDE: A Fast, Calibrated Decision Model Distilled from Reasoning Teachers"
description: "Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2611.26509v1) · [PDF](https://arxiv.org/pdf/2611.26509v1)

## 一句话摘要

Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Decision models enable fast, confidence-aware decisions by scoring candidate answers in a single forward pass, without generating text or intermediate reasoning. Yet reasoning can substantially improve decision quality, raising the question of whether its benefits can be retained without the cost of generating it. We investigate this question with \textbf{GLiDE}, a family of decision models spanning 0.4B to 27B parameters. Building on Qwen hybrid language models, GLiDE enables bidirectional interactions between the context, question, and candidate answers by removing causal masking from full-attention layers. To transfer reasoning capabilities into single-pass inference, we combine soft-target distillation from multiple teachers, including a reasoning model, with progressive post-training on diverse decision tasks. We further explore parameter-free recurrent depth to increase inference-time computation without generating tokens. Across five model sizes, GLiDE lies on the performance--parameter Pareto frontier of the Hugging Face \DI{}, with each model outperforming evaluated alternatives of equal or smaller size. \dmtwo{} (27B) achieves a hidden-set score of 71.52, with an expected calibration error of 2.0\% and a median latency of 92.9\,ms on a single GPU. Further checkpoint averaging and parameter-free recurrent depth yield GLiDE~27B, which reaches 73.37 with an expected calibration error of 2.1\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sahibzada Allahyar, Julia White, Dhruv Atreja, George Hurn-Maloney, Urchade Zaratiana
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
