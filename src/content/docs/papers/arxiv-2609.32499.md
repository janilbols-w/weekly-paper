---
title: "Learning an Anchored Prompt Space for Continual Adaptation of Large Language Models"
description: "Continually adapting large language models requires acquiring new knowledge while preserving previously learned capabilities."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32499) · [PDF](https://arxiv.org/pdf/2609.32499)

## 一句话摘要

Continually adapting large language models requires acquiring new knowledge while preserving previously learned capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continually adapting large language models requires acquiring new knowledge while preserving previously learned capabilities. Jointly adapting model parameters and task-specific soft prompts offers a promising solution, but faces two key limitations: historical prompts may become less effective as the model evolves, while their transferable cross-task relationships are not explicitly learned. We propose Learning an Anchored Prompt Space (LAPS), which preserves historical prompt effectiveness and learns relationships among task-specific soft prompts to facilitate positive transfer. LAPS first aligns historical prompts with the updated model through self-distillation. LAPS then constructs an anchored prompt space whose vertices correspond to learned task-specific soft prompts and whose intermediate geometry is shaped by learnable B\'ezier control prompts. Once this anchored prompt space is learned, LAPS identifies the best-performing prompt for each task on its validation set, allowing the optimized prompt to draw on knowledge acquired from observed tasks. Experiments on the TRACE benchmark across three Qwen3 model scales show that LAPS consistently outperforms distillation-based, prompt-based, and joint prompt--parameter adaptation baselines, improving average performance while reducing forgetting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rongguang Ye, Zhan Zhuang, Yichen Wu, Ming Tang, Kede Ma
- 发布：2026-09-26；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
