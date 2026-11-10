---
title: "ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training"
description: "Quantization-aware training (QAT) is the most reliable way to obtain accurate low-bit large language models (LLMs), but training with AdamW keeps two dense FP32 states for every weight matrix."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.08924) · [PDF](https://arxiv.org/pdf/2611.08924)

## 一句话摘要

Quantization-aware training (QAT) is the most reliable way to obtain accurate low-bit large language models (LLMs), but training with AdamW keeps two dense FP32 states for every weight matrix.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization-aware training (QAT) is the most reliable way to obtain accurate low-bit large language models (LLMs), but training with AdamW keeps two dense FP32 states for every weight matrix. We find that low-rank memory-efficient optimizers such as GaLore and LDAdam degrade substantially in QAT. A considerable part of the QAT momentum lies outside its top-r singular subspace, and projection-based methods discard this part at every step. We further observe that this residual remains useful when only its sign is kept. Based on these observations, we propose ResQAdam. It keeps a single BF16 momentum, applies Adam only to the r x r coordinates of the principal subspace, and adds a normalized sign update computed from the residual. We evaluate ResQAdam with two from-scratch QAT methods and three QAT fine-tuning pipelines, with weights quantized down to 2 bits. It reduces optimizer-state memory by 71% to 74% relative to AdamW, stays close to AdamW in most settings, and lowers training throughput by less than 2%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Liqun Ma, Shengkun Tang, Liangyu Wang, Lin Zhao, Wei Luo, Xinjun Niu, Spandan Tiwari, Ashish Sirasao, Kun Zhang, Zhiqiang Shen
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
