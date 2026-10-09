---
title: "DynaTE: Accelerating Diffusion LLMs via Dynamic Token Execution"
description: "Diffusion-based LLMs (dLLMs) have recently emerged as a promising alternative to autoregressive (AR) LLMs by enabling bidirectional parallel refinement, alleviating the sequential decoding bottleneck of AR generation."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.11284) · [PDF](https://arxiv.org/pdf/2610.11284)

## 一句话摘要

Diffusion-based LLMs (dLLMs) have recently emerged as a promising alternative to autoregressive (AR) LLMs by enabling bidirectional parallel refinement, alleviating the sequential decoding bottleneck of AR generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Diffusion-based LLMs (dLLMs) have recently emerged as a promising alternative to autoregressive (AR) LLMs by enabling bidirectional parallel refinement, alleviating the sequential decoding bottleneck of AR generation. However, their parallel iterative refinement mismatches AR accelerators optimized for sequential decoding and their discrete token generation differs from DiT accelerators designed for continuous denoising. Recent dLLM accelerators have explored workload-specific optimizations to reduce vocabulary processing overhead and redundant computation across denoising iterations. However, these approaches retain all tokens in parallel execution, despite varying token refinement utility and execution requirements. This paper presents DynaTE, a hardware--software co-design architecture that dynamically adapts accelerator execution to evolving token states during dLLM decoding. DynaTE first enables adaptive token execution by skipping low-utility token computation, while a dimension-reconfigurable PE array maintains high utilization under varying active-token patterns. Second, DynaTE exploits dynamic token dependencies through FLDD to refine a small number of locally dependent tokens within the current iteration, reducing the overall number of denoising iterations, while a Merge--Split--Merge dataflow hides the resulting serial overhead. Third, a streaming vocabulary engine interleaves multiple token streams from the LM head to accommodate irregular output variations caused by selective token computation and uneven vocabulary-selection demands. Evaluated on two representative dLLMs, DynaTE achieves 2.05--2.78$\times$ speedup and 2.99--3.93$\times$ higher energy efficiency over state-of-the-art dLLM accelerators, while delivering 2.55$\times$ speedup and 6.07$\times$ higher energy efficiency over Jetson AGX Orin.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minghan Jiang, Jiayi Wang, Shuaiting Li, Haibin Shen, Kejie Huang
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
