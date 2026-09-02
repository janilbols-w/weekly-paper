---
title: "DRLM: Deep Reinforcement Learning-Based LLM Query Orchestration in Edge Environments"
description: "Large language model (LLM) services increasingly process heterogeneous queries with diverse latency, accuracy, and resource requirements."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.00442) · [PDF](https://arxiv.org/pdf/2609.00442)

## 一句话摘要

Large language model (LLM) services increasingly process heterogeneous queries with diverse latency, accuracy, and resource requirements.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) services increasingly process heterogeneous queries with diverse latency, accuracy, and resource requirements. While edge deployment reduces response time, the heterogeneity of devices and the diversity of model families, parameter scales, and quantization levels make efficient LLM query orchestration challenging. This paper introduces DRLM, a Deep Reinforcement Learning-based LLM query orchestration framework in edge environments. DRLM integrates two lightweight predictors: (i) a class-conditioned quality estimator that maps queries to semantic categories and infers model performance, and (ii) a feature-driven latency predictor that estimates inference time across model-device configurations. These predictions, combined with system state, feed a factorized Proximal Policy Optimization (PPO) agent that performs state-aware orchestration decisions. To enable data-driven orchestration, we construct a large-scale benchmarking dataset with 223 835 measurements spanning 1258 queries, 6 query classes, 8 model families (32 deployed instances), 5 quantization levels, and heterogeneous edge devices. Evaluation on a 64-node edge cluster and comparison with three baselines and two state-of-the-art methods show that DRLM reduces inference latency by up to 51% and queuing delay by up to 67 %, while incurring at most 8% accuracy loss. It improves latency under increasing workloads up to 61.4%, demonstrating robust and stable orchestration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Reza Farahani, Zoha Azimi Ourimi, Mario Colosi, Lauri Loven, Christian Timmerer, Schahram Dustdar
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
