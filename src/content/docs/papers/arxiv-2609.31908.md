---
title: "Improving Medical Calculation of LLMs with Embedded Coding"
description: "Large Language Models (LLMs) perform well on medical examinations and question-answering benchmarks, but remain unreliable on medical calculation tasks that require exact numerical outputs."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.31908) · [PDF](https://arxiv.org/pdf/2609.31908)

## 一句话摘要

Large Language Models (LLMs) perform well on medical examinations and question-answering benchmarks, but remain unreliable on medical calculation tasks that require exact numerical outputs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) perform well on medical examinations and question-answering benchmarks, but remain unreliable on medical calculation tasks that require exact numerical outputs. These calculations support high-stakes decisions such as medication dosing, organ-function assessment, and prognostic scoring, for which even small errors can have serious clinical consequences. We introduce MedCode, a framework that improves medical calculation by training LLMs to generate embedded executable code. Given a clinical context, the model identifies the relevant calculator, extracts its input variables, and produces a script that delegates arithmetic operations to a deterministic interpreter. Executing the script returns the calculated value together with an explanation and the appropriate unit. We construct supervised fine-tuning (SFT) and preference datasets from the MedCalc benchmark and additionally curate a dataset for calculation tasks in Intensive Care Unit (ICU) scenarios. We further propose weighted Direct Preference Optimization (wDPO), which adaptively emphasizes preference pairs that are difficult for the model to distinguish. Experiments with LLaMA3-8B, Qwen2.5-7B, and Mistral-7B show absolute accuracy gains of 20--30 percentage points, demonstrating the effectiveness of embedded code generation for medical calculation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianshi Ming, Yingying Zhang, Xian Wu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
