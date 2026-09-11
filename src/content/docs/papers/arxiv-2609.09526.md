---
title: "Benchmarking Agentic HLS Design Tasks With HLS-Eval"
description: "Large language models (LLMs) and AI agents are increasingly explored for hardware design, including high-level digital design."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.09526) · [PDF](https://arxiv.org/pdf/2609.09526)

## 一句话摘要

Large language models (LLMs) and AI agents are increasingly explored for hardware design, including high-level digital design.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) and AI agents are increasingly explored for hardware design, including high-level digital design. While most work targets code generation and editing for hardware description languages (HDLs), our prior work introduced HLS-Eval, an open-source benchmark for evaluating LLMs on high-level synthesis (HLS) design tasks. Those evaluations, however, focused on zero-shot generation and editing, leaving open how agents achieve HLS design tasks. We therefore extend HLS-Eval with an agentic evaluation flow built on the open-source mini-swe-agent framework. The flow lets HLS design agents use file-editing tools, invoke a C++ compiler for self-verification, and iteratively refine designs during inference, while logging agent traces for analysis of cost, token usage, and iteration count. We present initial results on the existing HLS-Eval benchmarks. In our initial evaluation, we find open-source LLMs paired with an agentic harness solve every simple HLS code generation task in our evaluation, underscoring the need to expand benchmark difficulty as model capabilities advance. Analyzing traces from passing and failing runs, we show how model size, token usage, and trajectory length relate to design pass rates. These results establish a foundation for agentic HLS design and motivate harder benchmarks and new agentic tooling as model capabilities progress.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Stefan Abi-Karam, Callie Hao
- 发布：2026-09-08；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
