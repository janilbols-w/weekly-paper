---
title: "User-Schedulable Approximations for Quantized Tensor Programs"
description: "Quantization lets language models run on edge devices, but it sharply increases the number of tensor kernels a library must maintain: every weight format must be paired with every activation format on every instruction set and GPU, with an encoder and a decoder that agree on the stored bytes."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.17526) · [PDF](https://arxiv.org/pdf/2611.17526)

## 一句话摘要

Quantization lets language models run on edge devices, but it sharply increases the number of tensor kernels a library must maintain: every weight format must be paired with every activation format on every instruction set and GPU, with an encoder and a decoder that agree on the stored bytes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization lets language models run on edge devices, but it sharply increases the number of tensor kernels a library must maintain: every weight format must be paired with every activation format on every instruction set and GPU, with an encoder and a decoder that agree on the stored bytes. In GGML, the tensor library used by llama.cpp, these kernels are written by hand, and only 8 of the 54 weight-activation pairs it runs on our Arm CPU have a tiled matrix-multiplication kernel. We extend Halide's separation of algorithm and schedule to the representation of values. Each approximation is a codec, an encoder paired with a decoder, composed from reusable units: quantizers, integer representations, bit packers and layouts. A new directive, approximate_by, applies a codec to one stage of a program and returns the encoder and decoder as ordinary stages that Halide can schedule, so both decoders fuse into the register tiles of a matrix product. Optional contracts, such as a round-trip law, are checked by property tests; the law exposed an inconsistent block sum in GGML's q8_1. One algorithm and one schedule library generate 347 kernels for 31 of GGML's and KleidiAI's formats on Arm CPUs and Apple GPUs, covering 38 weight-activation pairs for which GGML has no kernel, in 3.7x less code than GGML and KleidiAI. On an Apple M3 Max, our kernels reach at least 95% of the speed of GGML's format-specific kernels in 91.0% of the cases that have one, with a median speedup of 1.13x, and are faster still where GGML falls back to blocked dot products. Counting Apple's BLAS library, which is usually faster for larger f32 products, we still reach that threshold in 86.9% of CPU cases. A port to x86 with Intel's AMX adds 793 lines of code and matches GGML in 83.5% of its cases.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Alex Reinking
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
