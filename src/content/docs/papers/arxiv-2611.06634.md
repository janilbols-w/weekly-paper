---
title: "flash-comm: Self-Synchronizing Collective Communication for LLM Decoding"
description: "We present flash-comm, a communication library that achieves efficient transport for LLM decoding by fusing readiness synchronization with data movement."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2611.06634) · [PDF](https://arxiv.org/pdf/2611.06634)

## 一句话摘要

We present flash-comm, a communication library that achieves efficient transport for LLM decoding by fusing readiness synchronization with data movement.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present flash-comm, a communication library that achieves efficient transport for LLM decoding by fusing readiness synchronization with data movement. flash-comm introduces self-synchronizing transfers in which each data block carries evidence of its readiness, allowing receivers to directly validate the blocks they need without separate inter-GPU barriers. Based on this principle, a cost-guided protocol selector adapts the readiness encoding to message size and the number of participating GPUs, balancing synchronization overhead against additional data-transfer cost. flash-comm further decouples transport order from reduction order to preserve result consistency across GPUs under asynchronous data arrivals. On a server with eight NVIDIA B300 GPUs, flash-comm reduces all-reduce latency by a median of 28.8% and up to 43.7% compared with custom AR v2 (the state-of-the-art all-reduce implementation). In end-to-end decoding, flash-comm reduces time per output token (TPOT) by 1.7-6.8%. Note that all-reduce accounts for 11.4% of the baseline decoding time, which bounds the latency reduction possible from optimizing this operation alone. The same mechanism also supports standalone all-gather, reducing latency by a median of 23.8% and up to 58.9% across eight B300 GPUs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Carrie Wang, Jack Li, Jason Zhao
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
