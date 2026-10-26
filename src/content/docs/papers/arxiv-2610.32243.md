---
title: "BiLoCo: Binary Low-Rank Corrections for Post-Training Quantization"
description: "Post-training quantization (PTQ) to FP4 has emerged as a key technique for reducing large language model inference cost, especially on Blackwell GPUs, which offer native FP4 tensor core support."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.32243) · [PDF](https://arxiv.org/pdf/2610.32243)

## 一句话摘要

Post-training quantization (PTQ) to FP4 has emerged as a key technique for reducing large language model inference cost, especially on Blackwell GPUs, which offer native FP4 tensor core support.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization (PTQ) to FP4 has emerged as a key technique for reducing large language model inference cost, especially on Blackwell GPUs, which offer native FP4 tensor core support. Direct PTQ to FP4, however, still leaves a noticeable accuracy gap. Recent work on SVDQuant mitigates the errors introduced through FP4 quantization for diffusion models by adding high-precision low-rank corrections obtained via SVD. However, this high-precision low-rank correction requires many bits per rank, and it runs on the same tensor cores as the main FP4 GEMM. We introduce BiLoCo, a low-rank correction method whose left and right factors are stored as binary ${\{\pm 1\}}$ sign vectors rather than as BF16 numbers. The signed format uses $16{\times}$ less storage per rank-one component, and since the correction now consists of additions/subtractions, this can be run on CUDA cores concurrently with the FP4 tensor-core GEMM. On 4B--72B LLMs, BiLoCo matches or improves memory-matched SVDQuant for PTQ. We implement BiLoCo on B300 as a fused single kernel, where the FP4 GEMM runs on tensor cores, the bit-packed correction on the CUDA cores of the same launch, and the two are combined in the GEMM epilogue. With batch size $1$, the fused kernel is at most $11\%$ slower than the FP4-only GEMM for every rank up to $512$. At rank $128$, it is at most $20\%$ slower up to batch size $8$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：David Jin, Beshr IslamBouli, Tarushii Goel, Han Guo, Yoon Kim
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
