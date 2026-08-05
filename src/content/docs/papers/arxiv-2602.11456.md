---
title: "AuroraRL: Fast, Fault-Tolerant, and Cost-Efficient Reinforcement Learning over Decentralized Network"
description: "LLM reinforcement learning (RL) requires frequent synchronization of large model parameters between the trainer and distributed rollout actors."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2602.11456) · [PDF](https://arxiv.org/pdf/2602.11456)

## 一句话摘要

LLM reinforcement learning (RL) requires frequent synchronization of large model parameters between the trainer and distributed rollout actors.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM reinforcement learning (RL) requires frequent synchronization of large model parameters between the trainer and distributed rollout actors. High-throughput RL post-training therefore relies on dedicated RDMA HPC/cloud clusters, an infrastructure cost most organizations cannot absorb. A natural alternative is to aggregate loosely-coupled GPUs over standard Ethernet and WAN links, but this commodity connectivity cannot sustain full-weight broadcasts: synchronizing an 8B model can take over 100~seconds on bandwidth-limited links, while rollout generation typically takes tens of seconds. Toward making RL practical in this regime, we observe that RL fine-tuning yields highly sparse per-step updates, with only around 1\% of parameter elements changing. On top of this insight, we present AuroraRL, a novel high-performance RL training system that preserves bit-exact updates without dropping or quantizing information, designed for commodity-networked, loosely-coupled GPU resources. AuroraRL represents each step as a sparse delta checkpoint, pipelines delta extraction with multi-stream transmission, overlaps transfer with rollout generation, and coordinates heterogeneous workers with throughput- and bandwidth-aware scheduling plus lease-based fault tolerance. Across Qwen3 4B--14B models deployed in up to four geographic regions, AuroraRL shrinks per-step weight transfer by 79$\times$ on Qwen3-8B, delivers 1.3--9.5$\times$ higher throughput than dense-broadcast baselines (PrimeRL-Full, async-tolerant, multi-stream variants), and brings end-to-end training within 8.91\% of an ideal RDMA single-datacenter baseline, while transparently tolerating common failures and preserving training accuracy. By leveraging on-demand, cross-cloud GPUs over commodity links, AuroraRL delivers 1.21--1.59$\times$ higher tokens per dollar than reserved RDMA clusters at comparable throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chaoyi Ruan, Geng Luo, Xinyi Wan, Long Zhao, Qinghe Wang, Jiaan Zhu, Duling Xu, Guanbin Xu, Dehui Wei, Xiang Liu, Cheng Li, Haifeng Sun, Liang Luo, Congcong Miao, Jialin Li
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
