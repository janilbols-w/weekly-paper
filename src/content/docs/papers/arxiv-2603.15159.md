---
title: "To See is Not to Master: Teaching LLMs to Use Private Libraries for Code Generation"
description: "Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2603.15159) · [PDF](https://arxiv.org/pdf/2603.15159)

## 一句话摘要

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries. Existing approaches mainly rely on retrieving private-library API documentation and injecting relevant knowledge into the context at inference time. However, our study shows that this is insufficient: even given accurate required knowledge, LLMs still struggle to invoke private-library APIs effectively. To address this limitation, we propose PriCoder, an approach that teaches LLMs to invoke private-library APIs through automatically synthesized data. Specifically, PriCoder models private-library data synthesis as the construction of a graph, and alternates between two graph operators: (1) Progressive Graph Evolution, which improves data diversity by progressively synthesizing more diverse training samples from basic ones, and (2) Multidimensional Graph Pruning, which improves data quality through a rigorous filtering pipeline. To support rigorous evaluation, we construct two new benchmarks based on recently released libraries that are unfamiliar to the tested models. Experiments on three mainstream LLMs show that PriCoder substantially improves private-library-oriented code generation, yielding gains of over 20% in pass@1 in many settings, while causing negligible impact on general code generation capability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yitong Zhang, Chengze Li, Ruize Chen, Guowei Yang, Xiaoran Jia, Yijie Ren, Jia Li
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
