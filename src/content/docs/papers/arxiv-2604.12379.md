---
title: "Beyond Output Correctness: Benchmarking and Evaluating Large Language Model Reasoning in Coding Tasks"
description: "Large language models (LLMs) increasingly rely on explicit reasoning to solve coding tasks, yet evaluating the quality of this reasoning remains challenging."
---

**评分：51/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2604.12379) · [PDF](https://arxiv.org/pdf/2604.12379)

## 一句话摘要

Large language models (LLMs) increasingly rely on explicit reasoning to solve coding tasks, yet evaluating the quality of this reasoning remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) increasingly rely on explicit reasoning to solve coding tasks, yet evaluating the quality of this reasoning remains challenging. Existing reasoning evaluators are not designed for coding, and current benchmarks focus primarily on code generation, leaving other coding tasks largely unexplored. We introduce CodeRQ-Bench, the first benchmark for evaluating LLM reasoning quality across three coding task categories: generation, summarization, and classification. Using this benchmark, we analyze 1,069 mismatch cases from existing evaluators, identify five recurring limitations, and derive four design insights for reasoning evaluation in coding tasks. Guided by these insights, we propose VERA, a two-stage evaluator that combines evidence-grounded verification with ambiguity-aware score correction. Experiments on CodeRQ-Bench show that VERA consistently outperforms strong baselines across four datasets, improving AUCROC by up to 0.26 and AUPRC by up to 0.21. We release CodeRQ-Bench at https://github.com/MrLYG/CodeRQ-Bench, supporting future investigations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 9 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yuangang Li, Justin Tian Jin Chen, Ethan Yu, David Hong, Iftekhar Ahmed
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/MrLYG/CodeRQ-Bench](https://github.com/MrLYG/CodeRQ-Bench)
- 阅读深度：metadata
