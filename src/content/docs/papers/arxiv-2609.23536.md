---
title: "Explicit State and Resource Contracts for Low-Precision Pipeline Parallel Training under Captured Graphs"
description: "CUDA Graphs eliminate launch overheads by replaying tensor operations over static virtual addresses."
---

**评分：45/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2609.23536) · [PDF](https://arxiv.org/pdf/2609.23536)

## 一句话摘要

CUDA Graphs eliminate launch overheads by replaying tensor operations over static virtual addresses.

## 为什么值得关注

待编辑增强。

## 摘要原文

CUDA Graphs eliminate launch overheads by replaying tensor operations over static virtual addresses. However, FP8 pipeline training continuously alters the scaling states, microbatches, and deferred backward tasks that those fixed addresses represent. Split-backward schedules (e.g., 1F1B, Zero-Bubble) decouple input-gradient ($dI$) and weight-gradient ($dW$) computations to minimize bubbles, breaking traditional LIFO lifecycles. Standard dataflow graphs cannot inform the runtime of hidden numerical updates, non-LIFO work ownership, or cache validity, leading to silent cross-stream data corruption. We present QEffect, an explicit state and resource contract runtime for low-precision pipeline training. QEffect formalizes four foundational invariants: (1) temporal serialization of hidden scaling updates, (2) generational ownership of retained backward resources, (3) validity versioning for cached weights across optimizer boundaries, and (4) bidirectional caller-graph stream completion synchronization. These invariants uniformly govern eager and captured execution, allowing ephemeral graph resources to be cleanly rebuilt across process restarts. Leveraging work-ownership semantics, we also introduce an affine direct-gradient placement mechanism that eliminates redundant memory copies. Integrated with TorchTitan and NVIDIA Transformer Engine, QEffect maintains strict bitwise parity with native baselines across delayed-scaling rollovers, deterministically traps cross-stream ordering violations, and enables flawless cold-start resumption. On NVIDIA H800 GPUs, captured Transformer layers achieve 1.82--2.79x speedup over eager execution, while direct gradient placement delivers an additional 1.132x gain by eliminating 96 matrix copies per rank-step.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pipeline parallel
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Genlang Chen, Junyi Zhu
- 发布：2026-09-20；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
