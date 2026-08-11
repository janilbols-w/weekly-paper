---
title: "MetaLint: Easy-to-Hard Generalization for Code Linting"
description: "Large language models excel at code generation but struggle with code linting, particularly in generalizing to unseen or evolving best practices beyond those observed during training."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2507.11687) · [PDF](https://arxiv.org/pdf/2507.11687)

## 一句话摘要

Large language models excel at code generation but struggle with code linting, particularly in generalizing to unseen or evolving best practices beyond those observed during training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models excel at code generation but struggle with code linting, particularly in generalizing to unseen or evolving best practices beyond those observed during training. We introduce MetaLint, a meta-learning framework that formulates code linting as an instruction-following task, where a model evaluates whether code adheres to a natural language specification of best practices. In contrast to prior work that trains models to detect violations from a fixed set of best practices, MetaLint evaluates code against a provided natural language specification, enabling test-time control over which practices to enforce and generalization to unseen or evolving rules without retraining. We demonstrate that models trained solely on synthetic data generated from automatic linters still generalize to harder, context-dependent best practices for which such linters are not available. To evaluate generalization beyond such easy signals, we introduce a human-curated benchmark of hard best practices inspired by Python Enhancement Proposals (PEPs). On this benchmark, MetaLint substantially improves performance without explicit fine-tuning on target best practices and exhibits strong, easy-to-hard generalization. Qwen3-4B achieves a 2.7x detection F-score gain (25.9% -> 70.4%), the highest recall, and a 26.7% localization F-score, matching larger models such as o3-mini. These gains generalize across programming languages, model families, scales, reasoning settings, and linter sources. We release the code and benchmark to support reproducibility and future work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Atharva Naik, Lawanya Baghel, Dhakshin Govindarajan, Darsh Agrawal, Yiqing Xie, Daniel Fried, Carolyn Rose
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
