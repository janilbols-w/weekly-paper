---
title: "Is Knowledge Distillation Actually Greener? A Case Study in Machine Translation"
description: "Knowledge distillation (KD) is a technique to compress a larger teacher system into a smaller student."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.09691) · [PDF](https://arxiv.org/pdf/2602.09691)

## 一句话摘要

Knowledge distillation (KD) is a technique to compress a larger teacher system into a smaller student.

## 为什么值得关注

待编辑增强。

## 摘要原文

Knowledge distillation (KD) is a technique to compress a larger teacher system into a smaller student. In machine translation, KD is commonly evaluated through translation quality and inference efficiency, without jointly accounting for the environmental costs of producing and deploying the distilled system. We evaluate representative KD methods both on bespoke MT models and LLMs, by considering both translation quality and computational cost, using the Machine Learning Life Cycle Assessment tool, which accounts for costs throughout the KD model life cycle. Our key finding is that the deployment volume required to amortize KD is serving-dependent and can shift by several orders of magnitude under batching. We include actionable guidance for selecting, developing, and evaluating KD methods under quality and compute-induced constraints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joseph Attieh, Timothee Mickus, Anne-Laure Ligozat, Aur\'elie N\'ev\'eol, J\"org Tiedemann
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
