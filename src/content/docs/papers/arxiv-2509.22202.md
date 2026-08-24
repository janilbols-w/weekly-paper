---
title: "Library Hallucinations in LLM-Generated Code: A Risk Analysis Grounded in Developer Queries"
description: "Large language models (LLMs) now play a central role in code generation, yet they continue to hallucinate, frequently inventing non-existent libraries."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2509.22202) · [PDF](https://arxiv.org/pdf/2509.22202)

## 一句话摘要

Large language models (LLMs) now play a central role in code generation, yet they continue to hallucinate, frequently inventing non-existent libraries.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) now play a central role in code generation, yet they continue to hallucinate, frequently inventing non-existent libraries. Such library hallucinations are not just benign errors: they can mislead developers, break builds, and expose systems to supply chain threats such as slopsquatting. Despite growing awareness of these risks, there is limited understanding of how library hallucinations manifest under realistic usage conditions. To fill this gap, we present the first systematic study of how user-level prompt variations influence library hallucinations in LLM-generated code. Across seven diverse LLMs, we analyse library name hallucinations (invalid imports) and library member hallucinations (invalid calls from valid libraries), examining the effects of realistic developer language and controlled user mistakes, including misspellings and fabricated libraries or members. Our findings expose systemic vulnerabilities: one-character misspellings trigger hallucinations in up to 26% of tasks; fabricated library names are accepted in up to 99%; and time-based prompts induce hallucinations in up to 85%. Grounded in the highest-risk prompts identified in our study, we introduce LibHalluBench, a benchmark that enables a systematic and reproducible evaluation of these library hallucinations. Our findings underscore the fragility of LLMs to natural prompt variation and highlight the urgent need for safeguards against library-related hallucinations and their downstream risks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lukas Twist, Mark Harman, Helen Yannakoudakis, Jie M. Zhang
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
