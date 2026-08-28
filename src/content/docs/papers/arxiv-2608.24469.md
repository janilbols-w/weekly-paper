---
title: "Low-Rank Ternary Adaptation for Fine-Tuning Transformers"
description: "Ternary transformers offer extreme memory and compute efficiency, but existing low-bit LoRA-based methods cannot directly fine-tune ternary weights."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.24469) · [PDF](https://arxiv.org/pdf/2608.24469)

## 一句话摘要

Ternary transformers offer extreme memory and compute efficiency, but existing low-bit LoRA-based methods cannot directly fine-tune ternary weights.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ternary transformers offer extreme memory and compute efficiency, but existing low-bit LoRA-based methods cannot directly fine-tune ternary weights. Current approaches either require dequantization, restoring low-bit base weights to higher precision to merge with adaptation weight, or update only quantization parameters, preventing a merged model that remains ternary. We propose ternary multiplicative adaptation, which represents discrete updates of ternary weights such as sign flips or zeroing through a low-rank Kronecker factorization into two small ternary matrices applied element-wise to ternary weights. This design is parameter-efficient and expressive, preserves the ternary domain, and supports direct merging without dequantization. Experiments on six models across language and vision, including ternarized LLaMA-3 1B and 3B and a ternary ViT-B/16, demonstrate that our method recovers much of the performance lost to quantization and outperforms strong low-bit and ternary baselines. Code is available at https://github.com/alexmanoo/ternary_adaptation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Alexandru-Dragos Manolache, Yunqiang Li, Jan van Gemert
- 发布：2026-08-25；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/alexmanoo/ternary_adaptation](https://github.com/alexmanoo/ternary_adaptation)
- 阅读深度：metadata
