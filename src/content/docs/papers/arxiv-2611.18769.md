---
title: "Gradient-Guided Hardware-Native MIXFP4"
description: "Blackwell tensor cores support native inference with 4-bit weights and activations (W4A4), but NVFP4 leaves a perplexity (PPL) gap to BF16."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.18769) · [PDF](https://arxiv.org/pdf/2611.18769)

## 一句话摘要

Blackwell tensor cores support native inference with 4-bit weights and activations (W4A4), but NVFP4 leaves a perplexity (PPL) gap to BF16.

## 为什么值得关注

待编辑增强。

## 摘要原文

Blackwell tensor cores support native inference with 4-bit weights and activations (W4A4), but NVFP4 leaves a perplexity (PPL) gap to BF16. Choosing a format for each 16-element block can improve accuracy, but current matrix multiply instructions cannot execute choices this fine. Applying these rules at hardware-compatible tiles loses most of their benefit. We introduce FlipQuant, which selects E2M1 or E0M3 for each MMA weight tile. It keeps both quantized weight candidates fixed and learns a binary format map from end-to-end gradients of a bucketed KL loss to a BF16 teacher, re-evaluating them after each update. Native kernels execute 16 x 64 tiles on SM120 and 256 x 64 tiles on SM100 with median GEMM overheads of 1.9% and 1.7%, respectively. Across six language models and two corpora, FlipQuant at 16 x 64 closes 42.5% of NVFP4's PPL gap to BF16 on average, compared with 13.3% for FourOverSix. Code is available at https://github.com/brian030128/flipquant.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jian-Jia Chen, Brian J. Chan, Wen-Hung Lee, Yi-Ting Li, Po-Shen Chen, Kuan-Te Kuo, Hsien-Cheng Huang, Cody Hao Yu, Chi-Chih Chang, Mohamed S. Abdelfattah, Kai-Chiang Wu
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/brian030128/flipquant](https://github.com/brian030128/flipquant)
- 阅读深度：metadata
