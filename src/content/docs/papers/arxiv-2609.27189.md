---
title: "ZOCheck: CPU-Shadow Checkpointing for Zeroth-Order LLM Fine-Tuning"
description: "Zeroth-order (ZO) optimization is an attractive option for memory-efficient LLM fine-tuning, but its fault tolerance remains underexplored."
---

**评分：52/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.27189) · [PDF](https://arxiv.org/pdf/2609.27189)

## 一句话摘要

Zeroth-order (ZO) optimization is an attractive option for memory-efficient LLM fine-tuning, but its fault tolerance remains underexplored.

## 为什么值得关注

待编辑增强。

## 摘要原文

Zeroth-order (ZO) optimization is an attractive option for memory-efficient LLM fine-tuning, but its fault tolerance remains underexplored. Unlike first-order training, ZO progress can be represented by lightweight seed-and-scalar step logs, yet naive log-only recovery still incurs replay cost that grows with training progress, and shortcut replay does not preserve the executed floating-point trajectory. We present ZOCheck, a fault-tolerant ZO training system that exploits this replayable structure through a CPU shadow process that continuously replays logged updates, materializes consistent recovery images off the GPU critical path, and persists them asynchronously. ZOCheck therefore combines non-blocking checkpointing during training with fast recovery from a near-current state. We also develop a cost model for choosing the snapshot policy under realistic failure rates. Experiments show that ZOCheck reduces checkpoint overhead by up to 219.7x and recovery latency by 1.55x on average compared with asynchronous full-state checkpointing, translating into up to 21.3x lower end-to-end wasted time across the evaluated failure rates, while preserving exact recovery behavior.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Minqiu Sun, Xin Huang, Luanzheng Guo, Nathan R. Tallent, Kento Sato, Dong Dai
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
