---
title: "Neural Spectral Capacity with Residual Context for Heterogeneous Resource Allocation within Transformers"
description: "Predicting relative trained performance from architectural specifications can guide design when training costs limit experimentation."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.30823) · [PDF](https://arxiv.org/pdf/2610.30823)

## 一句话摘要

Predicting relative trained performance from architectural specifications can guide design when training costs limit experimentation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Predicting relative trained performance from architectural specifications can guide design when training costs limit experimentation. Neural Spectral Capacity (NSC) provides such a heuristic, but scores projections independently and assigns identical scores to compatible reorderings of the same layer configurations. We introduce Residual-Aware Neural Spectral Capacity (ResNSC) for Transformers, using a specification-derived statistical reference for accumulated residual updates to determine the input and residual-state statistics in each projection's capacity calculation, while retaining additive evaluation without data or instantiated weights. When residual widths vary, earlier choices affect later scores, so we augment NSC's allocator (NSC-DP) with residual history beyond its layer-and-budget state. ResNSC-DP jointly allocates residual and feed-forward widths under a resource budget, with certified bounds on the best numerically evaluated ResNSC score within a specified finite candidate set. At the 121M and 374M pretraining scales, selected architectures achieve lower mean perplexity than uniform, variable-width, and tapered allocations on FineWeb-Edu, WikiText-2, and LAMBADA at comparable parameter budgets. In inherited-weight LLaMA-7B pruning using the LoNAS supernet, ResNSC-DP improves eight-task average accuracy over NSC by 3.28--5.46 percentage points across eight matched parameter budgets. Paired reversals preserve the projection shapes and NSC scores yet worsen performance in both settings, exposing performance differences hidden by position-independent scoring. The code for this work is available at https://github.com/Optima-CityU/neural-spectral-capacity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Chenyu Zhu, Ruoyu Zhao, Zhichao Lu
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Optima-CityU/neural-spectral-capacity](https://github.com/Optima-CityU/neural-spectral-capacity)
- 阅读深度：metadata
