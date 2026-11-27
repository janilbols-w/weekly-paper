---
title: "Physical regime changes expose formula misuse in large language models"
description: "Large language models (LLMs) are increasingly employed for scientific computing across the Earth and environmental sciences, but problems in these fields often involve distinct physical regimes."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2611.28669v1) · [PDF](https://arxiv.org/pdf/2611.28669v1)

## 一句话摘要

Large language models (LLMs) are increasingly employed for scientific computing across the Earth and environmental sciences, but problems in these fields often involve distinct physical regimes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly employed for scientific computing across the Earth and environmental sciences, but problems in these fields often involve distinct physical regimes. LLMs may fail to recognize these regime-dependent constraints, applying formulas outside their domains of validity and producing plausible but physically incorrect results. We systematically investigate these failures through controlled experiments and assess whether post-training can improve regime-aware reasoning. Across 72 physical mechanisms, we find frontier LLMs frequently misapply formulas outside their regimes of validity, reducing accuracy by 13-57 percentage points. Reinforcement learning with verifiable rewards enables Qwen3.5-9B to match DeepSeek V4 Flash (284B) on regime-dependent tasks, but its effectiveness is limited by the formulas available in the base model. Combining supervised fine-tuning on a few worked examples with reinforcement learning improves accuracy by 61 percentage points, while distillation from a teacher supplied with the correct formula raises accuracy from 0% to 71%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Maohao Ran, Yanting Zhang, Chendong Ma, Jun Song
- 发布：2026-11-21；更新：2026-11-21
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/acodercat/AtmosRegime](https://github.com/acodercat/AtmosRegime)
- 阅读深度：metadata
