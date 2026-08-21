---
title: "Collective Communication for Distributed LLM Systems: Planning, Runtime Adaptation, and Computation Coordination"
description: "Distributed large language model (LLM) systems increasingly rely on collective communication primitives such as AllReduce (AR), ReduceScatter (RS), AllGather (AG), and AlltoAll (A2A)."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2608.15118) · [PDF](https://arxiv.org/pdf/2608.15118)

## 一句话摘要

Distributed large language model (LLM) systems increasingly rely on collective communication primitives such as AllReduce (AR), ReduceScatter (RS), AllGather (AG), and AlltoAll (A2A).

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed large language model (LLM) systems increasingly rely on collective communication primitives such as AllReduce (AR), ReduceScatter (RS), AllGather (AG), and AlltoAll (A2A). In modern LLM training and serving clusters, heterogeneous GPU interconnects, multi-NIC networking, mixed parallelism strategies, low-latency inference requests, and high-throughput training pipelines have motivated increasingly diverse ways to plan, execute, and overlap collective communication. This paper presents a tutorial-style, collective-centric taxonomy for collective communication. We organize recent advances into three layers: communication planning, which generates topology-aware collective schedules; communication execution and adaptation, which maps these schedules onto GPU runtimes and hardware in real clusters; and computation-communication coordination, which turns collective optimization into end-to-end training and inference benefits. We further discuss open challenges and future opportunities for collective communication in distributed LLM systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: collective communication
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuebin Song, Menghao Zhang, Yuezheng Liu, Jinyi Xia, Shucan Yang, Xiaohe Hu, Chunming Hu, Mingwei Xu
- 发布：2026-08-15；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
