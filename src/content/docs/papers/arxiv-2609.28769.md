---
title: "Xtrace: High-Fidelity GPU Intra-Kernel Tracing via Binary-Level Instruction Splicing"
description: "Modern GPU kernels fuse increasingly more work into a single kernel, and intra-kernel tracing has become the mainstream method to profile them."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2609.28769) · [PDF](https://arxiv.org/pdf/2609.28769)

## 一句话摘要

Modern GPU kernels fuse increasingly more work into a single kernel, and intra-kernel tracing has become the mainstream method to profile them.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern GPU kernels fuse increasingly more work into a single kernel, and intra-kernel tracing has become the mainstream method to profile them. Tracing inserts probes into the kernel to record its runtime states, and the fidelity of the trace determines the efficiency of performance optimization. Unfortunately, existing tools insert probes before compilation. These tools interfere with the compiler's optimizations, so they trace a different binary from the one the GPU executes. They also add significant runtime overhead. Xtrace is the first GPU kernel tracing system with near-zero compile-time interference and minimized runtime overhead. Xtrace inserts probes directly into the compiled kernel binary. It reuses only the registers that hold dead values at the insertion address and resolves all hazards with the compiler's hazard tables. It further schedules the instruction order, register allocation, and control bits to minimize the runtime overhead the probe introduces. Xtrace supports 19 NVIDIA and AMD GPU architectures, and is publicly available for use at https://g-watch.github.io. We evaluate Xtrace on major production large language model (LLM) kernels against the state-of-the-art tracers Neutrino and IKET from NVIDIA. On H100, B300, and MI300X GPUs, Xtrace preserves 94-98% of the instructions of the kernel, while existing tools preserve only 8-48%. Xtrace adds only 0.9-2.8% overhead, while existing tools add 3.8-75.6%. Xtrace guides a coding agent to reach the same FlashAttention-3 performance with 3.9x fewer iterations than existing traces do. Thanks to our binary-level instrumentation, Xtrace also traces the faster closed-source cuDNN kernel, which guides the agent to lift the open-source FlashAttention-4 by 5.2-13.3% in throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhuobin Huang, Kai Zhang, Weihao Cui, Hongshi Tan, Liang Luo, Christopher Dewan, Shen Li, Bingsheng He
- 发布：2026-09-23；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
