---
title: "Not All Neighbors Matter: Understanding the Impact of Graph Sparsification on GNN Pipelines"
description: "As graphs scale to billions of nodes and edges, graph Machine Learning workloads are constrained by the cost of multi-hop traversals over exponentially growing neighborhoods."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2603.06952) · [PDF](https://arxiv.org/pdf/2603.06952)

## 一句话摘要

As graphs scale to billions of nodes and edges, graph Machine Learning workloads are constrained by the cost of multi-hop traversals over exponentially growing neighborhoods.

## 为什么值得关注

待编辑增强。

## 摘要原文

As graphs scale to billions of nodes and edges, graph Machine Learning workloads are constrained by the cost of multi-hop traversals over exponentially growing neighborhoods. While various system-level and algorithmic optimizations have been proposed to accelerate Graph Neural Network (GNN) pipelines, data management and movement remain the primary bottlenecks at scale. In this paper, we explore whether graph sparsification, a well-established technique that reduces edges to create sparser neighborhoods, can serve as a lightweight pre-processing step to address these bottlenecks while preserving accuracy on node classification tasks. We develop an extensible experimental framework that enables systematic evaluation of how different sparsification methods affect the performance and accuracy of GNN models. We conduct the first comprehensive study of GNN training and inference on sparsified graphs, revealing several key findings. First, sparsification often preserves or even improves predictive performance. As an example, random sparsification raises the accuracy of the GAT model by 6.8% on the PubMed graph. Second, benefits increase with scale, substantially accelerating both training and inference. Our results show that the K-Neighbor sparsifier improves model serving performance on the Products graph by 11.7x with only a 0.7% accuracy drop. Importantly, we find that the computational overhead of sparsification is quickly amortized, making it practical for very large graphs.

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

- taxonomy keywords: model serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yuhang Song, Naima Abrar Shami, Romaric Duvignau, Vasiliki Kalavri
- 发布：2026-08-18；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
