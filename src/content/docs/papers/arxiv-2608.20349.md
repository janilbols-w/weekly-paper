---
title: "Beyond Prompt Engineering: A Systematic Analysis of Prompt Lexical Sensitivity and Its Impacts on Quality"
description: "Large Language Models (LLMs) exhibit extreme sensitivity to surface-level prompt variations, in which minor lexical changes can trigger disproportionate performance fluctuations."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.20349) · [PDF](https://arxiv.org/pdf/2608.20349)

## 一句话摘要

Large Language Models (LLMs) exhibit extreme sensitivity to surface-level prompt variations, in which minor lexical changes can trigger disproportionate performance fluctuations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) exhibit extreme sensitivity to surface-level prompt variations, in which minor lexical changes can trigger disproportionate performance fluctuations. Moving beyond black-box optimization and coarse-grained templates, we present the first large-scale, n-gram token-level mechanistic analysis of prompt stability, leveraging a dataset of 132,000 prompt variants. Our investigation reveals a fundamental Scaling Law of Prompt Performance Stability: higher average task performance is strongly associated with lower variance and greater robustness across prompt perturbation. We identify two core linguistic drivers underlying this robustness: (1) Domain-Specific Terminology, which tightly anchors semantic boundaries, and (2) Explicit Action Directives, which formalize reasoning trajectories. Together, these elements constrain the model's interpretative space, effectively ``locking in'' more deterministic generation behavior. Building on these insights, we introduce an automated Prompt-Refining Agent that systematically restructures input queries by injecting domain anchoring and operational constraints. Empirical evaluation shows that our approach reduces performance variance by 40.7% in code generation task, while preserving or improving mean performance. These findings provide a statistically grounded and mechanistically interpretable framework for achieving robust prompt engineering.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qipeng Xie, Zi Liang, Jiafei Wu, Yufei Chen, Weizheng Wang, Wenao Ma, Zhong Ming, Haiqin Yang, Kaishun Wu
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
