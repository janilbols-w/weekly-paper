---
title: "OrderMoE: An expert similarity driven distributed edge MoE inference"
description: "Although mixture-of-experts, MoE, models have been increasingly adopted to scale large language models with moderate computation cost, it remains challenging to deploy MoE inference over resource-constrained and bandwidth-limited edge infrastructures."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2607.17154) · [PDF](https://arxiv.org/pdf/2607.17154)

## 一句话摘要

Although mixture-of-experts, MoE, models have been increasingly adopted to scale large language models with moderate computation cost, it remains challenging to deploy MoE inference over resource-constrained and bandwidth-limited edge infrastructures.

## 为什么值得关注

待编辑增强。

## 摘要原文

Although mixture-of-experts, MoE, models have been increasingly adopted to scale large language models with moderate computation cost, it remains challenging to deploy MoE inference over resource-constrained and bandwidth-limited edge infrastructures. Existing distributed MoE serving methods mainly rely on exact expert placement, caching, replication, or communication scheduling, while overlooking the functional similarity among experts, which provides an opportunity to reduce cross-server token transmission. Therefore, this paper introduces a similarity-aware expert allocation and distributed deployment framework, dubbed OrderMoE, which aims to accelerate edge MoE inference while balancing inference latency, communication overhead, server workload, and inference quality. OrderMoE first constructs an expert similarity model based on router-induced logits representations and partitions experts in each MoE layer into multiple similarity groups. Then, it develops a similarity-aware expert grouping and deployment strategy to improve local similarity coverage across edge servers. Since reducing remote expert invocation and preserving exact inference quality are conflicting objectives, OrderMoE further designs a quality-aware and trajectory-aware runtime server-expert selection algorithm to decide whether a token should invoke its remote target expert or use a feasible local substitute expert. Experimental results on a real distributed edge testbed show that OrderMoE significantly reduces average latency, tail latency, cross-server traffic, and remote expert invocation ratio, while introducing only small and controllable inference quality degradation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: moe inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xin Yuan, Ning Li, Quan Chen, Wenchao Xu, Song Guo
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
