---
title: "AVQ-Attention-2: Adaptive Vector-Quantized Attention with Exact Local Blocks and Linear-Cost Training"
description: "Attention costs $\\mathcal{O}(N^2)$ in the number of tokens."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.32989) · [PDF](https://arxiv.org/pdf/2611.32989)

## 一句话摘要

Attention costs $\mathcal{O}(N^2)$ in the number of tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention costs $\mathcal{O}(N^2)$ in the number of tokens. Vector-quantized attention reduces this to $\mathcal{O}(NM)$ by clustering the $N$ keys, attending to the $M$ codewords instead, and its adaptive form, AVQ-attention, concentrates codebook resolution where a query's attention mass actually falls. We present AVQ-Attention-2, a better design that merges it with exact local attention and attends to the mean of each cluster's keys rather than to a codeword. We show three improvements: consistently better quality at comparable cost; training that now also costs $\mathcal{O}(NM)$ rather than $\mathcal{O}(N^2)$; and an approximation accurate enough that the layer can be dropped into a pretrained transformer without fine-tuning. Across a variety of sequence lengths the result is competitive not merely with other approximate attention but with exact dense attention, running faster than FlashAttention at little to no loss in quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Winfried van den Dool, Patrick Forré, Amir Habibian, Yuki M. Asano, Max Welling
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
