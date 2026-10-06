---
title: "Graph Neural Network-Driven Deep Reinforcement Learning for Scalable RIS Allocation"
description: "Reconfigurable Intelligent Surfaces (RISs) offer a promising paradigm to mitigate blockage and extend millimeter-wave coverage in 6G multi-cell networks."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.06295) · [PDF](https://arxiv.org/pdf/2610.06295)

## 一句话摘要

Reconfigurable Intelligent Surfaces (RISs) offer a promising paradigm to mitigate blockage and extend millimeter-wave coverage in 6G multi-cell networks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reconfigurable Intelligent Surfaces (RISs) offer a promising paradigm to mitigate blockage and extend millimeter-wave coverage in 6G multi-cell networks. However, dynamically allocating shared RIS infrastructure across competing base stations is an NP-hard problem posing severe scalability bottlenecks. In this paper, we propose a scalable framework combining Graph Neural Networks (GNNs) with Deep Reinforcement Learning (DRL) for dynamic shared RIS orchestration. By formulating allocation as a Markov Decision Process, we introduce a physical topology sparsification strategy that prunes dense channel matrices into a sparse tripartite graph. This pruning reduces edge density by 77% and removes representation noise, thereby improving global coverage probability while reducing computational complexity. Our relational message-passing architecture naturally generalizes to arbitrary network dimensions without model retraining. Furthermore, structural ablation studies reveal that physical path loss localizes surface dependencies, enabling a highly efficient localized graph design with linear computational scaling. Extensive simulations in dense urban environments demonstrate that under strict infrastructure budget constraints, the proposed GNN-DRL framework consistently outperforms greedy heuristic baselines by up to ~12% in coverage while delivering faster inference speed via GPU acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Martin Mark Zan, Stefan Schwarz
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
