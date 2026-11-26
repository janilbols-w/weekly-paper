---
title: "SWE-Proof: Can Language Models Resolve Real-World Issues with Machine-Checked Proofs?"
description: "Ensuring the correctness of LLM-generated code is a core challenge for modern software engineering."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.21190) · [PDF](https://arxiv.org/pdf/2609.21190)

## 一句话摘要

Ensuring the correctness of LLM-generated code is a core challenge for modern software engineering.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ensuring the correctness of LLM-generated code is a core challenge for modern software engineering. Benchmarks for agentic code generation check correctness with held-out test suites, which are inherently incomplete and increasingly susceptible to memorization. Formal verification avoids both problems, but existing work covers only standalone tasks whose specifications are given as input, not real issues, which touch large repositories and state intent in vague natural language. We present BenchProofer, a pipeline that turns a coding task with a known correct patch into a formally verified one: it writes a specification for the new code, summarizes the existing functions that code calls with axioms, and admits an instance only after mechanical and adversarial gates agree. Applying it to SWE-bench Verified yields SWE-Proof, 500 real issues whose correctness is formally verified rather than tested, and it extends to SWE-bench Pro. Evaluating Claude Opus 4.8, we find that verification catches what tests miss: nearly a third of test-passing patches admit counterexamples, which a structured natural-language specification does not fix, while a correct formal one lifts resolution from 85% to 95%. Writing that specification is the hard part: an agent that must write its own gains nothing over an unaided baseline, and only 56% of those specifications pass our audit. The usual failure is faithfulness, where a specification constrains part of the required behavior and leaves the rest free. Specification quality also tracks the outcome, failing on 92% of unresolved instances against 51% of resolved ones, making faithful specification synthesis a concrete open problem. Code is available at https://github.com/amazon-science/BenchProofer.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：George Ma, Benjamin Mikek, Haoyu Li, Ferhat Erata, Yuhao Zhang, Zeren Shui, Behrooz Omidvar Tehrani, Jun Huan, Murali Krishna Ramanathan, Somayeh Sojoudi, Hao Zhou, Anoop Deoras
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/amazon-science/BenchProofer](https://github.com/amazon-science/BenchProofer)
- 阅读深度：metadata
