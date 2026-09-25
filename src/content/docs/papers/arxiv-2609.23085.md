---
title: "Measured Joules, Learned Routes: Learning to Route for Energy-Efficient LLM Serving"
description: "Large language models (LLMs) and agentic AI systems are creating rapidly growing inference energy demands as model sizes grow and reasoning trajectories extend."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.23085) · [PDF](https://arxiv.org/pdf/2609.23085)

## 一句话摘要

Large language models (LLMs) and agentic AI systems are creating rapidly growing inference energy demands as model sizes grow and reasoning trajectories extend.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) and agentic AI systems are creating rapidly growing inference energy demands as model sizes grow and reasoning trajectories extend. While in practice, many queries do not require the capabilities of the largest available model, and routinely directing such queries to a high-capability model can introduce unnecessary, considerable computation and energy consumption. In this paper, we investigate whether adaptive routing across a heterogeneous pool of LLMs can reduce this energy burden without substantially compromising task performance. We design a language-model-based router that reads in each query and selects an answer model from a fixed candidate pool. The candidate models are first profiled through an offline tournament that records their correctness, latency, power, and GPU energy for each query. Using these measurements, the router is trained through supervised fine-tuning followed by group relative policy optimization (GRPO) with the tailored paradigms. Results demonstrate that learned routing can selectively allocate expensive model capacity based on query context and improve the accuracy-energy tradeoff in multi-LLM serving. Across seven benchmark tasks, we also observe a sharp accuracy-energy phase transition among routers, providing practical insights into improving energy efficiency while maintaining LLM performance.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Muhammad Abdur Rab Siddiqui, Daniela Rojas, Chen Yang, Wenqi Cui, Yuanyuan Shi, Yize Chen
- 发布：2026-09-19；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
