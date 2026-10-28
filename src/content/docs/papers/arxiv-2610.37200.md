---
title: "PipeLink: Contract-Guided Linking of GPU Kernel Components"
description: "The fastest machine-learning kernels are compositions of components, such as loaders, matrix-multiply mainloops, epilogues and communication stages, that run concurrently on one GPU streaming multiprocessor and share its on-chip memory, barriers, warps and registers."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2610.37200) · [PDF](https://arxiv.org/pdf/2610.37200)

## 一句话摘要

The fastest machine-learning kernels are compositions of components, such as loaders, matrix-multiply mainloops, epilogues and communication stages, that run concurrently on one GPU streaming multiprocessor and share its on-chip memory, barriers, warps and registers.

## 为什么值得关注

待编辑增强。

## 摘要原文

The fastest machine-learning kernels are compositions of components, such as loaders, matrix-multiply mainloops, epilogues and communication stages, that run concurrently on one GPU streaming multiprocessor and share its on-chip memory, barriers, warps and registers. Because these components hard-code where they sit in this shared space, they cannot be compiled, shipped or replaced on their own: combining components from different sources means forking them by hand or keeping them in separate kernels. We present PipeLink, a contract-guided linker for GPU kernel components. Each component is compiled separately into an LTO object that carries a contract stating what it requires and what it promises; PipeLink checks the contracts against each other, relocates every component by solving one joint placement of the SM's resources, and generates the transfers between them, and the vendor LTO backend folds the result into constants. Across 51 configurations on Hopper and Blackwell GPUs, linked kernels run within 0.2% of the same sources compiled as one unit. Linking makes new compositions practical: a CuTe attention operator inside a ThunderKittens decode megakernel speeds up decoding by 2.16$\times$, a four-owner MoE training megakernel matches the original monolith, one unchanged attention core yields sparse and context-parallel variants that outperform FlexAttention, vLLM and Transformer Engine, and a GEMM + SwiGLU composition whose consumer serves three GPU architectures runs 1.2$\times$ faster on Blackwell than cuBLAS with a compiled activation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jize Guo, Xupeng Miao
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
