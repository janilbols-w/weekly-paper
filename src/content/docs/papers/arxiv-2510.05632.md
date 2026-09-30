---
title: "Systematic Exploration of Multi-core Architectures for Efficient LLM Serving using WaferAI-SIM"
description: "With the widespread adoption of Large Language Models (LLMs), the demand for high-performance LLM inference services continues to grow."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2510.05632) · [PDF](https://arxiv.org/pdf/2510.05632)

## 一句话摘要

With the widespread adoption of Large Language Models (LLMs), the demand for high-performance LLM inference services continues to grow.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the widespread adoption of Large Language Models (LLMs), the demand for high-performance LLM inference services continues to grow. Multi-core AI accelerators, such as Groq, Graphcore IPU, and Cerebras WSE, provide promising platforms for LLM serving, but their distributed memory systems require careful coordination between hardware configuration and serving policies. Otherwise, mismatched tensor partitioning, data placement, and memory management can substantially underutilize compute and communication resources. To address these challenges, we present WaferAI-SIM, a multi-level simulation framework that combines transaction-level simulation with an analytical performance model. WaferAI-SIM enables simulator-driven co-design of LLM serving strategies and multi-core accelerator architectures, targeting the early design stage in which emerging platforms are not yet broadly available for empirical serving studies. It captures how LLM serving policies interact with compute-core count, memory hierarchy, and interconnect topology, enabling architecture-aware exploration beyond GPU-centric assumptions. We evaluate representative LLMs across a range of chip configurations and serving scenarios. Across the evaluation, WaferAI-SIM reports 1.32$\times$--6.03$\times$ latency improvements, where the lower endpoint comes from ring-based placement at TP=16 over the placement baselines, and the upper endpoint comes from K-dimension TP over MN-dimension TP for Qwen3\_4B at TP=4 with sequence length 256. For LLM serving, our findings provide guidance for co-designing hardware architectures and serving strategies for multi-core AI accelerators across diverse LLM workloads.

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

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Zhu, Dahu Feng, Erhu Feng, Yubin Xia
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
