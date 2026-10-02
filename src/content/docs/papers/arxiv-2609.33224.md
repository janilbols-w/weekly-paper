---
title: "PackServe: SLO-Aware Request Scheduling for Agentic LLM Serving at Scale"
description: "Request scheduling is a key challenge in large-scale clusters serving agentic large language model (LLM) workloads."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](http://arxiv.org/abs/2609.33224v1) · [PDF](https://arxiv.org/pdf/2609.33224v1)

## 一句话摘要

Request scheduling is a key challenge in large-scale clusters serving agentic large language model (LLM) workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

Request scheduling is a key challenge in large-scale clusters serving agentic large language model (LLM) workloads. An effective scheduler must preserve key-value cache (KVC) reuse across long, shared prefixes, meet token-level latency service-level objectives (SLOs), and minimize GPU resource footprint. Existing schedulers struggle to reconcile these requirements: request consolidation can sacrifice cache locality and increase prefill/decode interference, compromising both SLO attainment and resource efficiency. We present PackServe, a scheduler designed to reduce resource costs while meeting latency SLOs for agentic LLM serving. PackServe uses compact white-box models to predict latency under prefill/decode interference. Guided by these predictions, it packs requests onto fewer serving instances while preserving KVC reuse and SLO constraints, trading available latency headroom for improved per-instance throughput. Evaluation on 64 NVIDIA H20 GPUs shows that PackServe uses up to 16.8% and 24.6% fewer GPU-hours than state-of-the-art schedulers under 30-ms and 50-ms TPOT targets, respectively, while meeting the target TPOT objectives. PackServe has also been deployed in our production cluster comprising over 1000 GPUs, where it reduces the resource footprint by 34.7% compared with the original production scheduler.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: request scheduling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiyuan Tan, Dejiang Zhu, Jingzhe Jiang, Yihao Zheng, Yang Tian, Tao Wang, Minchen Yu
- 发布：2026-09-27；更新：2026-09-27
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
