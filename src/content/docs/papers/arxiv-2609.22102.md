---
title: "When Who You Are Can Change the Code You Get: A Study of Persona-Induced Bias in LLM Code Generation"
description: "Large Language Models (LLMs) are widely used as programming assistants, yet it remains unclear whether and how user's demographic information impacts the technical quality of generated code."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.22102) · [PDF](https://arxiv.org/pdf/2609.22102)

## 一句话摘要

Large Language Models (LLMs) are widely used as programming assistants, yet it remains unclear whether and how user's demographic information impacts the technical quality of generated code.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) are widely used as programming assistants, yet it remains unclear whether and how user's demographic information impacts the technical quality of generated code. We conduct a large-scale empirical study of persona-induced bias in LLM-based code generation, focusing a proprietary model (Gemini 2.5 Pro) and an open-weight model (GPT-OSS-120B). Using 18 demographic personas spanning nationality, gender, and experience level, we compare persona-induced prompts against a neutral baseline. Across 35,000+ generated programs, we analyze demographic marker leakage in reasoning and responses, as well as differences in functional correctness, maintainability, code style, and security. Our results show that demographic cues are frequently reflected in LLM reasoning and outputs. Demographic markers appear in up to 65% of responses and 70% of reasoning traces, despite being semantically irrelevant to the tasks. On LiveCodeBench, persona prompting were associated with lower correctness scores of the Gemini model by an average of 1.54 percentage points, with one persona exhibiting a decrease of 3.6% (odds ratio = 0.51). In contrast, the accuracy of the GPT-OSS model improved by 3.4 - 5.7% across all personas (odds ratios = 1.8 - 3.0). Maintainability and code style metrics show statistically significant but negligible effect sizes (all Cliff's {\delta} < 0.15), and security vulnerabilities exhibit no systematic persona-specific patterns. Overall, our results show that the presence of demographic information about users is associated with measurable variation in LLM reasoning and code quality even in purely technical tasks, and that these effects hold across models. Our work highlights an under-examined risk in LLM-assisted software development.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anubhav Gupta, Mayara Costa Figueiredo, Leticia Santos Machado, Tanner Wright, Ivan Beschastnikh, Cleidson R. B. de Souza, Gema Rodr\'iguez-P\'erez
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
