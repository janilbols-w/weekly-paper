---
title: "Tetra: Serving Leech-Lattice Quantized LLMs at 2.7 Bits per Parameter"
description: "Leech-lattice quantization gives good quality at two bits per weight, but its codebooks hold more than 10^14 points, too many for a lookup table."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.35465) · [PDF](https://arxiv.org/pdf/2609.35465)

## 一句话摘要

Leech-lattice quantization gives good quality at two bits per weight, but its codebooks hold more than 10^14 points, too many for a lookup table.

## 为什么值得关注

待编辑增强。

## 摘要原文

Leech-lattice quantization gives good quality at two bits per weight, but its codebooks hold more than 10^14 points, too many for a lookup table. Our earlier kernel expanded the codes at load time and read 4.804 bits per weight from GPU memory for 2 bits of code. We present Tetra, a new codebook on the same lattice. A 24-weight block still takes 48 bits, most of which index a 64-state trellis of the Golay code and one shared 16 KiB table. The kernel decodes a block with six table loads and two small lookups inside the matrix-vector product, and reads 2.148 bits per weight. For full models, we retrain one scale per matrix row, store the matrices that lose the most as 4-bit integers, and pay for them with 4-bit embedding tables. Our Qwen3-4B, 8B and 14B files hold 2.73, 2.70 and 2.73 bits per parameter over the whole model. They score 63.37, 69.58 and 75.66 on the full MMLU test set, 4.76, 4.21 and 2.46 points below 4-bit AWQ at 5.3 to 6.0 bits per parameter. They generate 113.8, 95.0 and 57.2 tokens per second in our engine. On GSM8K, through the served kernel, they lose 9.63, 4.62 and 3.26 points to FP16. At 4B our file scores 23.6 points above llama.cpp's IQ2_XXS (2.48 bits per parameter). Every number we measured for a table or figure comes from one NVIDIA L40S GPU. We preregistered the main experiments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Pier-Jean Malandrino
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/pjmalandrino/llvq](https://github.com/pjmalandrino/llvq)
- 阅读深度：metadata
