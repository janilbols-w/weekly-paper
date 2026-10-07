---
title: "KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization"
description: "Deep learning inference and training performance depends critically on GPU kernel efficiency."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.30059) · [PDF](https://arxiv.org/pdf/2609.30059)

## 一句话摘要

Deep learning inference and training performance depends critically on GPU kernel efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins. Recent LLM-assisted kernel optimizers can close this gap for standalone kernels, yet treat compiled models as black boxes, generally optimizing individual standalone kernels without respecting the compiler's structural decisions or verifying the model end-to-end. We present KernelOPT, a multi-agent system that treats compiled models as structured artifacts. It preserves vendor library calls (cuBLAS, cuDNN) and exclusively targets generated Triton sub-kernels using five profiling-guided LLM agents. A four-gate verification cascade applies static validation, multi-seed correctness checking, model-level float64-fallback verification, and performance gating ($\gamma{=}1.03$) to filter candidates and verify the re-stitched model end-to-end. When candidates fail verification, the system preserves the compiler baseline. The system accepts PyTorch nn Modules, standalone Triton kernels, and Helion kernels. Evaluated on 250 KernelBench problems (100 Level 1, 100 Level 2 and 50 Level 3) on NVIDIA H200, KernelOPT achieves geometric mean speedups over torch compile of 1.40$\times$ (L1), 1.15$\times$ (L2), and 1.07$\times$ (L3) across all kernels, including fallback cases. Optimized-only geomeans (excluding cases where verification gates preserve the compiler baseline) are substantially higher: 2.54$\times$ (L1: 36/100), 1.84$\times$ (L2: 23/100), and 1.37$\times$ (L3: 11/50), reflecting where the optimizer achieves meaningful leverage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aheli Poddar, Sanskar Prasad, Arindam Samanta, Subha Chakraborty, Vishal Goyal, Rohit Singh Rathaur
- 发布：2026-09-24；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
