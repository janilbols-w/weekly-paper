---
title: "From Overloaded to Guaranteed: High-Throughput Multi-SLO Enforcement for LoRA-Assisted On-Premise LLM Deployment"
description: "As Large Language Models (LLMs) become essential in privacy-sensitive sectors like hospitals and government agencies, the on-premise LLM servers offer a cost-effective and secure alternative to public cloud services."
---

**评分：45/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.04956) · [PDF](https://arxiv.org/pdf/2610.04956)

## 一句话摘要

As Large Language Models (LLMs) become essential in privacy-sensitive sectors like hospitals and government agencies, the on-premise LLM servers offer a cost-effective and secure alternative to public cloud services.

## 为什么值得关注

待编辑增强。

## 摘要原文

As Large Language Models (LLMs) become essential in privacy-sensitive sectors like hospitals and government agencies, the on-premise LLM servers offer a cost-effective and secure alternative to public cloud services. However, these resource-constrained servers struggle to guarantee heterogeneous Service Level Objectives (SLOs) when serving multiple LoRA-adapted services simultaneously. Existing serving frameworks suffer from severe SLO violations due to the computational overhead of LoRA layers and the rigid nature of batch scheduling. To address this, we propose HALO, a scheduling method tailored for LoRA-assisted on-premise LLM deployment. HALO introduces two key innovations: a spatial multiplexing strategy that overlaps Base and LoRA computations by partitioning GPU Streaming Multiprocessors (SMs), and an SLO-aware scheduler that decouples request execution based on "request-level slack." By prioritizing urgent tasks and utilizing idle budget for traffic shaping, HALO significantly mitigates resource contention. Our evaluation demonstrates that HALO minimizes SLO violations while improving throughput compared to state-of-the-art baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zeshen Zhang, Han Zhao, Weihao Cui, Quan Chen, Yu Liu, Yongjun Deng, Jing Yang, Jiuchen Shi, Chen Chen, Youmin Chen, Yu Feng, Minyi Guo
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
