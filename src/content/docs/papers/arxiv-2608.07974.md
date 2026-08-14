---
title: "ZeroLock: Concurrent Memory-Efficient LLM Training via Modular Update Decoupling"
description: "Large language model (LLM) fine-tuning at the edge adapts the model to scenario-specific data while preserving privacy."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2608.07974) · [PDF](https://arxiv.org/pdf/2608.07974)

## 一句话摘要

Large language model (LLM) fine-tuning at the edge adapts the model to scenario-specific data while preserving privacy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) fine-tuning at the edge adapts the model to scenario-specific data while preserving privacy. Although existing studies proposed pipeline parallelism to address the limited memory and computing resources of edge devices, they commonly rely on backpropagation (BP) training, which has a fundamental limitation of update locking and could experience severe throughput and memory bottlenecks. In this work, we propose a BP-free algorithm, called ZeroLock, that decouples the model updates into independent chunk updates by local objective construction. It breaks the update locking of BP and hence can improve throughput at the algorithm level and lower memory usage by reducing activation storage. To the best of our knowledge, we provide the first theoretical framework for such local objective construction-based approaches under general model chunk division by mapping local objectives to the global objective. We prove that ZeroLock has a convergence rate of $\tilde{\mathcal{O}}(1/\sqrt{T})$, which differs from BP only by polylogarithmic factors. We design a system for ZeroLock and build real-world prototypes, incorporating techniques such as early forwarding and failure recovery for efficient and robust implementation. Experiments on the prototype show that compared to BP-based baselines, ZeroLock reduces the memory by 26.5% and improves throughput by 4.9%.

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

- taxonomy keywords: failure recovery
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Wentao Dai, Xuanran Li, Yuxiang Zhang, Ming Tang, Chao Huang
- 发布：2026-08-08；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
