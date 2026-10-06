---
title: "MOLT: A Fine-Grained GPU Memory Sharing System for LLM Serving with Opportunistic Fine-Tuning"
description: "Large language model (LLM) serving scales its replica count with the request load, yet GPU memory still stands idle inside the replicas."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.05748) · [PDF](https://arxiv.org/pdf/2610.05748)

## 一句话摘要

Large language model (LLM) serving scales its replica count with the request load, yet GPU memory still stands idle inside the replicas.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving scales its replica count with the request load, yet GPU memory still stands idle inside the replicas. Adding a replica takes minutes, while the memory that a replica needs changes within seconds. Even instant autoscaling could not return this idle memory, because the smallest unit that it can remove is a whole replica. Colocating parameter-efficient fine-tuning (PEFT) with inference can use this memory, but inference must be able to reclaim it within seconds, before requests that wait for memory exceed their latency service-level objective (SLO). Existing colocation systems either keep the tuning memory resident or let inference reclaim it at the coarse granularity of a whole training sample. Each such reclamation also discards the running tuning step. To address these limitations, we present MOLT, a fine-grained memory sharing system that lets inference reclaim the memory of individual activations that a running tuning step has saved for its backward pass. The step continues, and its backward pass recomputes those activations. Inference reclaims only memory that no in-flight GPU work can still access, even under CPU--GPU asynchrony and tensor parallelism. On four model deployments (24B--70B) across H100 SXM and B200 GPUs under trace-driven workloads, MOLT keeps inference SLO attainment at or above 99.7% and completes 1.9--3.3x the tuning work of discard-based memory sharing.

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

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jaehoon Yang, Yongbeom Kim, Hojoon Kim, Seung Yul Lee, Jae W. Lee
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
