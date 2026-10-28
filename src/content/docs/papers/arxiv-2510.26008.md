---
title: "Seeing is believing: The case for hardware-centric inefficiency detection and remediation"
description: "Large-scale machine learning workloads on the cloud suffer from silent inefficiencies, which do not trigger failures or obvious anomalies, making them hard to detect and diagnose."
---

**评分：43/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2510.26008) · [PDF](https://arxiv.org/pdf/2510.26008)

## 一句话摘要

Large-scale machine learning workloads on the cloud suffer from silent inefficiencies, which do not trigger failures or obvious anomalies, making them hard to detect and diagnose.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large-scale machine learning workloads on the cloud suffer from silent inefficiencies, which do not trigger failures or obvious anomalies, making them hard to detect and diagnose. Existing diagnosis systems rely on guest-side instrumentation or dedicated healthy baselines. These assumptions do not hold in modern production cloud environments, where operators cannot observe inside the guest, and a healthy baseline for each setup is impractical because of system diversity. We present Unveil, a hardware-centric observability framework for detecting, identifying, and remediating silent inefficiencies using only host-visible telemetry. Unveil requires neither guest instrumentation nor application modification. It uses unsupervised learning models to detect inefficiencies and identifies known ones through a novel fingerprinting algorithm. An extensible knowledge base containing curated remediation scripts is used to correct problems without interrupting workloads when possible. We evaluate Unveil on distributed machine learning workloads, such as large language model serving, introducing less than 2% monitoring overhead. It successfully recovered from a 7% throughput loss and reduced inference latency by up to 43.48%. These results demonstrate that host-visible telemetry is sufficient for practical and continuous diagnosis of production machine learning systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziji Chen, Steven W. D. Chien, Peng Qian, Noa Zilberman
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
