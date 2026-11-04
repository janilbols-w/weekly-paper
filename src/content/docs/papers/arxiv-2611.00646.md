---
title: "When Shards Fly: Cross-Tensor In-Flight Conversion for Low-Latency, Low-Memory Weight Updates in Disaggregated RL"
description: "Disaggregated LLM reinforcement learning (RL) repeatedly synchronizes policy weights between training and rollout GPU pools."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.00646) · [PDF](https://arxiv.org/pdf/2611.00646)

## 一句话摘要

Disaggregated LLM reinforcement learning (RL) repeatedly synchronizes policy weights between training and rollout GPU pools.

## 为什么值得关注

待编辑增强。

## 摘要原文

Disaggregated LLM reinforcement learning (RL) repeatedly synchronizes policy weights between training and rollout GPU pools. Existing systems reduce communication through shard delivery and replica forwarding, yet separate conversion passes and staging buffers still add latency and GPU-memory overheads to synchronous updates. We present ShardFly, which coordinates reusable transfer planning with streaming GPU execution for synchronous, in-place weight updates. ShardFly introduces two components. The Planner compiles native shard mappings, quantization dependencies, and replica routes into cross-tensor schedules, reserving payload buffers only for scheduled transfers. The Executor runs each rank's schedule in one persistent transfer kernel, fusing memory-layout conversion, quantization, GPU-initiated communication, and destination writes while forwarding transformed bytes across replicas. Plans and communication state are reused under stable configurations and replaced between updates for coordinated rollout scaling. On up to 32 H20 GPUs, ShardFly achieves complete BF16 weight-update speedups of 1.26--27.92$\times$ across five models and four baselines: veRL NCCL, Awex, veRL NIXL, and WeightBridge. In end-to-end Qwen3-30B-A3B GRPO across four rollout configurations, ShardFly improves response-token throughput by 5.49--6.71\% over veRL NCCL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiayu Xiao, Ye Wang, Zhi Zhang, Jiarui Guo, Kan Liu, Tao Lan, Minchen Yu
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
