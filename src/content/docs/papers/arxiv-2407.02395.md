---
title: "Toward Secure Code Generation: Bridging Correctness and Security via Task-Adaptive Vulnerability Modeling and Execution-Based Benchmarking"
description: "Large language models (LLMs) are increasingly used for program synthesis, yet they often generate code that is functionally plausible but insecure."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2407.02395) · [PDF](https://arxiv.org/pdf/2407.02395)

## 一句话摘要

Large language models (LLMs) are increasingly used for program synthesis, yet they often generate code that is functionally plausible but insecure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly used for program synthesis, yet they often generate code that is functionally plausible but insecure. Progress in secure code generation has been hindered by benchmarks that are small, non-executable, leak mitigation details, or rely on noisy analyzers and subjective judgments, making it difficult to measure whether security improves without sacrificing correctness. We address these gaps with CodeSecEval, an execution-based benchmark for secure code generation, comprising 255 Python tasks spanning 77 CWE categories. Each task provides paired insecure and secure implementations together with executable functional and vulnerability-targeted security tests, enabling precise and reproducible evaluation of secure code generation and insecure-code repair. Building on CodeSecEval, we propose SecAwareCoder, an agent-based framework that shifts code generation toward secure-by-construction synthesis. SecAwareCoder performs task-adaptive threat modeling to identify security-sensitive regions and derive task-grounded vulnerability hypotheses, uses these hypotheses to guide both constraint-aware code generation and security-aware test synthesis, and leverages execution feedback for targeted refinement. Experiments across multiple LLM backbones show that SecAwareCoder consistently improves Pass@1 and security robustness over prompting and analyzer-driven baselines, narrowing the security--correctness gap in LLM code generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiexin Wang, Liuwen Cao, Xitong Luo, Yang Cao, Zhenghao Li, Yunyi Xiao, Mengchen Zhao, Adam Jatowt, Yi Cai
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
