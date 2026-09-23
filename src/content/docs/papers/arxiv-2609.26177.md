---
title: "Magnitude Profile Pruning: Calibration-Free Structured Attention Head Removal for Transformer Compression"
description: "Structured pruning of attention heads provides a hardware-friendly way to compress Transformer language models."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.26177) · [PDF](https://arxiv.org/pdf/2609.26177)

## 一句话摘要

Structured pruning of attention heads provides a hardware-friendly way to compress Transformer language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning of attention heads provides a hardware-friendly way to compress Transformer language models. However, existing methods for measuring head-level importance require calibration data, gradient computation, or Hessian estimation. These requirements add extra overhead and make the methods depend on the data. Our work presents Magnitude Profile (MP) scoring, a training-free criterion for head importance that identifies dispensable heads through statistical outlier detection on weight row norms. Heads whose projection weights fall within the population bulk are pruned, while heads exhibiting outlier norms, which carry disproportionate representational capacity, are preserved. Our work further gives MP-G, a variant that handles Grouped Query Attention (GQA) by distributing shared key-value group scores across associated query heads. Across five models evaluated on WikiText-2 perplexity at 12.5%-50% head sparsity, MP-G achieves the best perplexity on OPT-6.7B at all sparsity levels (18.46 at 12.5%, 27.87 at 25%, 152.0 at 50%). MP-G also gives the best results on RoBERTa-large at 12.5% and 25% sparsity, with perplexity values of 7.27 and 10.28, outperforming calibration-dependent baselines including Wanda-Head, SparseGPT-Head, and Gradient-Head. It requires zero forward passes, calibration samples, or gradient computation. At 50% sparsity, head pruning yields up to 16% parameter reduction with 50% attention FLOP savings. Our results show that weight-only statistical scoring can match or outperform data-dependent methods for structured head pruning, providing a practical, zero-cost criterion for Transformer compression.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kasun Dewage, Marianna Pensky, Heranga K. Rathnasekara, Suranadi De Silva
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
