---
title: "SPECTRA: Adaptive Execution of Speculative Decoding on a Runtime-Reconfigurable Tiled Architecture"
description: "LLM inference on edge devices is constrained by computational and memory resources, making efficient autoregressive decoding challenging."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.24847) · [PDF](https://arxiv.org/pdf/2609.24847)

## 一句话摘要

LLM inference on edge devices is constrained by computational and memory resources, making efficient autoregressive decoding challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM inference on edge devices is constrained by computational and memory resources, making efficient autoregressive decoding challenging. Speculative decoding alleviates this bottleneck by generating tokens with a smaller draft model and verifying multiple tokens in parallel with a batched target model pass. However, verification introduces a runtime-dependent intermediate regime between memory-bound general matrix-vector (GEMV) operations in decoding and compute-bound general matrix-matrix (GEMM) operations in prefill, as its arithmetic intensity varies with speculation length and acceptance rate. We present SPECTRA, a runtime-reconfigurable tiled architecture that sustains high utilization across the full speculative decoding pipeline. Within each tile, the compute engine switches between systolic execution for GEMMs and vector-lane execution for GEMVs. Across tiles, SPECTRA dynamically adapts computation parallelism by selecting tile count, kernel partitioning, and communication pattern. Both tile-level and system-level reconfiguration operate on a per-kernel basis, enabling efficient execution across these diverse regimes. Evaluated on a 20-tile FPGA prototype across the Pythia, SmolLM2, and GPT-2 families, SPECTRA achieves up to $2.09\times$ speedup from tile-level reconfiguration and a further $1.25\times$ gain from system-level adaptability over fixed designs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gabriele Tombesi, William Baisi, Je Yang, Elisavet Lydia Alvanaki, Kevin Lee, Michael Lippe, Biruk Seyoum, Luca P. Carloni
- 发布：2026-09-21；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
