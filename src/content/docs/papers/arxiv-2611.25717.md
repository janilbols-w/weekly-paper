---
title: "VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin"
description: "In recent years, GPUs have incorporated increasingly specialized support for low-precision computation, from Hopper's FP8 to Blackwell's FP4 Tensor Cores."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2611.25717v1) · [PDF](https://arxiv.org/pdf/2611.25717v1)

## 一句话摘要

In recent years, GPUs have incorporated increasingly specialized support for low-precision computation, from Hopper's FP8 to Blackwell's FP4 Tensor Cores.

## 为什么值得关注

待编辑增强。

## 摘要原文

In recent years, GPUs have incorporated increasingly specialized support for low-precision computation, from Hopper's FP8 to Blackwell's FP4 Tensor Cores. Precision formats have evolved alongside this hardware, from MXFP4 and NVFP4 on Blackwell to E2M1 FP4 with direct UE5M3 block scaling on Vera Rubin, which we term as $\boldsymbol{VRFP4}$. These advances help serve larger language models at lower cost, but four-bit activation quantization can substantially degrade model quality. We introduce VR-SparseQuant, which uses Vera Rubin's elementwise 2:4 sparsity to recover accuracy while retaining native FP4 execution. By allowing two sparse streams to overlap, we use the same FP4 value budget as dense quantization to refine activations with larger errors. Offline scale-ratio calibration avoids runtime search, while a shared-weight GEMM accumulates both streams efficiently. On Nemotron-3-Nano-30B-A3B, VR-SparseQuant reduces WikiText-2 perplexity from $\boldsymbol{6.85}$ to $\boldsymbol{5.57}$ versus dense RTN W4A4. Including activation preparation, our native Rubin kernels for VRFP4 achieve up to $\boldsymbol{3.1\times}$ GEMM and $\boldsymbol{2.7\times}$ MoE speedup over BF16. To the best of our knowledge, this is the first study of adaptive activation quantization using Vera Rubin's elementwise 2:4 structured sparse FP4 instructions.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, fp8, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Samir Khaki, Wei-Chen Wang, Song Han, Ryan Hanrui Wang
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
