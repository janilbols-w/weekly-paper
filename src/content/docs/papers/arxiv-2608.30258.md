---
title: "Stratified Consistency Distillation for Natural Language Formalization"
description: "Neurosymbolic reasoning has shown promising success in addressing complex reasoning tasks by combining large language models (LLMs) and symbolic solvers."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.30258) · [PDF](https://arxiv.org/pdf/2608.30258)

## 一句话摘要

Neurosymbolic reasoning has shown promising success in addressing complex reasoning tasks by combining large language models (LLMs) and symbolic solvers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Neurosymbolic reasoning has shown promising success in addressing complex reasoning tasks by combining large language models (LLMs) and symbolic solvers. While this approach shows promise, a fundamental challenge remains: improving the accuracy of translations from natural language to logical formulas. Current methods predominantly rely on prompt engineering, which is difficult to scale across different domains and input formats. Drawing inspiration from the success of fine-tuning in other model adaptation and alignment applications, we propose a fine-tuning-based Stratified Consistency Distillation approach: (1) We generate K logical translations per input using a frontier LLM and cluster them by semantic equivalence (2) Based on the entropy level, we apply majority voting (low entropy), LLM-as-a-Judge (medium entropy), or unification/abstention (high entropy), and (3) fine-tune a smaller model using the selected pseudo-labels. Our experiments show significant and consistent improvements in both Pass@K and our novel Equivalent Logical Similarity metrics, demonstrating the potential of advancing logical translation through consistency distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhichao Hou, Ferhat Erata, Joe Lilien, MohamadAli Torkamani
- 发布：2026-08-31；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
