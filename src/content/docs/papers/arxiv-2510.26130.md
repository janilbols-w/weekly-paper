---
title: "Beyond Synthetic Benchmarks: Evaluating LLM Performance on Real-World Class-Level Code Generation"
description: "Large language models (LLMs) have advanced rapidly from well-studied function-level code generation to emerging repository-level approaches, yet this progression reveals a critical gap: class-level code generation, which is the fundamental building block connecting individual functions to complete repositories, remains systematically underexplored."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2510.26130) · [PDF](https://arxiv.org/pdf/2510.26130)

## 一句话摘要

Large language models (LLMs) have advanced rapidly from well-studied function-level code generation to emerging repository-level approaches, yet this progression reveals a critical gap: class-level code generation, which is the fundamental building block connecting individual functions to complete repositories, remains systematically underexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have advanced rapidly from well-studied function-level code generation to emerging repository-level approaches, yet this progression reveals a critical gap: class-level code generation, which is the fundamental building block connecting individual functions to complete repositories, remains systematically underexplored. Understanding class-level capabilities is a prerequisite to repository-level success, as current approaches cannot distinguish whether failures stem from basic implementation deficiencies or sophisticated context management issues. We introduce RealClassEval, a benchmark derived from real-world open-source repositories, comprising 400 classes divided into seen and unseen partitions based on model training cutoffs. Our systematic evaluation across seven state-of-the-art LLMs reveals fundamental limitations masked by synthetic benchmarks: while LLMs achieve 84 to 89% correctness on synthetic tasks, they attain only 25 to 34% on real-world classes, with minimal distinction between seen and unseen codebases. Notably, this performance range converges with concurrent work using rich natural language descriptions and repository context, suggesting that specification complexity cannot overcome core implementation bottlenecks. Documentation provides marginal improvements (1 to 3%), while retrieval augmentation yields greater gains (4 to7%), specifically with incomplete specifications. Error analysis reveals AttributeError, TypeError, and AssertionError dominate 84% of failures, with distinct patterns between synthetic (logic-focused) and real-world (object-oriented) scenarios. These findings establish the diagnostic foundation necessary for advancing both fundamental LLM capabilities and sophisticated repository-level approaches, while providing actionable guidance for production deployment strategies.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Musfiqur Rahman, SayedHassan Khatoonabadi, Emad Shihab
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
