---
title: "Agentic Autoscaling through Worker-Pool Orchestration for LLM-driven Text Classification in Cloud Computing Environments"
description: "The growing adoption of large language model (LLM)-based systems for large-scale text processing has created a critical need for dynamic autoscaling to manage high-latency, bursty, and computationally intensive workloads."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2609.14898) · [PDF](https://arxiv.org/pdf/2609.14898)

## 一句话摘要

The growing adoption of large language model (LLM)-based systems for large-scale text processing has created a critical need for dynamic autoscaling to manage high-latency, bursty, and computationally intensive workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

The growing adoption of large language model (LLM)-based systems for large-scale text processing has created a critical need for dynamic autoscaling to manage high-latency, bursty, and computationally intensive workloads. This paper proposes an agentic autoscaling framework through worker-pool orchestration for LLM-driven text classification. The framework integrates a priority task queue, a dynamic pool of agent workers, a real-time metrics collector, and an application-layer autoscaler. Its classifier-agnostic design supports both zero-shot and fine-tuned language models without modifying the autoscaling logic. The framework is evaluated using Autoscaling+BART and Autoscaling+DeBERTa against static allocation and standalone RoBERTa and DistilBERT baselines. On the AG News dataset, Autoscaling+BART achieves 84.5% accuracy, while Autoscaling+DeBERTa improves it to 90.5%. On the SMS Spam Collection dataset, Autoscaling+DeBERTa achieves 99.5% accuracy, whereas Autoscaling+BART attains 84.5% accuracy with lower execution time. Overall, the proposed framework consistently outperforms the baseline approaches in resource efficiency while maintaining high classification performance, demonstrating that elastic worker-pool orchestration provides an effective and cost-efficient solution for scalable LLM-driven text classification in cloud environments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: autoscaling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bablu Kumar, Anshul Verma, Rajkumar Buyya
- 发布：2026-09-14；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
