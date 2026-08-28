---
title: "Beyond Dense Adam States: Adaptive Log-Space Quantization for Memory-Efficient Optimizers"
description: "Low-precision optimizer-state methods are commonly designed and evaluated for dense Adam-style first and second moments."
---

**评分：57/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.22322) · [PDF](https://arxiv.org/pdf/2608.22322)

## 一句话摘要

Low-precision optimizer-state methods are commonly designed and evaluated for dense Adam-style first and second moments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-precision optimizer-state methods are commonly designed and evaluated for dense Adam-style first and second moments. Memory-efficient optimizers depart from this setting: Adafactor factorizes second moments, CAME adds factored confidence states, and APOLLO maintains statistics in a projected gradient space. Consequently, an equal amount of state reconstruction error can induce different update errors depending on state topology and update semantics. We first characterize this heterogeneity in optimizer-state traces from language model pre-training. We then introduce Adaptive Log-Space (AL) quantization, a block-wise representation for non-negative states that adapts its nonzero range per block and enforces the exact-zero invariant $q = 0 \Leftrightarrow x = 0$. AL8 and AL16 are combined with independent signed-momentum encodings and state-specific precision choices rather than a single policy for every state. Across 96 runs totaling 214.7 GPU-hours, we evaluate dense, factored, confidence, and projected states in AdamW, Adafactor, CAME, and APOLLO paths. On a 20K-step TinyLlama-1.1B pre-training benchmark, an AdamW configuration with AL8 second moments and uniform 8-bit momentum reaches 72.90 perplexity, compared with 72.48 for FP32 AdamW and 73.54 for an 8-bit dynamic-quantization baseline, while reducing measured optimizer-state storage from 8392.7 to 2119.2 MiB. CAME exposes a different precision regime: promoting its non-negative states to AL16 recovers 86.16 perplexity versus 86.68 for the full-precision reference, whereas all-AL8 reaches 90.19. A 100K-step GPT-2 experiment further shows that topology-aware parameter protection reduces the late-loss gap of quantized Adafactor from +0.1185 to +0.0159 in the evaluated setup. These results support a state- and topology-aware view of optimizer quantization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 7 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yan Wang
- 发布：2026-08-23；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/yanfeiwong/adafactor-8bit](https://github.com/yanfeiwong/adafactor-8bit)
- 阅读深度：metadata
