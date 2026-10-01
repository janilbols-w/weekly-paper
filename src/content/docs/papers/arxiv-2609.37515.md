---
title: "Hierarchical Compression of Vision-Language Model Benchmarks"
description: "Thorough evaluation of vision-language models (VLMs) has become prohibitively expensive, as benchmarks span an ever-broader spectrum of capabilities and new models arrive at a relentless pace."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.37515) · [PDF](https://arxiv.org/pdf/2609.37515)

## 一句话摘要

Thorough evaluation of vision-language models (VLMs) has become prohibitively expensive, as benchmarks span an ever-broader spectrum of capabilities and new models arrive at a relentless pace.

## 为什么值得关注

待编辑增强。

## 摘要原文

Thorough evaluation of vision-language models (VLMs) has become prohibitively expensive, as benchmarks span an ever-broader spectrum of capabilities and new models arrive at a relentless pace. Benchmark compression methods that preserve model rankings at a fraction of the cost are well studied for language models, but for VLMs the question remains under-explored. We present PRIMEBench (Pruning Redundant Items for Multimodal Evaluation), a vision-aware hierarchical benchmark compression framework that substantially reduces evaluation cost while preserving model rankings. This hierarchical framework operates in four stages: data cleaning to remove items answerable without the image and all-correct items, category representative selection to pick one benchmark per capability category, item pruning with Vision-Aware Variance (VAW), and category-count pruning. VAW combines inter-model variance with a vision-dependence score computed from multimodal embeddings alone, while encouraging coverage of diverse items within each benchmark. On models held out from item selection, it has the highest mean fidelity at the released 5% retention. The hierarchical design lets practitioners stop at any stage to match their compute budget; the released suite removes over 97% of items while preserving model rankings. Beyond compression, our analyses show how VLM evaluation behaves as model panels grow and evolve, providing guidance for designing future benchmarks that are more efficient, robust to model turnover, and explicit about the limits of evaluation-side pruning.

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

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hyunjong Ok, Seunggu Kang, Jaeho Lee
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
