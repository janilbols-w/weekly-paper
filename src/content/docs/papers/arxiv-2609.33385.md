---
title: "OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading"
description: "Semi-autoregressive diffusion large language models (dLLMs) improve decoding parallelism through iterative block-wise denoising, but scaling them with mixture-of-experts (MoE) layers introduces a large expert parameter footprint that exceeds memory-constrained GPU capacity."
---

**评分：57/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.33385) · [PDF](https://arxiv.org/pdf/2609.33385)

## 一句话摘要

Semi-autoregressive diffusion large language models (dLLMs) improve decoding parallelism through iterative block-wise denoising, but scaling them with mixture-of-experts (MoE) layers introduces a large expert parameter footprint that exceeds memory-constrained GPU capacity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semi-autoregressive diffusion large language models (dLLMs) improve decoding parallelism through iterative block-wise denoising, but scaling them with mixture-of-experts (MoE) layers introduces a large expert parameter footprint that exceeds memory-constrained GPU capacity. Expert offloading is a natural remedy, yet existing MoE serving systems target autoregressive decoding and rely on intra-iteration layer-wise prefetching: while computing one layer, they predict and load experts for subsequent layers. Under dLLM inference, block-wise routing expands the active expert working set within each iteration, making such prefetches difficult to complete in time and costly when mispredicted. Consequently, existing prefetch-based solutions often degenerate into on-demand expert loading with high decoding latency. We propose OLED-MoE, an expert offloading system that shifts the optimization target from intra-iteration prefetching to inter-iteration expert retention. Its key insight is that adjacent denoising iterations exhibit strong expert routing overlap, and token confidence indicates which experts are likely to be reused. OLED-MoE uses confidence-guided inter-iteration prediction to retain high-value experts in GPU memory without introducing extra prefetch traffic. It further compensates unavoidable cache misses through CPU-GPU cooperative execution, jointly considering dynamic expert computation load and predicted future reuse. Across diverse dLLM workloads, OLED-MoE reduces time per output token (TPOT) by 1.23x-7.93x and improves expert cache utilization by 1.44x-4.23x over state-of-the-art offloading systems. Notably, OLED-MoE approaches full-residency performance while using only 40% of the expert GPU memory, incurring merely 23% higher TPOT despite a 60% reduction in expert memory footprint. OLED-MoE's source code is publicly available at https://github.com/flashserve/OLED-MoE.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 16 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Jingyuan Xiao (Tianjin University, Tianjin, China), Jiayue Wang (Tianjin University, Tianjin, China), Yitao Hu (Tianjin University, Tianjin, China), Xinning Wang (Tianjin University, Tianjin, China), Shi Chen (Tianjin University, Tianjin, China), Ziqi Gong (Tianjin University, Tianjin, China), Zhengchao Wang (Tianjin University, Tianjin, China), Guotao Yang (Tianjin University, Tianjin, China), Sheng Chen (Tianjin University, Tianjin, China), Keqiu Li (Tianjin University, Tianjin, China)
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/flashserve/OLED-MoE](https://github.com/flashserve/OLED-MoE)
- 阅读深度：metadata
