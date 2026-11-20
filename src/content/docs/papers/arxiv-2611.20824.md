---
title: "Network-Native DNN Architecture Synthesis for Distributed Inference"
description: "Distributed deep neural network (DNN) inference typically follows a model-first paradigm, in which a predefined DNN is partitioned and deployed over a physical network."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2611.20824) · [PDF](https://arxiv.org/pdf/2611.20824)

## 一句话摘要

Distributed deep neural network (DNN) inference typically follows a model-first paradigm, in which a predefined DNN is partitioned and deployed over a physical network.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed deep neural network (DNN) inference typically follows a model-first paradigm, in which a predefined DNN is partitioned and deployed over a physical network. On irregular communication-computation topologies, however, this approach can create transmission bottlenecks and leave distributed resources underutilized. This paper reverses this perspective and asks: given a physical network, what kind of DNN can it naturally support? To answer this question, we propose a network-native DNN architecture synthesis paradigm in which the physical network topology directly defines inter-node neural dependencies. Neural computation is allocated across nodes under communication, computation, storage, synchronization, and latency constraints. We establish structural properties of the synthesis problem and develop linear programming (LP)-based Architecture Synthesis (LPAS), an efficient topology-guided algorithm that produces a feasible architecture with a computable bound on suboptimality. Experiments on physical networks of different sizes show that LPAS achieves relative gaps below 0.6% to the LP-derived upper bound, with substantially lower runtime than direct mixed-integer LP optimization on larger networks. Under matched network deadlines, the network-native architectures activate more compute nodes and utilize a larger proportion of available model-storage capacity than the model-first baseline. After training, the network-native models achieve higher classification accuracy across all evaluated dataset-precision settings, with the average gain of up to 10.69%. This network-native design paradigm thus turns the physical network from a deployment constraint into an architecture design primitive.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fan Yang, Xiaolong Wu, Qi Cao, Fen Hou, Yulin Shao
- 发布：2026-11-16；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
