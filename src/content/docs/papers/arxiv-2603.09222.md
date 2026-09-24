---
title: "EnComp: Lightweight Encoder-Only Context Compression for Retrieval-Augmented Question Answering"
description: "Efficient context compression is critical for retrieval-augmented question answering in resource-constrained settings, where long retrieved contexts increase latency, memory use, and LLM reader cost."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.09222) · [PDF](https://arxiv.org/pdf/2603.09222)

## 一句话摘要

Efficient context compression is critical for retrieval-augmented question answering in resource-constrained settings, where long retrieved contexts increase latency, memory use, and LLM reader cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficient context compression is critical for retrieval-augmented question answering in resource-constrained settings, where long retrieved contexts increase latency, memory use, and LLM reader cost. We propose a lightweight encoder-only framework for query-driven sentence pruning that preserves answer-critical evidence while aggressively reducing irrelevant context. Our method learns marginal contribution scores for sentences using counterfactual training signals and optimizes a contrastive ranking objective that separates critical evidence from noncritical context. Our approach scores all sentences from a single full-context encoding, enabling fast inference with low computational overhead. Experiments show that it maintains accuracy comparable to the strongest baseline while using 3.7$\times$ less peak memory and achieving nearly 3$\times$ lower compression latency, demonstrating an effective quality--efficiency trade-off for practical resource-constrained deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Thao Do, Dinh Phu Tran, An Vo, Seon Kwon Kim, Daeyoung Kim
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
