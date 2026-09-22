---
title: "Sharing a Fabric with Collective Communication: Two Storage Penalties in Deep Learning Training"
description: "Distributed DL training on HPC systems often shares one network fabric between NCCL/RCCL collective communication and parallel-filesystem I/O."
---

**评分：50/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2609.06506) · [PDF](https://arxiv.org/pdf/2609.06506)

## 一句话摘要

Distributed DL training on HPC systems often shares one network fabric between NCCL/RCCL collective communication and parallel-filesystem I/O.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed DL training on HPC systems often shares one network fabric between NCCL/RCCL collective communication and parallel-filesystem I/O. Using a real GNN training workload on a Slingshot-11 system, we show that this sharing imposes two distinct costs. The primary cost is heavy-tailed DataLoader stalls: the typical DataLoader wait is just 15 ms at steady state, yet spikes to multiple seconds in 28% of Lustre iterations and 12% of VAST iterations. The secondary cost is traffic-class contention on collective communication: Lustre I/O stalls the all-reduce by up to 145$\times$ in an isolated benchmark. The two costs arise from different mechanisms. I/O stall latency affects any storage path that traverses the shared fabric, whereas all-reduce network contention occurs only when storage and collective communication share the same traffic class. Their common root cause is that storage I/O traverses the shared fabric. This work shows that node-local NVMe staging via DYAD (Our code is publicly available at https://github.com/flux-framework/dyad) eliminates both effects by keeping storage I/O off that path. Across a full training epoch, DYAD achieves a 7.4 times speedup over direct Lustre reads and a 1.06 times speedup over VAST. By the second epoch, once the local cache is fully warmed, DataLoader stalls are eliminated entirely, allowing DYAD to reach a 1.31 times speedup over VAST.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: network fabric
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Chen Wang, Wenzhao Wu, Hyojin Kim, Jae-Sung Yeom
- 发布：2026-09-09；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/flux-framework/dyad](https://github.com/flux-framework/dyad)
- 阅读深度：metadata
