---
title: "Load Balancing with Evolving Workloads in Large-Scale Language Model Serving"
description: "Serving large language models requires assigning requests whose workloads grow during processing and whose completion times are unknown."
---

**评分：47/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2601.17855) · [PDF](https://arxiv.org/pdf/2601.17855)

## 一句话摘要

Serving large language models requires assigning requests whose workloads grow during processing and whose completion times are unknown.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving large language models requires assigning requests whose workloads grow during processing and whose completion times are unknown. With a synchronization barrier, lightly loaded workers wait for the slowest worker at every decode iteration. We model this loss through aggregate workload imbalance and formulate a joint admission and assignment problem with sticky requests and capacity limits. Short lookahead incorporates predicted completions of ongoing requests. For exact optimization without lookahead, we prove a comparison under independent geometric decode lengths, bounded independent nondegenerate prompt sizes, and batched releases satisfying a cumulative supply condition. The long-run expected imbalance improvement over first come, first served admission with request-count join-shortest-queue grows at least as the square root of the product of worker capacity and the logarithm of worker count, in the stated scaling regime. The comparison extends to capacity-aware round robin, random routing, and power of two choices. BalanceRoute approximations connect the formulation to practical routing. Experiments using up to 144 NPUs with proprietary and public traces show lower workload spread and higher throughput than the evaluated baselines. These empirical results complement the guarantee for exact optimization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zixi Chen, Tianci Bu, Chendong Song, Xin Lu, Yinyu Ye, Zijie Zhou
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
