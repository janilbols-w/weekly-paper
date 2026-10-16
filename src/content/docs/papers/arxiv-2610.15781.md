---
title: "Heterogeneous Structured Pruning Under Resource Constraints for Hardware-Efficient Large Language Models"
description: "Training-free pruning removes weights from pretrained large language models to reduce their deployment cost."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.15781v1) · [PDF](https://arxiv.org/pdf/2610.15781v1)

## 一句话摘要

Training-free pruning removes weights from pretrained large language models to reduce their deployment cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training-free pruning removes weights from pretrained large language models to reduce their deployment cost. However, existing approaches typically consider only the total number of retained weights. Consequently, their pruning decisions do not account for how target hardware stores and processes those weights. These methods select a sparsity structure in advance and apply it uniformly to all projections, rather than accounting for how each structure trades pruning error against latency and memory across sublayers. We propose Heterogeneous Structured Pruning (HSP), a hardware-aware pruning framework that combines two components: (i) a heterogeneous search space of dense, unstructured, 2:4, block-sparse, and head / channel (H/C) pruning options and (ii) structure-regularising constraints based on latency and memory models. Our contribution generalises existing importance-based methods: a global solver selects one option per sublayer to minimise proxy pruning loss under a resource budget, thereby assigning each projection a structure and density. We evaluate HSP on OPT and LLaMA models for an NVIDIA Jetson Orin Nano Super edge device, where it improves the quality-resource frontiers over training-free baselines. A project page and updated links for the related code is maintained at: cameronbarker.me/publications/hsp.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Cameron Barker, Andreas Paraskeva, Jan N. van Rijn, Elliot J. Crowley, Henry Gouk
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
