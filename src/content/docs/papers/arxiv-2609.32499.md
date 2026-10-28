---
title: "Learning an Anchored Prompt Space for Continual Adaptation of Large Language Models"
description: "Continually adapting large language models requires acquiring new knowledge while preserving previously learned capabilities."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.32499) · [PDF](https://arxiv.org/pdf/2609.32499)

## 一句话摘要

Continually adapting large language models requires acquiring new knowledge while preserving previously learned capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Continually adapting large language models requires acquiring new knowledge while preserving previously learned capabilities. Although jointly adapting model parameters and task-specific soft prompts is promising, it has two key limitations: previously learned prompts may lose effectiveness as the model evolves, and relationships among prompts that could support cross-task transfer are not explicitly learned. We propose Learning an Anchored Prompt Space (LAPS), which preserves historical prompt effectiveness and learns relationships among task-specific soft prompts to facilitate positive transfer. Historical prompts are first aligned with the updated model through self-distillation. LAPS then constructs an anchored prompt space whose vertices correspond to learned task-specific soft prompts and whose intermediate geometry is shaped by learnable B\'ezier control prompts. Once this space is learned, LAPS identifies the best-performing prompt for each task on its validation set, allowing the selected prompt to draw on knowledge acquired from related tasks. Experiments on the TRACE benchmark across three Qwen3 model scales show that LAPS consistently outperforms existing distillation-based, prompt-based, and joint prompt-parameter adaptation methods, improving overall task performance while reducing forgetting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rongguang Ye, Zhan Zhuang, Yichen Wu, Ming Tang, Kede Ma
- 发布：2026-09-26；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
