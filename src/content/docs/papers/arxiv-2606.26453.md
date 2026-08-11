---
title: "Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization"
description: "We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools."
---

**评分：56/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2606.26453) · [PDF](https://arxiv.org/pdf/2606.26453)

## 一句话摘要

We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools. KernelPro introduces four contributions: (1) a semantic feedback operator that encodes expert heuristics as pluggable micro-profiling tools, transforming raw hardware metrics into actionable natural language guidance; (2) a two-stage tool invocation architecture where roofline-based bottleneck classification filters which specialized analysis tools execute, combining kernel-level (ncu), instruction-level (SASS), and system-level (nsys) profiling; (3) a domain-adapted MCTS with progressive widening, asymmetric branching, log-reward calibration, dead-end pruning, and search memory for cross-iteration learning; and (4) direct CuTe source-level code generation via autonomous code search over the CUTLASS/CuTe codebase. On KernelBench, KernelPro achieves geometric mean speedups of 2.42x/4.69x/5.30x on Levels 1/2/3, establishing state-of-the-art performance across all difficulty levels. On VeOmni's expert-optimized MoE training kernels, KernelPro achieves 1.23x over hand-tuned Triton by generating a from-scratch raw-CUDA+CuTe Hopper WGMMA kernel. Ablation studies demonstrate that each design component independently and significantly improves optimization quality: micro-profiling tools (p < 0.0001 vs raw metrics), MCTS search (26% higher geometric mean vs greedy, p = 0.004), and proactive tool orchestration (23% improvement, p = 0.035). Finally, KernelPro is the first CUDA kernel coding agent to optimize energy efficiency beyond the speed-only focus of prior systems, demonstrating an 11.6% measured energy reduction at matched speed.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 24 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cuda kernel, gpu kernel, kernel optimization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiading Gai, Shuai Zhang, Kaj Bostrom, Jin Huang, Vihang Patil, Haoyang Fang, Bernie Wang, Huzefa Rangwala, George Karypis
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
