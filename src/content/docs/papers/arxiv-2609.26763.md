---
title: "SARA: SLO-Aware Resource Allocation for Disaggregated Agentic LLM Services"
description: "Recent advances in large language models (LLMs) are driving the emergence of multi-modal and agentic services for mobile users through cloud and edge infrastructures, where long-context workloads pose daunting challenges for inference latency."
---

**评分：48/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.26763) · [PDF](https://arxiv.org/pdf/2609.26763)

## 一句话摘要

Recent advances in large language models (LLMs) are driving the emergence of multi-modal and agentic services for mobile users through cloud and edge infrastructures, where long-context workloads pose daunting challenges for inference latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advances in large language models (LLMs) are driving the emergence of multi-modal and agentic services for mobile users through cloud and edge infrastructures, where long-context workloads pose daunting challenges for inference latency. Existing disaggregated LLM serving systems largely rely on hardware profiling, configuration enumeration, or heuristic scheduling, offering limited analytical guidance for cost-efficient resource allocation. In this paper, we propose SARA, a Service level objectives (SLOs)-Aware Resource Allocation framework for disaggregated agentic LLM serving systems, which maximizes goodput under a deployment cost constraint and a series of quantile-based SLO constraints. By capitalizing on queuing theory, we first model the prefill, KV cache transfer, and decode stages as an M/G/k queue, an M/G/1 queue, and a generalized birth-death process, respectively. The analysis reveals that the prefill and decode stages are dominantly limited by computational capacity and high-bandwidth memory (HBM) resources, respectively. With these mathematical models, we further derive tractable tail behaviors of different stage-wise service level metrics for both light- and heavy-tailed workloads. These characterizations explicitly map workload, model architecture, and hardware parameters to stage-wise SLO constraints and minimum resource requirements. Finally, we develop an effective resource allocation framework to maximize system goodput under limited cost budgets. Simulation and hardware results demonstrate that the proposed framework accurately predicts the stage-wise SLO with mean errors below 5%, and improves system goodput by 26.6% on average over state-of-the-art baseline methods under the same deployment cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shicong Liu, Xianghao Yu, Zhen Gao, Jun Zhang
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
