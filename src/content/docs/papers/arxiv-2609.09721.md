---
title: "EFQ-Softmax: Exp-Free Quantization for Softmax"
description: "Low-bit attention accelerates Transformer inference by moving the $QK^\\top$ and $PV$ matrix multiplications to FP8 or FP4 matrix engines."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.09721) · [PDF](https://arxiv.org/pdf/2609.09721)

## 一句话摘要

Low-bit attention accelerates Transformer inference by moving the $QK^\top$ and $PV$ matrix multiplications to FP8 or FP4 matrix engines.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-bit attention accelerates Transformer inference by moving the $QK^\top$ and $PV$ matrix multiplications to FP8 or FP4 matrix engines. However, the softmax path often evaluates shifted-score exponentials in higher precision, forms a temporary probability block, and quantizes it before low-bit $PV$ multiplication. This exp-then-quantize path creates a mismatch between a high-precision probability producer and a low-bit matrix consumer. We propose EFQ-Softmax (Exp-Free Quantization for Softmax), a low-bit probability-generation method that directly maps shifted attention scores to block-scaled E2M1 operands. For each microscaling block, EFQ-Softmax selects an exponent-only scale from the local maximum, maps the shifted scores to a normalized residual domain, and generates nonnegative E2M1 probability codes using a single affine rule. The resulting operand is used consistently in both the $\widetilde{P}V$ numerator update and the $\widetilde{P}\mathbf{1}$ denominator update. The FlashAttention-style row-maximum update, historical rescaling, high-precision accumulation, and final normalization remain unchanged. We evaluate end-to-end quality on Qwen3-8B, Qwen3-VL-8B-Instruct, and WAN2.2-TI2V-5B, and separately measure kernel-level performance on the A5 vector unit. EFQ-Softmax improves the Qwen3-8B seven-task mean from 0.6749 with MXFP4 to 0.6773 and the Qwen3-VL nine-task mean from 0.7826 to 0.8000. On WAN2.2, it maintains temporal consistency and visual quality comparable to the FP16 and MXFP4 baselines under VBench. On the A5 vector unit, EFQ-Softmax reduces the vector-stage latency of the fused probability-generation kernel by 40.33% on average across sequence lengths from 16K to 128K. These results show that direct low-bit probability generation can replace the conventional exp-then-quantize path while preserving end-to-end model quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, microscaling, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haohui Han, Yuming Wan, Hongni Wang, Pengcheng Xie, Xiaodong Yan, Runqi You, Wencong Zhang
- 发布：2026-09-09；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
