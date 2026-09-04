---
title: "How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?"
description: "Large language models (LLMs) are increasingly deployed on mobile devices, making energy efficiency a key deployment constraint, yet the energy impact of prompt design remains underexplored."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.01798) · [PDF](https://arxiv.org/pdf/2609.01798)

## 一句话摘要

Large language models (LLMs) are increasingly deployed on mobile devices, making energy efficiency a key deployment constraint, yet the energy impact of prompt design remains underexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly deployed on mobile devices, making energy efficiency a key deployment constraint, yet the energy impact of prompt design remains underexplored. This paper aims to understand how two prompt properties, cognitive load and phrasing pattern, shape the energy behavior of on-device LLM inference. We conduct a broad empirical study covering prompt properties, datasets, models, and devices, with phase-level profiling that separates prefill and decode energy. We find that cognitive load primarily affects the energy cost per token, while phrasing pattern affects energy largely through token usage. Our energy-quality analysis further shows that prompt design reshapes the attainable frontier differently across models, highlighting the need for model-aware prompt design in energy-efficient on-device LLM inference. Code, datasets, and scripts are available at https://amai-gsu.github.io/PromptProperty/.

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

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wei Hu, Xiaolong Tu, Dawei Chen, Yitao Chen, Kyungtae Han, Haoxin Wang
- 发布：2026-09-01；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
