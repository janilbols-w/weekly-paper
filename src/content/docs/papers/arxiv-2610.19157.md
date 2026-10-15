---
title: "DivAlgo: A systematic evaluation of algorithmic diversity for code generation models"
description: "Code generation models are actively being used in professional and educational settings."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2610.19157) · [PDF](https://arxiv.org/pdf/2610.19157)

## 一句话摘要

Code generation models are actively being used in professional and educational settings.

## 为什么值得关注

待编辑增强。

## 摘要原文

Code generation models are actively being used in professional and educational settings. However, the competence of large language models (LLMs) to generate algorithmically diverse code remains largely unknown. We propose the DivAlgo benchmark, a large-scale dataset constituting algorithmically diverse solutions to programming problems. We also introduce a lightweight similarity metric to enable large-scale evaluation. Our experiments across 24 modern code generation models found that uncontrolled model-generated code is significantly less diverse than human solutions (capturing ~31% of human diversity), and even the best diverse code generation strategy could achieve only ~70% of human diversity. Moreover, while it was possible to steer the models to generate solutions based on human strategies, they were unable to reproduce the diversity of the human solutions. These findings indicate the limitations of code generation models in capturing the algorithmic diversity humans exhibit, and that overexposure to model-generated code can narrow programmers' algorithmic vocabulary.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anubhav Jangra, Smaranda Muresan
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
