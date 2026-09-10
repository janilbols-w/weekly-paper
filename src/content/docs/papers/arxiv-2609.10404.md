---
title: "HybridFLow: SDN-Orchestrated Client Partitioning for Hybrid Federated Learning"
description: "Cross-silo Federated Learning (FL) enables geographically distributed institutions to collaboratively train machine learning models without sharing raw data."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.10404) · [PDF](https://arxiv.org/pdf/2609.10404)

## 一句话摘要

Cross-silo Federated Learning (FL) enables geographically distributed institutions to collaboratively train machine learning models without sharing raw data.

## 为什么值得关注

待编辑增强。

## 摘要原文

Cross-silo Federated Learning (FL) enables geographically distributed institutions to collaboratively train machine learning models without sharing raw data. In wide-area deployments, however, communication delays often dominate round completion time and exacerbate the straggler effect. Hybrid FL addresses this challenge by combining synchronous and asynchronous client participation, but effective partitioning requires visibility into network conditions such as shared bottlenecks, link utilization, and path contention that individual clients cannot observe. We present HybridFLow, a closed-loop SDN-driven orchestration framework that integrates network-layer intelligence directly into hybrid FL. Leveraging the SDN controller's global topology view, HybridFLow generates calibrated per-client communication-time estimates before each training round and uses them to partition clients into synchronous and asynchronous groups while balancing round latency and update staleness. After each round, measured communication times are fed back to the controller to continuously refine future predictions. Experimental results across multiple network topologies show that HybridFLow reaches 80% target accuracy 33-40% faster than SmartFLow and reduces average round duration by 30-40 seconds, while FedAsync fails to reach the target accuracy under non-IID data distributions.

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

- taxonomy keywords: straggler
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Osama Abu Hamdan, Rabin Pandey, Hao Che, Engin Arslan, Md Arifuzzaman
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
