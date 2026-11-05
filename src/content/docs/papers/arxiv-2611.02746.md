---
title: "Replay for LLM Continual Learning with Multi-Teacher On-Policy Distillation"
description: "Multi-teacher on-policy distillation (MOPD) distills several domain experts into one student and is used in the post-training of recent large language models."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.02746) · [PDF](https://arxiv.org/pdf/2611.02746)

## 一句话摘要

Multi-teacher on-policy distillation (MOPD) distills several domain experts into one student and is used in the post-training of recent large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-teacher on-policy distillation (MOPD) distills several domain experts into one student and is used in the post-training of recent large language models. It trains on all domains at once, so every expert must be available at the same time. In practice, capabilities often arrive one after another, and the experts of earlier domains may be gone when a new domain is learned. Distilling the experts in sequence then suffers from catastrophic forgetting of the earlier domains. Some recent pipelines store a snapshot after every stage and end with a multi-teacher recovery stage taught by all snapshots. The number of stored models then grows with the number of stages. Different from these pipelines, this paper formulates continual MOPD by what is kept from earlier stages and studies replay toward the previous student. Inside every stage, prompts of earlier domains are replayed with the student of the previous stage as their teacher, so neither earlier experts nor stage snapshots are kept. Two design choices of replay are explored. The replay budget of a stage is either shared among the earlier domains or fixed per earlier domain. Replay steps either distill the token distribution alone or add alignment of hidden states, region-pooled self-attention scores and value relations. A five-domain benchmark of logic, math, code, safety and instruction following is built from public experts of one 1.5B student. Experiments on its 14 benchmarks show that, without storing any snapshot, replay toward the previous student closes most of the gap between sequential distillation and joint MOPD. With a fixed replay share per earlier domain, it performs on par with recovery from all stored snapshots.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiqiao Qiu
- 发布：2026-11-03；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
