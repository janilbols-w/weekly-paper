---
title: "Taming Multi-Dimensional Skew in Sparse Matrix Multiplication with Contention-Aware Scheduling [Technical Report]"
description: "Sparse general matrix-matrix multiplication (SpGEMM) is a key kernel in graph analytics, relational queries, and machine learning."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.36822) · [PDF](https://arxiv.org/pdf/2610.36822)

## 一句话摘要

Sparse general matrix-matrix multiplication (SpGEMM) is a key kernel in graph analytics, relational queries, and machine learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse general matrix-matrix multiplication (SpGEMM) is a key kernel in graph analytics, relational queries, and machine learning. Yet, its performance remains a significant challenge, due to the inherent sparsity and, more critically, the prevalent skew patterns often found in real-world workloads. This paper investigates this problem and demonstrates that an unbalanced workload distribution is the main culprit, harming performance through two co-existing root causes: first, multi-dimensional skew, where imbalance across computation cost, output density, and data locality cannot be captured by any single balancing metric; and second, cache contention, where dense substructures induce severe on-chip interference. To that end, we propose adaptive morsel scheduling (AMS), a dynamic scheduling framework that decouples skew dimensions via fixed-result-size morsels and integrates contention-aware load balancing (CALB) and data-conscious simultaneous multithreading activator (SMTact) to alleviate cache-level contention, alongside a hybrid accumulation mechanism (HYB) that adaptively selects the best accumulator per morsel. Evaluations across matrix squaring, relational queries, graph analytics, and other sparse matrix kernels show that AMS significantly outperforms state-of-the-art methods on skewed workloads while maintaining comparable performance on non-skewed ones. These gains, along with improved bandwidth utilization, remain valid across a wide range of workloads and hardware systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wentao Huang, Qiming Huang, Yunhong Ji, Mian Lu, Yuqiang Chen, Bingsheng He, Kian-Lee Tan
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
