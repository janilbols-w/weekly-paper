---
title: "Replica-Aware Split Inference for Edge IoT Systems"
description: "Split Inference (SI) addresses the hardware resource limitations of Internet of Things (IoT) devices by distributing tiny Machine Learning (TinyML) model segments across multiple IoT devices."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2611.04779) · [PDF](https://arxiv.org/pdf/2611.04779)

## 一句话摘要

Split Inference (SI) addresses the hardware resource limitations of Internet of Things (IoT) devices by distributing tiny Machine Learning (TinyML) model segments across multiple IoT devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Split Inference (SI) addresses the hardware resource limitations of Internet of Things (IoT) devices by distributing tiny Machine Learning (TinyML) model segments across multiple IoT devices. However, a device failure can interrupt the inference pipeline. This paper proposes a replica-aware recovery approach that deploys replicas of TinyML model segments originally hosted on failed devices onto surviving devices. We formulate the joint selection of replica hosts and communication protocols as a mixed-integer linear programming (MILP) problem that minimizes post-reconfiguration inference latency, accounting for computation and transmission latencies, under flash memory and runtime memory constraints. Simulations using MobileNetV2 on heterogeneous IoT networks compare the proposed approach with four baselines. We implement the model in a network of 15 IoT devices with a maximum link-rate reduction of 75%, and show that MILP approach achieves an average modeled end-to-end inference latency that is 6.8% lower than that of Computation Greedy and 18.3% lower than that of Random. Index Terms TinyML, split inference, Internet of Things, fault tolerance, replica placement.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zied Jenhani, Nasrin Razmi, Admela Jukan
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
