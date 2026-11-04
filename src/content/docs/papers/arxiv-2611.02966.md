---
title: "SHq: Learnable Grids for LLM Weight Quantization"
description: "Block-scaled lookup-table (LUT) formats, which represent weights as indices into a small value set (the grid), have become standard for low-bit LLM quantization, ranging from NF4 and BOF4 to the 3-bit LUT instruction in NVIDIA Rubin."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.02966) · [PDF](https://arxiv.org/pdf/2611.02966)

## 一句话摘要

Block-scaled lookup-table (LUT) formats, which represent weights as indices into a small value set (the grid), have become standard for low-bit LLM quantization, ranging from NF4 and BOF4 to the 3-bit LUT instruction in NVIDIA Rubin.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block-scaled lookup-table (LUT) formats, which represent weights as indices into a small value set (the grid), have become standard for low-bit LLM quantization, ranging from NF4 and BOF4 to the 3-bit LUT instruction in NVIDIA Rubin. While these formats leave the grid definition flexible, existing implementations rely on fixed grids derived either from numerical data types (INT, FP) or assumed weight distributions (NF, BOF). We demonstrate that no single fixed grid is universally optimal; the best fixed grid varies with bit-width: BOFS at 2 bits, NF at 4 and 5 bits, and INT at 6 bits. We introduce SHq, a closed-form family of grids parameterized by two critical degrees of freedom: a companding strength {\alpha} that interpolates level spacing from uniform to floating-point-like, and an offset c that introduces asymmetry. This offset allows the sign bit of the FP8 block scale, otherwise unused, to select between the grid and its mirror image, up to doubling the number of distinct values available per block. SHq modifies only the lookup table contents and serves as a drop-in replacement for the grid in any such format. Across five models ranging from 3B to 35B parameters, including a mixture-of-experts architecture, evaluated at 2-6 bits using RTN and GPTQ, SHq achieves the lowest KL divergence in every setting at 3 and 4 bits and in most settings at 2, 5 and 6 bits. It outperforms the best fixed grid by up to 34% and remains superior under mixed-precision configurations. At 4.5 bits per weight, the SHq format reduces the KL divergence of NVFP4 by 41-67% while improving downstream accuracy. Grid families incorporating both spacing and offset parameters perform comparably, whereas those lacking an offset exhibit clearly higher error, confirming that these two degrees of freedom drive the observed gains. We therefore propose SHq as the standard grid for block-scaled lookup-table formats.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Michael Helcig, Earl Killian, Dan Alistarh
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
