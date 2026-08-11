---
title: "LegoLM: Structured Weight Sharing for Large Language Models"
description: "We present \\LegoLM{}, a structured weight-sharing compression framework for large language models grounded in a systematic study of why global weight sharing fails and how to fix it."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.08652) · [PDF](https://arxiv.org/pdf/2608.08652)

## 一句话摘要

We present \LegoLM{}, a structured weight-sharing compression framework for large language models grounded in a systematic study of why global weight sharing fails and how to fix it.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present \LegoLM{}, a structured weight-sharing compression framework for large language models grounded in a systematic study of why global weight sharing fails and how to fix it. We identify two distinct failure modes. Distributional mismatch: for vector blocks of dimension d <= 2, transformer layers with heterogeneous weight scales impose a scale-mismatch penalty that grows linearly with d and cannot be resolved by increasing K, producing perplexity in the millions.Outlier dominance: for scalar blocks, a fraction ~1/K of weights lies beyond the outermost Lloyd-Max decision threshold and cannot be represented by any centroid; their misrepresentation accumulates across layers, causing catastrophic quality loss. \LegoLM{} resolves both failure modes via three data-free adaptations: 1 scalar-block encoding to eliminate the $d$-linear mismatch component, 2 percentile-selective replacement that identifies and preserves outlier weights verbatim, and 3 boundary-layer protection for the first and last transformer blocks. Across GPT-2 small (124M) and Mistral-7B, \LegoLM{} achieves +0.03% PPL degradation at 4.41X compression on Mistral-7B - outperforming PTQ-8bit in both quality and compression ratio - and -0.02% at 2.67X. Downstream evaluation on LAMBADA and HellaSwag confirms that \LegoLM{} at K=64, p=99% preserves accuracy within noise at 5.12 X compression, exceeding PTQ-8bit's compression ratio while matching its accuracy. We further discover that outlier dominance grows with model scale: full replacement at K=128 degrades GPT-2 small by only +23% but catastrophically degrades Mistral-7B by +1,134,279%, while selective replacement at p=99% rescues both models to under +15%. A controlled ablation confirms that selective replacement is the dominant mechanism: adding it to per-layer K-means also yields near-lossless quality, matching \LegoLM{} within 0.02%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: weight sharing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Joseph Bingham
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
