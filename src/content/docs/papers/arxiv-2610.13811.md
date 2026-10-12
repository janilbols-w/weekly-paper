---
title: "QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code"
description: "Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.13811) · [PDF](https://arxiv.org/pdf/2610.13811)

## 一句话摘要

Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a correct solution, but not whether its tests can distinguish correct implementations from faulty ones. We introduce QTestBench, a framework that evaluates LLM-generated quantum test suites against independent benchmark checkers, never treating the tests themselves as ground truth. For each task, QTestBench prompts models to produce syntactic, semantic, and behavioral tests, injects candidate solutions at runtime, and compares each test verdict with the checker's label under three validation cohorts, each answering a distinct diagnostic question. We benchmark five LLMs on eight PennyLane QHack challenges and ten Qiskit HumanEval tasks. Generated suites almost always execute, but discrimination lags behind: the best generator reaches a test quality of 0.71 on QHack and 0.34 on Qiskit HumanEval, so executability alone overstates test quality. Oracle-verified synthetic mutants stabilize bug-detection estimates when natural faulty solutions are scarce, as on three of ten Qiskit tasks that yield none. QTestBench offers a reproducible, cross-framework benchmark for the trustworthiness of LLM-generated quantum tests.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Meriem Terki, Nouhaila Innan, Minghao Shao, Muhammad Kashif, Alberto Marchisio, Muhammad Shafique
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
