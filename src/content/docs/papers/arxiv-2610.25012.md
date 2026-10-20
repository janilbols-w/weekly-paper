---
title: "Conjugate Compilation: Self-Improving Agentic Co-Compilation for Speculative Decoding"
description: "As LLM adoption surges, scaling model serving requires unlocking stranded GPU capacity alongside deploying more GPUs."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.25012) · [PDF](https://arxiv.org/pdf/2610.25012)

## 一句话摘要

As LLM adoption surges, scaling model serving requires unlocking stranded GPU capacity alongside deploying more GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

As LLM adoption surges, scaling model serving requires unlocking stranded GPU capacity alongside deploying more GPUs. Speculative decoding brings two models into the serving process: a small draft model proposes tokens that a larger target model verifies. Yet compiling these models individually leaves their shared execution outside the compiler's optimization boundary. We introduce CONJUGATE COMPILATION, which reframes speculative decoding as a cross-model compilation problem and jointly optimizes the draft and target models within their shared execution rather than treating each in isolation. Our key insight is that cross-model compilation should be informed by the measured performance of the co-located shared execution it produces: an optimization that improves a kernel in isolation need not improve the models when they execute together. To expand cross-model opportunities, we devise operand layouts that interleave blocks from both models within common tiles, co-locating GEMM and non-GEMM work while preserving their mathematics. We realize CONJUGATE COMPILATION through a self-improving agentic search system in which an LLM edits cross-model optimization plans using the compiler and GPU execution as its environment. Each proposed plan is compiled and evaluated through its co-located shared execution, whose measured score, together with kernel-level verdicts and compiler feedback, informs subsequent proposals, while Monte Carlo tree search accumulates rewards to guide exploration. Across six single-GPU speculative-decoding configurations on NVIDIA B300 and RTX 5090 GPUs, CONJUGATE COMPILATION achieves a geometric-mean per-round speedup of 1.37x over conventional execution. Interleaved kernels raise this speedup to 1.45x, reaching 1.59x in the best case. CONJUGATE COMPILATION also improves GPU utilization on average by 1.46x on RTX 5090 and 1.50x on B300.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Annabelle Sujun Tang, Rohan Mahapatra, Christopher Priebe, Hanyang Xu, Manya Ghobadi, Christopher Rossbach, Hadi Esmaeilzadeh
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
