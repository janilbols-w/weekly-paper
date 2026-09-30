---
title: "ReMCTS: Reflection-Enhanced Monte Carlo Tree Search for Code Generation"
description: "Open-weight large language models (LLMs) can generate function-level programs from natural-language prompts, but plausible candidates still fail on hidden semantics and repeat mistakes across repair attempts."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.34717) · [PDF](https://arxiv.org/pdf/2609.34717)

## 一句话摘要

Open-weight large language models (LLMs) can generate function-level programs from natural-language prompts, but plausible candidates still fail on hidden semantics and repeat mistakes across repair attempts.

## 为什么值得关注

待编辑增强。

## 摘要原文

Open-weight large language models (LLMs) can generate function-level programs from natural-language prompts, but plausible candidates still fail on hidden semantics and repeat mistakes across repair attempts. We present ReMCTS, an execution-grounded, memory-augmented, LLM-guided MCTS-style search framework. It organizes program candidates as tree states, retains branch-local debugging context, retrieves failure experience across branches, and distinguishes failed checks from unavailable evidence. On HumanEval and MBPP-Sanitized, visible-test ReMCTS improves over direct generation in 8 of 10 model-dataset pairs under held-out evaluation, whereas proxy-only search is less stable. Controlled tree-search, sampling, repair, and memory ablations characterize the source and limits of these gains. A 30-task HumanEval-X C++ pilot further demonstrates compatibility with compiler-backed execution, but does not constitute a broad multilingual evaluation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Huifei Wang, Xinying Huang, Yiheng Sun, Yifan Yuan
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
