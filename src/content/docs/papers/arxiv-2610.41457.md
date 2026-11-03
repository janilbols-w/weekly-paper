---
title: "RecIS: Unifying Sparse and Dense Computation for Efficient Recommendation Training"
description: "Modern recommender models scale sparse representations and dense computation together."
---

**评分：45/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.41457) · [PDF](https://arxiv.org/pdf/2610.41457)

## 一句话摘要

Modern recommender models scale sparse representations and dense computation together.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern recommender models scale sparse representations and dense computation together. They process thousands of heterogeneous feature fields, long user-behavior sequences, and trillion-scale Embedding parameters, while their dense networks increasingly use large Transformer architectures. The resulting execution mismatch creates fine-grained operations within stages, load imbalance and synchronization delays across devices, and GPU resource bubbles between stages. As models grow, these costs become a primary limit to scalable recommender training. Although existing systems improve Embedding caching and data prefetching, these inefficiencies still coexist in the GPU-centric workloads we study and jointly limit end-to-end throughput. We present RecIS, a unified framework for GPU-centric recommender training. RecIS treats the complete path from input features to dense computation as one optimization target and coordinates three complementary mechanisms. First, adaptive fusion combines fragmented feature transformations with vectorized memory access. Second, a GPU Embedding engine uses hash-based sharding and hierarchical communication to balance request placement and eliminate redundant transfers; it also specializes aggregation for forward and backward index structures. Third, a multistage pipeline overlaps input preparation for future iterations with dense computation in the current iteration. Together, these mechanisms reorganize a fragmented sparse front end into a dataflow that continuously feeds dense computation. We evaluate RecIS on representative industrial recommender models across distributed training platforms. Compared with PICASSO and TorchRec, RecIS reaches up to $2.62\times$ and $1.15\times$ their throughput, respectively, while reducing step latency by up to 61.5\% and 12.9\%. RecIS provides an efficient and scalable training system for large recommender models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hua Zong, Shuai Yang, Zhengxiong Zhou, Qingtao Zeng, Jiawei Liu, Hao Wan, Hongbin Zhou, Jiahao Wang, Hao Zhang, Bencheng Yan, Yuheng Huang, Huimin Yi, Jiamang Wang, Han Zhu, Jian Xu, Bo Zheng, Lin Qu
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
