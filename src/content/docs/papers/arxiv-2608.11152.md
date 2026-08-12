---
title: "Scheduling Mixed RL Rollouts Beyond Prefix Locality"
description: "Modern reinforcement learning (RL) post-training pipelines for large language models (LLMs) increasingly combine rollout workloads across multiple domains and feedback paradigms."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.11152) · [PDF](https://arxiv.org/pdf/2608.11152)

## 一句话摘要

Modern reinforcement learning (RL) post-training pipelines for large language models (LLMs) increasingly combine rollout workloads across multiple domains and feedback paradigms.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern reinforcement learning (RL) post-training pipelines for large language models (LLMs) increasingly combine rollout workloads across multiple domains and feedback paradigms. Prefix-aware routing improves inference efficiency through cache reuse and load balancing, but it does not control how heterogeneous rollout sessions compete for KV-cache capacity. When reinforcement learning with verifiable rewards (RLVR), reinforcement learning from human feedback (RLHF), and agentic rollouts share an asynchronous inference service, their distinct sequence structures, interaction patterns, and KV-residency times create substantially different serving demands. Rollout scheduling must account for this heterogeneity without distorting the workload mixture specified by the trainer. We present MISA-T, a routing-layer admission policy for mixed rollout serving. MISA-T combines adaptive session admission, workload-aware KV-capacity allocation, and residency-time-aware KV accounting. In rollout-only ablations on Step3.7 and Qwen3.6-35B-A3B, MISA-T improves rollout throughput over a sweep-tuned cache-aware vLLM Router by 53.3% and 43.6%, respectively, while maintaining high prefix-cache hit rates. In a matched 50-iteration Step3.7 experiment, it increases rollout throughput by 35.6% and reduces mean iteration time by 22.8%, while keeping the consumed workload mixture close to the trainer target and achieving comparable task scores.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zetao Hong, Song Yuan, Yuanhao Ding, Yibo Zhu, Daxin Jiang, Zhibin Wang, Chen Tian
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
