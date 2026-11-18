---
title: "EfficientSkill: Learning Skills for Token-Efficient Multi-Turn Agents"
description: "Reflective skill optimizers improve multi-turn LLM agents by revising instructions from failed and successful rollouts, yet accumulating edge-case rules bloats prompts, inflates token use, and pushes agents into long, error-prone loops."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.19823) · [PDF](https://arxiv.org/pdf/2611.19823)

## 一句话摘要

Reflective skill optimizers improve multi-turn LLM agents by revising instructions from failed and successful rollouts, yet accumulating edge-case rules bloats prompts, inflates token use, and pushes agents into long, error-prone loops.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reflective skill optimizers improve multi-turn LLM agents by revising instructions from failed and successful rollouts, yet accumulating edge-case rules bloats prompts, inflates token use, and pushes agents into long, error-prone loops. We introduce EfficientSkill, a two-step framework that first discovers a reliable skill without token penalties, and then warm-starts accuracy-guarded pruning from that skill to compress instructions, bound agent turns, and offload reusable code into workspace utilities with zero implementation prompt cost. Across four frontier, mid-tier, and open-weight models on MATH-500, ALFWorld, and SpreadsheetBench, EfficientSkill cuts output tokens over unconstrained EvoSkill on 11 of 12 configurations (by up to 80%) while raising mean accuracy on every benchmark, including +14.3 and +17.5 percentage-point gains on SpreadsheetBench with Gemini 3.8 Flash and Grok 4.1 Fast by replacing stalled loops with compact workflows. By shrinking both generated tokens and replayed history, EfficientSkill lowers total token usage and serving cost across every evaluated configuration, with or without full-prefix KV caching.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Deep Shah, Sanket Badhe, Nehal Kathrotia, Priyanka Tiwari
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
