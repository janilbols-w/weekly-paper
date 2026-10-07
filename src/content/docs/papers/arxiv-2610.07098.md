---
title: "T-CCL: Resource Efficient and Performant Collective Communication using Tensor Memory Accelerator"
description: "Large transformer-based models increasingly depend on multi-GPU execution, which requires frequent collective communication among GPUs."
---

**评分：53/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.07098) · [PDF](https://arxiv.org/pdf/2610.07098)

## 一句话摘要

Large transformer-based models increasingly depend on multi-GPU execution, which requires frequent collective communication among GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large transformer-based models increasingly depend on multi-GPU execution, which requires frequent collective communication among GPUs. Existing communication libraries often rely on many GPU threads to achieve high bandwidth or low latency, resulting in a large streaming multiprocessor (SM)-side resource footprint. This footprint can limit the resources available to other GPU work, particularly when communication and computation execute concurrently. Thus, efficient collective communication should not only achieve high collective performance but also reduce its SM-side resource usage. This paper presents T-CCL, a resource-efficient collective communication library based on the Tensor Memory Accelerator (TMA) for intra-node communication. T-CCL offloads both data movement and reduction operations to TMA and executes each collective as a pipelined series of asynchronous TMA operations, reducing the SM resources required for collective communication while maintaining high bandwidth. Evaluated across AllReduce, AllGather, and ReduceScatter collectives, T-CCL outperforms NCCL by up to 2.4x with unrestricted communication resources and up to 3.42x under restricted resource budgets, remains competitive with NCCL's recent symmetric-memory kernels, and occupies the same or fewer SMs in profiled cases. In a GEMM-collective overlap case study, switching the communication backend from NCCL to T-CCL raises the average operator-level speedup over a sequential baseline from 1.12x to 1.25x on two GPUs and from 1.04x to 1.14x on four GPUs, as T-CCL uses fewer SMs for communication, leaving more SMs available to the overlapped GEMM. Integrated into vLLM as a communication backend, T-CCL improves end-to-end inference throughput over vLLM's automatic backend dispatch by up to 1.31x, outperforming it at every evaluated batch size on both the conversation and decode-heavy workloads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Keyvan Dadashzadeh, Yuehong Zhou, Minyu Cui, Miquel Pericas
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
