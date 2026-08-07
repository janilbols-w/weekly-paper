---
title: "NIXT: A NCCL Inspector Exporter Tool for Observability of Collective Communication in Large Model Training"
description: "As machine learning workloads scale, it is increasingly important to gain more observability into the performance of collective communication to easily identify performance vari- ations and accelerate root cause identification."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.01449) · [PDF](https://arxiv.org/pdf/2608.01449)

## 一句话摘要

As machine learning workloads scale, it is increasingly important to gain more observability into the performance of collective communication to easily identify performance vari- ations and accelerate root cause identification.

## 为什么值得关注

待编辑增强。

## 摘要原文

As machine learning workloads scale, it is increasingly important to gain more observability into the performance of collective communication to easily identify performance vari- ations and accelerate root cause identification. Towards this goal, the Nvidia Collective Communication Library (NCCL) introduced NCCL Inspector, a profiler plugin that provides lightweight and continuous reporting of NCCL communication performance statistics. However, the large volume of data collected by NCCL Inspector can be difficult to assess and to extract actionable insights from. This paper presents NIXT, a NCCL Inspector Exporter Tool that improves the observability of collective communication by providing readily accessible analysis and actionable insights from NCCL Inspector profiling. To highlight the benefits of our Exporter Tool, we present a case study of Nemotron-4 LLM pretraining on an Nvidia H100 GPU cluster with up to 2,048 GPUs, demonstrate observability into how communication phases change with ML parallelism and GPU scale, and perform attribution of performance variation and root cause analysis of stragglers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: large model training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ziyang Jia, Sirshak Das, Jason Sewall, Laxmi Bhuyan, Pasha Shamis, Daniel Wong
- 发布：2026-08-02；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
