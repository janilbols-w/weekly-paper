---
title: "FairPGT: Partitioned Graph Transformers for Dual-Level Fair Graph Clustering"
description: "Clustering on attributed graphs can produce demographically biased clusters, particularly when communities align with protected groups."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.23631) · [PDF](https://arxiv.org/pdf/2611.23631)

## 一句话摘要

Clustering on attributed graphs can produce demographically biased clusters, particularly when communities align with protected groups.

## 为什么值得关注

待编辑增强。

## 摘要原文

Clustering on attributed graphs can produce demographically biased clusters, particularly when communities align with protected groups. Graph transformers can amplify this bias through same-group attention, while global attention limits scalability. We propose FairPGT, a partitioned graph transformer for fair graph clustering. FairPGT restricts attention to METIS partitions and connects them through routing tokens, which divides the quadratic cost of attention by the number of partitions. A graph-aware self-training target guides clustering, with a provably bounded deviation from the standard DEC target. Fairness is imposed at two levels: a mutual-information term promotes demographic parity in cluster assignments, while a normalized cross-group attention ratio (nCGAR) guides attention toward group neutrality through self-distillation. We prove that the nCGAR correction moves attention toward neutrality and establish a condition preventing overshooting. Across seven benchmarks, FairPGT achieves the best clustering performance and statistical parity on the three largest graphs (Credit, Pokec-n, Pokec-z), with a statistical-parity gap approximately ten times lower than DMoN, and is Pareto-dominated on only one dataset. On controlled stochastic block models, FairPGT attains 97% of the derived upper bound on NMI for exactly fair clustering when communities and protected groups coincide. These graphs further show that, under strong alignment, assignment-level fairness alone makes the attention group-heterophilous, whereas attention-level fairness alone improves neutrality without ensuring fair clusters. Code for reproducibility is available at https://github.com/SiamakGhodsi/FairPGT.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Siamak Ghodsi, Amjad Seyedi, Sahar Tahmasebi, Eirini Ntoutsi, S\"oren Auer
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/SiamakGhodsi/FairPGT](https://github.com/SiamakGhodsi/FairPGT)
- 阅读深度：metadata
