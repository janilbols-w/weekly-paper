---
title: "Program Semantic Inequivalence Game with Large Language Models"
description: "Large Language Models (LLMs) can achieve strong performance on everyday coding tasks, but they can fail on complex tasks that require non-trivial reasoning about program semantics."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2505.03818) · [PDF](https://arxiv.org/pdf/2505.03818)

## 一句话摘要

Large Language Models (LLMs) can achieve strong performance on everyday coding tasks, but they can fail on complex tasks that require non-trivial reasoning about program semantics.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) can achieve strong performance on everyday coding tasks, but they can fail on complex tasks that require non-trivial reasoning about program semantics. Finding training examples to teach LLMs to solve these tasks can be challenging. In this work, we explore a method to synthetically generate code reasoning training data based on a semantic inequivalence game (SInQ): a generator agent creates program variants that are semantically distinct, derived from a dataset of real-world programming tasks, while an evaluator agent has to identify input examples for which they behave differently. The agents train each other semi-adversarially, improving their ability to understand the underlying logic of code. We evaluated our approach on multiple code generation and understanding benchmarks, including cross-language vulnerability detection (Lu et al., 2021),, where our method improves vulnerability detection in C/C++ code despite being trained exclusively on Python code, and the challenging Python builtin identifier swap benchmark (Miceli Barone et al., 2023),, showing that whereas modern LLMs still struggle with this benchmark, our approach yields substantial improvements. We release the code needed to replicate the experiments, as well as the generated synthetic data, which can be used to fine-tune LLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Antonio Valerio Miceli-Barone, Vaishak Belle, Ali Payani
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
