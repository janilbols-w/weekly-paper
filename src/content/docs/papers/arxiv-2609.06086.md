---
title: "Poseidon: DAG-Guided Parallelism Search for LLM Pre-Training on Heterogeneous Clusters"
description: "With the rapid advancement of accelerator technologies, pre-training large language models (LLMs) on heterogeneous accelerator clusters has become increasingly crucial for maximizing hardware utilization."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.06086) · [PDF](https://arxiv.org/pdf/2609.06086)

## 一句话摘要

With the rapid advancement of accelerator technologies, pre-training large language models (LLMs) on heterogeneous accelerator clusters has become increasingly crucial for maximizing hardware utilization.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the rapid advancement of accelerator technologies, pre-training large language models (LLMs) on heterogeneous accelerator clusters has become increasingly crucial for maximizing hardware utilization. Existing systems, however, suffer from inaccurate training time modeling, which undermines the parallelization optimizations built upon it. Moreover, for current approaches, the vast configuration search space makes exhaustive exploration infeasible, forcing a trade-off between search time and training efficiency. To overcome these limitations, we introduce Poseidon, an efficient and scalable LLM training framework designed with heterogeneity awareness. Its core is an explicit training time model based on a directed acyclic graph. Building on this graph, Poseidon employs two efficient, theoretically grounded strategies: stage-level pruning via early stopping with partial estimation, and layer-to-stage mapping exploiting a ridge-like distribution pattern. These strategies reduce the search space without sacrificing optimal training efficiency. Experiments on heterogeneous clusters show that Poseidon improves training throughput by up to $2.76\times$ over state-of-the-art systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaosong Chen, Shaoheng Nie, Zhongmin Zhao, Zizhao Mo, Jiapeng Chen, Huanle Xu, Zeren Li, Weiwei Sun, ChengZhong Xu
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
