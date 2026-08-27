---
title: "Multi-Turn Reasoning LLMs for Task Offloading in Mobile Edge Computing"
description: "Emerging computation-intensive applications impose stringent latency requirements on resource-constrained mobile devices."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2604.07148) · [PDF](https://arxiv.org/pdf/2604.07148)

## 一句话摘要

Emerging computation-intensive applications impose stringent latency requirements on resource-constrained mobile devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Emerging computation-intensive applications impose stringent latency requirements on resource-constrained mobile devices. Mobile Edge Computing (MEC) addresses this challenge through task offloading. However, designing effective policies remains difficult due to dynamic task arrivals, time-varying channels, and the spatio-temporal coupling of server queues. Conventional heuristics lack adaptability, while Deep Reinforcement Learning (DRL) suffers from limited generalization and architectural rigidity, requiring retraining when network topology changes. Although Large Language Models (LLMs) offer semantic reasoning capabilities, standard Supervised Fine-Tuning (SFT) yields myopic policies that greedily minimize immediate latency without accounting for long-term system evolution. To address these limitations, we propose COMLLM, a generative framework that enables foresighted decision-making in MEC systems. COMLLM integrates Group Relative Policy Optimization (GRPO) with a Look-Ahead Collaborative Simulation (LACS) mechanism, which performs multi-step Monte Carlo rollouts while jointly modeling server queue dynamics. By incorporating these rollouts into the reward design, the framework captures the long-term impact of current decisions on future system states. Experimental results demonstrate that COMLLM achieves near-optimal latency and improved load-balancing fairness. Notably, it exhibits zero-shot topological scalability, allowing a model trained on small-scale networks to generalize to larger, unseen topologies without retraining, outperforming SFT, DRL, and heuristic baselines.

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

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ning Yang, Chuangxin Cheng, Haijun Zhang
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
