---
title: "Multi-Bin Batching for Increasing LLM Inference Throughput"
description: "As large language models (LLMs) grow in popularity for their diverse capabilities, improving the efficiency of their inference systems has become increasingly critical."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2412.04504) · [PDF](https://arxiv.org/pdf/2412.04504)

## 一句话摘要

As large language models (LLMs) grow in popularity for their diverse capabilities, improving the efficiency of their inference systems has become increasingly critical.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) grow in popularity for their diverse capabilities, improving the efficiency of their inference systems has become increasingly critical. Batching LLM requests is a critical step in scheduling the inference jobs on servers (e.g. GPUs), enabling the system to maximize throughput by allowing multiple requests to be processed in parallel. However, requests often have varying generation lengths, causing resource underutilization, as hardware must wait for the longest-running request in the batch to complete before moving to the next batch. We formalize this problem from a queueing-theoretic perspective, and aim to design a control policy which is throughput-optimal under a static-batching framework. We propose Multi-Bin Batching, a simple yet effective method that can provably improve LLM inference throughput under this framework by grouping requests with similar (predicted) execution times into predetermined bins. Through a combination of theoretical analysis and experiments, including real-world LLM inference scenarios with static and continuous-batching baselines, we demonstrate that multi-bin batching substantially improves throughput over static batching and quantify the remaining gap to native continuous batching under both oracle and estimated length information.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: continuous batching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ozgur Guldogan, Jackson Kunde, Kangwook Lee, Ramtin Pedarsani
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
