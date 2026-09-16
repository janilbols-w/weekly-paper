---
title: "Forward-Free LLM Depth Pruning via Weight Redundancy"
description: "Depth pruning reduces large language model (LLM) inference cost by removing complete Transformer blocks."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.09883) · [PDF](https://arxiv.org/pdf/2609.09883)

## 一句话摘要

Depth pruning reduces large language model (LLM) inference cost by removing complete Transformer blocks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Depth pruning reduces large language model (LLM) inference cost by removing complete Transformer blocks. Activation-based methods collect hidden states through forward passes on calibration data, while existing forward-free methods score each Transformer block separately without measuring similarity between blocks. We propose Weight-Redundancy Pruning (WRP), a forward-free depth-pruning method that estimates inter-layer redundancy from checkpoint weights to select blocks without calibration data or model forward passes. WRP compares attention output and MLP down-projection weights across layers and combines their pairwise similarities with relative projection-scale information. The resulting all-pairs similarity matrix guides layer grouping and block selection. Across multiple pruning settings, model families, and downstream tasks, WRP consistently outperforms existing forward-free magnitude pruning and approaches the performance of activation-based methods.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vincent-Daniel Yun, Woosang Lim
- 发布：2026-09-09；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
