---
title: "OpenClassGen: A Large-Scale Corpus of Real-World Python Classes for LLM Research"
description: "Existing class-level code generation datasets are either synthetic (ClassEval: 100 classes) or insufficient in scale for modern training needs (RealClassEval: 400 classes), hindering robust evaluation and empirical analysis."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2504.15564) · [PDF](https://arxiv.org/pdf/2504.15564)

## 一句话摘要

Existing class-level code generation datasets are either synthetic (ClassEval: 100 classes) or insufficient in scale for modern training needs (RealClassEval: 400 classes), hindering robust evaluation and empirical analysis.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing class-level code generation datasets are either synthetic (ClassEval: 100 classes) or insufficient in scale for modern training needs (RealClassEval: 400 classes), hindering robust evaluation and empirical analysis. We present OpenClassGen, a large-scale corpus of 324,843 Python classes extracted from 2,970 engineered open-source projects. Each entry pairs a human-written class with its corresponding skeleton, which comprises class and method signatures with associated docstrings, and is enriched with 27 static code metrics covering complexity, coupling, cohesion, and inheritance properties. Unlike prior benchmarks that require repository-level context resolution, OpenClassGen provides self-contained class skeletons that serve as complete generation specifications. We demonstrate the corpus's utility by evaluating three LLMs (GPT-o4-mini, Claude-4-Sonnet, Qwen-3-Coder) on a curated, executable subset of 300 classes, enriched with test suites achieving 58% branch coverage. Results show strong semantic similarity (CodeBERTScore-F3: 0.89) but moderate functional correctness (pass rate: 0.33), with substantial variance across models. This variance, along with diverse class characteristics, confirms that OpenClassGen enables meaningful differentiation of LLM capabilities. The dataset supports diverse use cases, including fine-tuning, retrieval-augmented generation, difficulty modelling, and failure mode analysis. The complete dataset and curation scripts are publicly available at https://zenodo.org/records/18409150.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
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
