---
title: "Heterogeneity-Aware Microscaling for Efficient Low-Bit LLM Inference"
description: "Microscaling (MX) is now the standard for low-bit large language model (LLM) inference."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.03867) · [PDF](https://arxiv.org/pdf/2608.03867)

## 一句话摘要

Microscaling (MX) is now the standard for low-bit large language model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Microscaling (MX) is now the standard for low-bit large language model (LLM) inference. Its 4-bit form MXFP4 still loses substantial accuracy, because existing MX formats fix either the element format or the precision-recovery scheme across blocks, and thus capture only limited quantization heterogeneity. Quantization heterogeneity appears at two levels: 1) across blocks, the preferred element format and precision-recovery scheme vary; 2) across operands, weights and activations require different encoding. We introduce AdaMX (Adaptive Microscaling), a heterogeneity-aware format and accelerator. It selects the precision-recovery scheme per block and the representation per operand, at no increase in equivalent bit width (EBW). One design covers two block sizes, giving a higher-accuracy operating point and a lower-EBW operating point that saves storage. We implement a 22nm FD-SOI AI accelerator prototype with the proposed decoder, computing unit, and quantization logic. Against an otherwise identical MXFP4 accelerator with FP4-only multipliers, AdaMX adds about 1% system energy. At the lower-EBW point, AdaMX stays more accurate than the baseline while lowering both memory footprint and energy. Across LLMs from 3B to 70B, AdaMX removes 83% of the MXFP4 accuracy loss on commonsense and 82% on MMLU, and 43% and 27% of the NVFP4 loss. AdaMX also generalizes to multimodal models. On Gemma-4 12B, it leads MXFP4 on all four vision-language benchmarks and keeps up to 96% of FP16 accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, microscaling, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junyi Luo, Xinting Jiang, Tai-Hao Wen, Ruichen Qi, Minxing Chu, Hongyi Wu, Gregory Kielian, Ben Laurie, Qirui Zhang, Quan Cheng, Dennis Sylvester, Mehdi Saligane
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
