---
title: "Reservoir of Importance: Learning Semi-Structured Sparsity with Differentiable Subset Sampling"
description: "Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs)."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.23048) · [PDF](https://arxiv.org/pdf/2608.23048)

## 一句话摘要

Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs). However, existing learnable-mask approaches incur substantial parameter and memory overhead, limiting their scalability to large models and aggressive sparsity regimes. In this work, we revisit semi-structured pruning from a perspective that reconciles efficiency with scalability. We propose Reservoir of Importance (RoI), a lightweight semi-structured pruning framework that learns sparsity masks through differentiable subset sampling. Unlike prior methods that model full categorical distributions over all feasible $N$:$M$ patterns, RoI introduces a compact-logit parameterization for sparsity mask learning and performs sampling without replacement to select masks, thereby reducing trainable parameters from combinatorial complexity to $\mathcal{O}({M})$. As a result, RoI requires 1.5-8.75$\times$ fewer learnable parameters and significantly lower memory cost, while remaining fully aligned with hardware-friendly sparsity patterns. Extensive evaluations across multiple scales of the Qwen2.5 LLM family (0.5-7B parameters) demonstrate that RoI achieves competitive performance with strong memory efficiency, stability, and scalability to more aggressive $N$:$M$ sparsity patterns, offering a practical path toward efficient LLM deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ha Dinh, Xuan Duy Ta, Khoat Than, Khac-Hoai Nam Bui
- 发布：2026-08-24；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
