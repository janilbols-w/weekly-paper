---
title: "Fault Tolerance for Stream Processing Engines"
description: "Distributed Stream Processing Engines (DSPEs) target applications related to continuous computation, online machine learning and real-time query processing."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/1605.00928) · [PDF](https://arxiv.org/pdf/1605.00928)

## 一句话摘要

Distributed Stream Processing Engines (DSPEs) target applications related to continuous computation, online machine learning and real-time query processing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Distributed Stream Processing Engines (DSPEs) target applications related to continuous computation, online machine learning and real-time query processing. DSPEs operate on high volume of data by applying lightweight operations on real-time and continuous streams. Such systems require clusters of hundreds of machines for their deployment. Streaming applications come with various requirements, i.e., low-latency, high throughput, scalability and high availability. In this survey, we study the fault tolerance problem for DSPEs. We discuss fault tolerance techniques that are used in stream processing engines that were state of the art at the time of writing (2016), namely S4, Storm, Flink, Spark Streaming, Samza and MillWheel. Further, we give insight on fault tolerance approaches that we categorize as active replication, passive replication and upstream backup. Finally, we discuss implications of the fault tolerance techniques for different streaming application requirements. This revised version corrects errors in the original 2016 manuscript, summarizes later developments in Flink and Spark, discusses durable logs and archival storage for replay, and points to more recent surveys.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Anis Uddin Nasir
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
