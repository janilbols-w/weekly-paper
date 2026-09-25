---
title: "LLM-Based FORM Code Generation with Verification-Driven Fine-Tuning"
description: "FORM is a domain-specific symbolic manipulation language widely used in particle physics for processing the very large algebraic expressions arising from multi-loop Feynman diagram calculations."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.23367) · [PDF](https://arxiv.org/pdf/2609.23367)

## 一句话摘要

FORM is a domain-specific symbolic manipulation language widely used in particle physics for processing the very large algebraic expressions arising from multi-loop Feynman diagram calculations.

## 为什么值得关注

待编辑增强。

## 摘要原文

FORM is a domain-specific symbolic manipulation language widely used in particle physics for processing the very large algebraic expressions arising from multi-loop Feynman diagram calculations. Despite its central role in precision theoretical physics, no artificial-intelligence tooling exists, to our knowledge, for assisting physicists in writing FORM code. We show that contemporary large language models (LLMs), including frontier models with hundreds of billions of parameters, achieve a zero-percent execution pass rate on our instruction-following and tutorial-style FORM tasks without documentation in a single attempt, establishing FORM as a genuine zero-shot language for LLMs at the time of writing. We then present a verification-driven data generation pipeline that uses the FORM binary itself as an execution oracle to produce and validate a corpus of 4,633 training examples spanning deterministic computations, open-ended programs, tutorial code, and knowledge question-answer pairs. Fine-tuning a compact open-weights model (Qwen3-8B) with quantized low-rank adaptation (QLoRA) yields a specialist that, evaluated on four complementary benchmarks (840 tasks, single attempt each), decisively outperforms frontier models with up to 756B parameters in execution rate and in strict, FORM-verified output matching on the larger benchmarks, and remains statistically indistinguishable from them on the smaller, harder ones. General reasoning and coding capabilities are preserved within 2.6 percentage points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bakar Chargeishvili
- 发布：2026-09-20；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
