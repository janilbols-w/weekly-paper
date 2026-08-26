---
title: "TaLK: Text-attributed Graph Dataset Distillation via Coupling Language Model with Graph-Aware Kernel"
description: "Text-attributed graphs (TAGs) are widely used in many real-world domains, and learning on TAGs requires jointly modeling text semantics and graph structure."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.22975) · [PDF](https://arxiv.org/pdf/2606.22975)

## 一句话摘要

Text-attributed graphs (TAGs) are widely used in many real-world domains, and learning on TAGs requires jointly modeling text semantics and graph structure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Text-attributed graphs (TAGs) are widely used in many real-world domains, and learning on TAGs requires jointly modeling text semantics and graph structure. A standard approach for modeling TAGs is to combine a language model (LM) and a graph neural network (GNN), but joint training is computationally expensive and difficult to scale. Dataset distillation is a promising way to reduce training costs, but existing methods are not well suited to TAGs because they are typically designed for a single modality or still require repeatedly training expensive LM-GNN models on the full dataset during distillation. To address this, we propose TaLK, an effective dataset distillation method for TAGs that couples an LM with a graph-aware neural tangent kernel. This design enables efficient dataset distillation, avoiding repeated joint training on the full dataset while reflecting both textual and structural information for effective TAG learning. Experiments on multiple TAG benchmarks show that TaLK consistently outperforms existing baselines and achieves up to 97% of full-dataset performance with only 1% synthetic data.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yeongho Kim, Yeonje Choi, Kijung Shin
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
