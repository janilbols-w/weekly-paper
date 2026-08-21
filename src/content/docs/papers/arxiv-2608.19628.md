---
title: "A Thread-Register Decoupled GPU Execution Model for Efficient Tensor Computation"
description: "Modern GPUs increasingly integrate Tensor Cores into the execution pipeline."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.19628) · [PDF](https://arxiv.org/pdf/2608.19628)

## 一句话摘要

Modern GPUs increasingly integrate Tensor Cores into the execution pipeline.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern GPUs increasingly integrate Tensor Cores into the execution pipeline. Although aggregate tensor throughput continues to grow, aided by an operand supply that has evolved from register-based in Ampere to redundancy-free, memory-based in Hopper and Blackwell, efficiently orchestrating the complete tensor compute pipeline for the modern AI workloads remains challenging. We identify the fundamental bottlenecks as fixed parallelism and coarse-grained scheduling, both of which are exposed by modern AI workloads that interleave diverse non-GEMM operations with GEMM. To orchestrate tensor computation efficiently, we propose FIBER, a new architecture that extends the GPU SIMT (single instruction, multiple thread) model. Its basic execution instance, the \emph{fiber}, is decoupled from private register ownership, carrying only minimal control state while accessing an SM's registers through a shared view. This enables dynamic parallelism scaling, fine-grained register-level dataflow scheduling, and offers a redundancy-free alternative for matrix operand supply. We extend the ISA, microarchitecture, and compiler to realize shared-register addressing, conflict-free operand delivery, and fiber-based program mapping. Under a typical mixed-precision LLM serving scenario, FIBER achieves a 2.25x end-to-end speedup on Ampere (1.15x for the original FP16 computation), with 1.8x and 2.09x on Hopper and Blackwell respectively, and kernel-level gains up to 2.49x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zihan Liu, Jingwen Leng, Yangjie Zhou, Yitong Ding, Guanlin Zhu, Yilu Huang, Chiheng Jin, Chen Zhang, Shixuan Sun, Yu Feng, Anbang Wu, Minyi Guo, Jian Weng, Jiajin Tu, Junsong Wang
- 发布：2026-08-21；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
