---
title: "Fewer Heads, Fewer Memories: Pruning Redundant Attention Heads Suppresses Verbatim Memorisation"
description: "Large language models have been shown to memorise and reproduce verbatim sequences from their training data, raising concerns about privacy leakage, intellectual property exposure, and the limits of generalisation."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.40974) · [PDF](https://arxiv.org/pdf/2610.40974)

## 一句话摘要

Large language models have been shown to memorise and reproduce verbatim sequences from their training data, raising concerns about privacy leakage, intellectual property exposure, and the limits of generalisation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models have been shown to memorise and reproduce verbatim sequences from their training data, raising concerns about privacy leakage, intellectual property exposure, and the limits of generalisation. Recent theoretical work suggests that attention heads may contribute to this behaviour by functioning as associative memory mechanisms, with memorisation capacity scaling with the number of heads. At the same time, empirical work has shown that many attention heads are redundant and can be pruned with limited impact on downstream performance. Despite these parallel findings, the effect of pruning redundant heads on memorised-sequence reproduction remains unexplored. In this work, we demonstrate that zeroing out a substantial fraction of attention heads prior to inference can significantly suppress verbatim memorisation while preserving, or even improving, language modelling performance on the benchmark used to identify redundant heads. Evaluating GPT-2-XL(1.5B) on known memorised sequences, we find that pruning 729 task-redundant heads reduces the memorisation count by 91.5%, while improving WikiText-103 perplexity by 0.92. These findings suggest that attention-head redundancy can be exploited to mitigate memorisation at inference time, without retraining or modifying the training data.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aryan Chowdhury, Riza Batista-Navarro
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
