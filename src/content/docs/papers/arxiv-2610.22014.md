---
title: "GraphBEAT: Graph-based Bucketized Event Aggregation Over Time for Early Risk Stratification of Gastrointestinal Cancers"
description: "Longitudinal electronic health records (EHRs) contain complementary diagnostic and laboratory information about patient health."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.22014) · [PDF](https://arxiv.org/pdf/2610.22014)

## 一句话摘要

Longitudinal electronic health records (EHRs) contain complementary diagnostic and laboratory information about patient health.

## 为什么值得关注

待编辑增强。

## 摘要原文

Longitudinal electronic health records (EHRs) contain complementary diagnostic and laboratory information about patient health. However, irregularity, sparsity, heterogeneity, and incompleteness in documentation complicate EHR modeling. To address the problem, we introduce GraphBEAT (Graph-based Bucketized Event Aggregation over Time), a temporal graph representation learning framework that groups clinical events into time buckets and transforms observed features into patient-specific, temporally directed graphs to enable early risk stratification for gastrointestinal cancers. Each node in an EHR graph encodes feature identity, observed value, and temporal position of clinical events. A context-aware, time-decay message-passing mechanism models transitions between successive buckets, followed by multi-head attention pooling to generate patient-level representations. GraphBEAT was trained and evaluated on multi-site longitudinal diagnosis codes and laboratory tests to predict pancreatic, liver, and intestinal cancer at 12-, 24-, and 36-month diagnostic lead times. In all experimental setups, GraphBEAT consistently outperformed baseline graph neural networks (GraphSAGE, GAT, and GCN) and sequence modeling approaches (Transformer and long short-term memory [LSTM]). GraphBEAT also required over 250x fewer floating-point operations per patient and over 20x fewer parameters than the Transformer and LSTM baselines. These results support GraphBEAT as an accurate and computationally efficient approach for cancer risk stratification from sparse, heterogeneous longitudinal health records.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Leo Y. Li-Han, Chris Varghese, Elizabeth B. Habermann, Mark J. Truty, William R. G. Perry, Cornelius A. Thiels, Hojjat Salehinejad
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
