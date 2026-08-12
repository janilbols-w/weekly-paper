---
title: "Compute-Optimal Is Not Cluster-Optimal: Systems-Aware Scaling for Sparse Mixture-of-Experts"
description: "In large-scale pretraining, the algorithm, architecture, and systems decisions are conventionally made in disconnected stages."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.10605) · [PDF](https://arxiv.org/pdf/2608.10605)

## 一句话摘要

In large-scale pretraining, the algorithm, architecture, and systems decisions are conventionally made in disconnected stages.

## 为什么值得关注

待编辑增强。

## 摘要原文

In large-scale pretraining, the algorithm, architecture, and systems decisions are conventionally made in disconnected stages. A scaling law stage selects an architecture and training recipe, optimizing loss under compute constraints, and a separate systems stage then optimizes the implementation for hardware efficiency. In this work, we develop MOSAIC, which formulates model architecture and systems co-design as an optimization problem. MOSAIC couples a predictive scaling law with a calibrated performance model that estimates Model FLOPs Utilization (MFU), communication cost, memory footprint, and the best parallel layout. We instantiate the framework for sparse Mixture-of-Experts (MoE) language models, where expert count, routing sparsity, and other MoE layer dimensions affect both the loss and systems efficiency. We fit a scaling law on sparse MoE models trained on text data, whose scaling dimensions include the sparsity factor, which is the fraction of model parameters inactive per token in a forward pass. The scaling law sweeps in our work span active parameters from $104$ million to $2.7$ billion and total model sizes reaching $79$ billion parameters. We show that, within the calibrated sparsity range, an efficiency-agnostic model-FLOPs budget admits no interior optimal sparsity. The fitted loss decreases monotonically with sparser models and the compute optimum lies at the upper boundary of the data support. An optimal sparsity in MoE models instead emerges under the cluster's systems constraints, as captured by MOSAIC. Our results argue for a shift towards unified architecture and systems co-design for frontier language model training.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Soumajyoti Sarkar, Yuxin Tang, Sheng Zha
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
