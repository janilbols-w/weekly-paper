---
title: "Solving Every Step Is Not Enough: Milestone Oracles Reveal a Composition Gap in LLM Math Reasoning"
description: "Large language models (LLMs) can solve every intermediate step of a multi-step math problem on its own and still fail the full problem, even when given a roadmap of the steps and all of their answers."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.32235) · [PDF](https://arxiv.org/pdf/2609.32235)

## 一句话摘要

Large language models (LLMs) can solve every intermediate step of a multi-step math problem on its own and still fail the full problem, even when given a roadmap of the steps and all of their answers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) can solve every intermediate step of a multi-step math problem on its own and still fail the full problem, even when given a roadmap of the steps and all of their answers. We introduce OracleLadder, a diagnostic evaluation that locates where LLM math reasoning fails by giving the model increasing levels of oracle help. For each problem, a teacher model writes a fixed roadmap of intermediate sub-goals (milestones), and a deterministic symbolic verifier grades every answer. Testing the model with no help, with the roadmap, with the roadmap plus the milestone answers, and on each milestone alone sorts each failure into one of five reasoning gaps. On 354 NuminaMath problems and six models from 8B to 671B parameters (Qwen3, gpt-oss, Llama 3.3, DeepSeek-V3.1), the largest gap for every model is the composition gap, a stricter form of the compositionality gap. It covers 33-48% of problems, and 24-37% after removing problems that an LLM review flags as grading errors. Accuracy and milestone-help recovery rank the two strongest models differently, and two RLVR runs with similar accuracy gains move problems differently. The roadmap effect replicates on MATH500 and AIME 2024/25, per-problem recovery agrees for 83-87% of problems under an independent second teacher, and the help ladder carries over to code generation. We release the data, roadmaps, prompts, and code at https://github.com/slark-prime/OracleLadder.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zhuohan Wang, Haoran Ma, Tianyu Wu, Yuanlin Duan, Zichun Liao, Jieming Yu
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/slark-prime/OracleLadder](https://github.com/slark-prime/OracleLadder)
- 阅读深度：metadata
