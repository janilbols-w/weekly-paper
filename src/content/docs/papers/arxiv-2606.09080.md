---
title: "Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy"
description: "Pruning has emerged as a dominant paradigm for accelerating large language model (LLM) inference, spanning a broad spectrum of methods that remove computation across tokens, layers, heads, dimensions, and attention patterns."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.09080) · [PDF](https://arxiv.org/pdf/2606.09080)

## 一句话摘要

Pruning has emerged as a dominant paradigm for accelerating large language model (LLM) inference, spanning a broad spectrum of methods that remove computation across tokens, layers, heads, dimensions, and attention patterns.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pruning has emerged as a dominant paradigm for accelerating large language model (LLM) inference, spanning a broad spectrum of methods that remove computation across tokens, layers, heads, dimensions, and attention patterns. Despite sharing the same objective, these pruning approaches induce fundamentally different execution behaviors, causing realized speedups to depend heavily on hardware and kernel implementations. Consequently, the practical acceleration benefits of different pruning families remain poorly understood. In this work, we introduce a GEMM-centric taxonomy that reorganizes existing pruning methods according to the logical \textbf{M}, \textbf{N}, and \textbf{K} dimensions of general matrix multiplication (GEMM). Leveraging this abstraction, we build a unified benchmarking framework that enables implementation-consistent comparison across the pruning design space and systematically characterizes the acceleration--quality Pareto frontier. Our results on Llama3.1-8B show that static depth pruning remains the strongest Pareto-optimal baseline and stays closest to its theoretical acceleration upper bound in memory-bounded scenarios. During prefill, the frontier transitions from static depth at low quality loss (0\%--4\%), to dynamic depth at moderate loss (5\%--16\%), and finally to static width pruning at higher loss levels (17\%--26\%). These findings establish the first unified view of the practical limits of pruning-based LLM acceleration and provide guidance for future pruning research. Code is available at https://github.com/EIT-NLP/LLM-Pruning/tree/main/PruningInferSim

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Haozhe Hu, Hao Wu, Anhao Zhao, Longwei Ding, Peiran Yin, Yunpu Ma, Xiaoyu Shen
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/EIT-NLP/LLM-Pruning/tree/main/PruningInferSim](https://github.com/EIT-NLP/LLM-Pruning/tree/main/PruningInferSim)
- 阅读深度：metadata
