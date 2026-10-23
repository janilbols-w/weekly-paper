---
title: "FIGFLEX: A Mixed-Precision FP-INT GEMM Accelerator Co-Designed with Low-Bit LLM Quantization"
description: "Weight-only quantization keeps LLM activations in floating point and stores weights as low-bit integers, turning the dominant workload into floating-point-integer (FP-INT) general matrix multiplication."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.30480) · [PDF](https://arxiv.org/pdf/2610.30480)

## 一句话摘要

Weight-only quantization keeps LLM activations in floating point and stores weights as low-bit integers, turning the dominant workload into floating-point-integer (FP-INT) general matrix multiplication.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight-only quantization keeps LLM activations in floating point and stores weights as low-bit integers, turning the dominant workload into floating-point-integer (FP-INT) general matrix multiplication. Recent quantizers reach a 2-3-bit average with mixed precision, but hardware has not kept pace: GPUs dequantize weights to FP16 before the tensor-core multiply-accumulate, and bit-parallel FP-INT accelerators run at a single weight precision, so fewer bits save memory but not computation. In this paper, we present FIGFLEX, an algorithm-hardware co-designed mixed-precision accelerator whose bit-parallel datapath scales throughput as precision falls. FIGFLEX contributes (1) a shift-add, radix-4 reformulation of FP-INT multiplication that fuses the multiply-accumulate into a unified, precision-flexible partial-product reduction and roughly halves the partial products, together with a novel INT3 optimization that reclaims the idle datapath radix-4 leaves at that precision; and (2) a mixed-precision quantizer that assigns each channel group its bit-width according to the error GPTQ cannot compensate, with a per-input-channel column scaling whose power-of-two normalization keeps the scaled activations out of the FP16 subnormal range, so that the quantized model maps directly onto FIGFLEX's datapath with the same accuracy as on a GPU. On LLaMA-2-7B, FIGFLEX attains 5.85 and 8.77 WikiText-2 perplexity at 3- and 2-bit average precision, lower than GPTQ, AWQ, SliM-LLM, AMQ, and QuIP# (without fine-tuning), while delivering 1.56x and 1.42x higher whole-chip throughput per area on the linear GEMMs of a 3-bit mixed-precision model than AxCore and FIGLUT, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Faraz Tahmasebi, Haocheng Xu, Andrew Trauger, Yomal Perera, Zhenyu Tang, Nael Chowdhury, Sitao Huang
- 发布：2026-10-23；更新：2026-10-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
