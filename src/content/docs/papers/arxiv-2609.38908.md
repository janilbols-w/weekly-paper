---
title: "CellMSA: Context Modeling for Single-Cell Representation Learning"
description: "Single-cell transcriptomics enables profiling of cellular states at unprecedented resolution, but its high dimensionality, sparsity, and technical batch effects pose significant challenges for representation learning."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.38908) · [PDF](https://arxiv.org/pdf/2609.38908)

## 一句话摘要

Single-cell transcriptomics enables profiling of cellular states at unprecedented resolution, but its high dimensionality, sparsity, and technical batch effects pose significant challenges for representation learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Single-cell transcriptomics enables profiling of cellular states at unprecedented resolution, but its high dimensionality, sparsity, and technical batch effects pose significant challenges for representation learning. Existing single-cell foundation models typically encode each cell independently or only model cells from the same batch for denoising, thereby underutilizing the rich relational information across batches and cell types to model gene expression patterns. We argue that single-cell models can benefit from more informative cell-context modeling. By comparing consistency and variation across cells, models can capture fine-grained gene-gene dependencies associated with cell states, which are essential for learning high-quality representations. Inspired by the use of multiple sequence alignment (MSA) context in protein modeling, we propose CellMSA, a single-cell representation learning framework that introduces an MSA-inspired inductive bias into transcriptomic modeling. For each target cell, CellMSA retrieves relevant cells from different batches and biologically related cell types as context, and summarizes cross-cell patterns into a context-dependent gene-pair representation. This representation is then injected into a pair-aware target-cell encoder for fine-grained representation learning. We pretrain CellMSA on a large-scale human single-cell corpus of approximately 109 million cell observations, including 65.6 million primary observations. Experiments show that our framework consistently outperforms existing methods across multiple benchmarks. Code is available at the following repository: https://github.com/PharMolix/CellMSA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Suyuan Zhao, Minghao Liu, Yizhen Luo, Zaiqing Nie
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/PharMolix/CellMSA](https://github.com/PharMolix/CellMSA)
- 阅读深度：metadata
