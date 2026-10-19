---
title: "Accelerated Dataflow: scaling inference in streaming data analytics with efficiency"
description: "Streaming data analytics helps businesses identify opportunities and spot risks in a timely fashion."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2610.22731) · [PDF](https://arxiv.org/pdf/2610.22731)

## 一句话摘要

Streaming data analytics helps businesses identify opportunities and spot risks in a timely fashion.

## 为什么值得关注

待编辑增强。

## 摘要原文

Streaming data analytics helps businesses identify opportunities and spot risks in a timely fashion. As large language model (LLM) usage grows, people are exploring incorporating agents or LLMs in streaming data pipelines to help find patterns in datasets without supervision or interpret natural languages for content moderation. However, most streaming systems are currently optimized for data movement and perform poorly on GPU intensive workloads such as performing inference with LLMs. We introduce a system on Google Cloud Dataflow designed to tackle hybrid streaming machine learning workloads with co-designed autoscaling on heterogeneous worker pools and prefix-aware batching. This increases throughput 1.5x to 2x for streaming pipelines using LLMs while maintaining similar latency with up to 75% peak resource savings and 84% lower peak tail latency compared with existing streaming data processing systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：RuiLong Jiang, Dustin Rhodes, Danny McCormick, Yuta Labur, Reza Rokni
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
