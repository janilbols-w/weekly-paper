---
title: "LayerCheck: Adaptive Layer-wise Checkpointing for Large Language Model Post-training"
description: "With the rising computational and monetary costs of training large language models (LLMs), checkpointing---periodically storing model states for recovery---becomes essential for fault tolerance."
---

**评分：47/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.27193) · [PDF](https://arxiv.org/pdf/2609.27193)

## 一句话摘要

With the rising computational and monetary costs of training large language models (LLMs), checkpointing---periodically storing model states for recovery---becomes essential for fault tolerance.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the rising computational and monetary costs of training large language models (LLMs), checkpointing---periodically storing model states for recovery---becomes essential for fault tolerance. Conventional checkpointing entails a severe trade-off between checkpoint frequency (I/O overhead) and computational recovery (recovery time). State-of-the-art approaches mitigate this cost through pipelining checkpoint I/Os, differential checkpointing, or in-memory persistence, yet none leverage the distinct characteristics of LLM training dynamics, where model weight updates are non-uniformly distributed across transformer layers. This observation implies that saving all weights each time might not be efficient. Inspired by this observation, we present LayerCheck, a layer-wise adaptive checkpointing framework that selectively persists layers whose updates exceed a threshold. This design avoids periodic I/O bursts by distributing layer-wise checkpoint writes over time, resulting in smoother and more balanced I/O profiles. Upon recovery, LayerCheck reconstructs a mixed-timestamp composite model state by aggregating the most recently persisted versions of each layer together with their matching optimizer states. Under a bounded per-layer staleness guard, this introduces a controlled perturbation: under standard Adam assumptions it adds a bounded staleness term, and empirically the post-restart loss deviates from the failure-free trajectory by at most 0.54%. Empirical results on multiple open-source LLMs with different datasets further demonstrate that recovered models preserve the original convergence behavior and accuracy while substantially reducing checkpoint overheads. Specifically, LayerCheck achieves up to 22.6x reduction in total checkpoint size and 1.31x reduction in end-to-end training time compared to state-of-the-art systems, significantly lowering the cost of checkpointing.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint, checkpointing
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Minqiu Sun, Xin Huang, Luanzheng Guo, Nathan R. Tallent, Kento Sato, Dong Dai
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
