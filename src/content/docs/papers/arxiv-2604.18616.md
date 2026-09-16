---
title: "Ave: Guiding Agentic GPU Optimization Using Data-Flow Invariants"
description: "LLM coding agents can generate correct GPU kernels, but their performance still trails expert libraries."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Kernel 与算子融合

[论文原文](https://arxiv.org/abs/2604.18616) · [PDF](https://arxiv.org/pdf/2604.18616)

## 一句话摘要

LLM coding agents can generate correct GPU kernels, but their performance still trails expert libraries.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM coding agents can generate correct GPU kernels, but their performance still trails expert libraries. Reaching peak throughput requires coordinating low-level optimizations such as shared-memory staging, software pipelining, and instruction scheduling. Yet unit tests and profiles provide only sparse end-to-end feedback, making it difficult for agents to identify which global constraints an optimization violates. We present Ave, an agentic framework that uses data-flow invariants as compile-time guardrails for GPU kernel optimization. Ave provides a tile-based Pythonic DSL that exposes hardware instructions and compiler policies while abstracting complex memory layouts. Tag functions assign symbolic labels to data, the compiler propagates them through data and control flow, and tag assertions enforce required relationships at use sites. A flow-sensitive, path-insensitive analysis with an SMT solver checks these assertions and returns concrete counterexamples for violations, with no runtime overhead. An in-context reinforcement learning planner proposes optimizations from a curated knowledge base, while a lowering agent implements them and instantiates the required invariants. We evaluate Ave on AMD MI300X across GEMM, flash attention, and MoE, which together account for up to 90% of GPU time in LLM inference. With GPT-5.6 Sol, Ave achieves 89-99% of the effective throughput of state-of-the-art hand-optimized libraries and improves geometric-mean throughput by 1.62-1176x over uncontaminated agentic baselines. On 200 KernelBench tasks, Ave produces valid kernels within three attempts for 100% of Level 1 and 88% of Level 2 problems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu kernel, kernel optimization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haohui Mai, Xiaoyan Guo, Xiangyun Ding, Daifeng Li, Qiuchu Yu, Chenzhun Guo, Cong Wang, Jiacheng Zhao, Christos Kozyrakis, Binhang Yuan
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
