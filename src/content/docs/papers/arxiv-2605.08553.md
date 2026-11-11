---
title: "VeriContest: A Competitive-Programming Benchmark for Verifiable Code Generation"
description: "Large language models can generate useful code from natural language, but their outputs come without correctness guarantees."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2605.08553) · [PDF](https://arxiv.org/pdf/2605.08553)

## 一句话摘要

Large language models can generate useful code from natural language, but their outputs come without correctness guarantees.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models can generate useful code from natural language, but their outputs come without correctness guarantees. Verifiable code generation offers a path beyond testing by requiring models to produce not only executable code, but also formal specifications and machine-checkable proofs. Progress in this direction, however, is difficult to measure: existing benchmarks are often small, cover only part of the pipeline, lack ground-truth proofs or rigorous specification validation, or target verification settings far from mainstream software development. We present VeriContest, a benchmark of 1,006 competitive-programming problems from LeetCode and Codeforces for verifiable code generation in Rust with Verus. Each problem includes a natural language description, expert-validated formal specifications, judge-accepted Rust code, Verus-checked proofs, and positive and negative test suites. VeriContest is constructed through a three-phase pipeline that scales from manually verified seed problems to semi-automated expansion with human-in-the-loop review. To strengthen benchmark quality, we also use testing to validate postcondition completeness. VeriContest supports both isolated and compositional evaluation of specification, code, and proof generation, and end-to-end verified program synthesis. Evaluating ten state-of-the-art models reveals a sharp gap between ordinary coding and verifiable code generation: the strongest model reaches 97.51% on natural-language-to-code generation, but only 57.16% on specification generation, 13.82% on proof generation, and 6.76% end-to-end. These results identify proof and specification generation as the central bottlenecks for current models and establish VeriContest as a rigorous platform for evaluating and training future systems that generate code with machine-checkable correctness.

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

- 作者：Zichen Xie, Mrigank Pawagi, Yuxin Liu, Aaditi Rai, Lize Shao, John Berberian Jr., Sicong Che, Wenxi Wang
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
