---
title: "Who Speaks for the Pruned? Visual Token Pruning as Coverage Optimization"
description: "Visual token pruning reduces the inference cost of vision-language models (VLMs), but most methods only ask which tokens to keep."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.03158) · [PDF](https://arxiv.org/pdf/2609.03158)

## 一句话摘要

Visual token pruning reduces the inference cost of vision-language models (VLMs), but most methods only ask which tokens to keep.

## 为什么值得关注

待编辑增强。

## 摘要原文

Visual token pruning reduces the inference cost of vision-language models (VLMs), but most methods only ask which tokens to keep. This retained-token view can keep redundant high-scoring tokens while leaving discarded evidence without a close representative. We propose CoverPruner, a training-free pruner that asks the complementary demand-side question: after a token is removed, which surviving original token represents it for the target VLM? CoverPruner formulates pruning as Representational Coverage Maximization (RCM), covering the full projected visual-token set with query-weighted demand. It instantiates RCM with projector-space coverage and a lightweight first-layer attention probe. Across multiple VLM architectures and compression rates, CoverPruner achieves the best average accuracy among all compared methods, with the largest gains usually appearing under aggressive compression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qingchan Zhu, Weihang You, Hanqi Jiang, Changdi Yang, Tianming Liu, Geng Yuan
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
