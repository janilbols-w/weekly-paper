---
title: "Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference"
description: "Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.13205) · [PDF](https://arxiv.org/pdf/2607.13205)

## 一句话摘要

Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest. On schema-dense input streams such as nested JSON, this score acts as a non-stationary filter that disproportionately retains noise: a non-content sink role (delimiters or whitespace) carries an order of magnitude more energy than any content role, and structural KEY tokens are over-retained at roughly 1.8x the rate of the answer-carrying VALUE tokens, collapsing exact-match accuracy from 88% to 0% at a 5% budget as the signal-to-noise ratio of the retained state degrades. A counterfactual experiment establishes that suppressing KEY tokens is the best deployable filter. Our retraining-free, role-conditional allocation over SnapKV's windowed score, governed by a single tuned hyperparameter, closes 63-98% of the H2O gap at sub-20% budgets and, at higher budgets, modestly matches or exceeds full-cache accuracy -- a small, seed-sensitive denoising effect (borderline significant at B=0.50; not distinguishable from zero at B=0.30 over four seeds). A 15 MB linear role probe supplies these labels at negligible inference cost, though matching parser-level downstream accuracy remains open.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Soumil Mandal
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
