---
title: "Benchmarking LLM Inference on Desktop-Scale NVIDIA Grace Blackwell Clusters"
description: "Two NVIDIA DGX Spark GB10 systems connect directly over 200 GbE to serve larger language models and increase inference capacity, but the benefits depend on how they are deployed."
---

**评分：50/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2611.20289) · [PDF](https://arxiv.org/pdf/2611.20289)

## 一句话摘要

Two NVIDIA DGX Spark GB10 systems connect directly over 200 GbE to serve larger language models and increase inference capacity, but the benefits depend on how they are deployed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Two NVIDIA DGX Spark GB10 systems connect directly over 200 GbE to serve larger language models and increase inference capacity, but the benefits depend on how they are deployed. We benchmark 17 open-weight checkpoints spanning dense and mixture-of-experts architectures, 8B to 235B parameters and four weight precisions on one and two RDMA-connected systems. Using vLLM, we compare tensor parallelism (TP=2), pipeline parallelism (PP=2) and a two-replica baseline at concurrency 1 to 64, with three independent launches per configuration. TP=2 delivers a median 1.59x peak-throughput gain over one Spark, versus 1.39x for PP=2 and has higher throughput in 93 of 96 matched comparisons with separated 95% Welch intervals. It reduces unloaded inter-token latency to 0.52x to 0.73x of one Spark, whereas PP=2 provides little reduction. TP=2 also achieves the highest goodput under a strict 100 ms inter-token latency objective wherever both strategies are supported and the objective is met. For models fitting on one Spark, TP=2 generally favors low-concurrency serving, while replication offers higher throughput at high concurrency. One Spark uses less GPU energy per output token at matched concurrency. Across three precision ladders, NVFP4 reduces unloaded latency more than adding a second Spark at BF16. NCCL microbenchmarks and comparisons with an earlier TCP campaign suggest that collective communication overhead contributes to the advantage of TP=2. These results provide deployment guidance for desktop-scale inference.

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

- taxonomy keywords: rdma
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Kevin Bhimani, Christian Escobar, Daniel Mihovch, Rudolf Eigenmann, Sunita Chandrasekaran
- 发布：2026-11-15；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/kevinhbhimani/dgx-spark-llm-serving-benchmark](https://github.com/kevinhbhimani/dgx-spark-llm-serving-benchmark)
- 阅读深度：metadata
