---
title: "NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?"
description: "With the growing demand for large language model (LLM) services, optimizing LLM serving systems is becoming increasingly complex, and the bottleneck is no longer predicting how a given configuration will perform."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.29255) · [PDF](https://arxiv.org/pdf/2611.29255)

## 一句话摘要

With the growing demand for large language model (LLM) services, optimizing LLM serving systems is becoming increasingly complex, and the bottleneck is no longer predicting how a given configuration will perform.

## 为什么值得关注

待编辑增强。

## 摘要原文

With the growing demand for large language model (LLM) services, optimizing LLM serving systems is becoming increasingly complex, and the bottleneck is no longer predicting how a given configuration will perform. The harder problem is deciding what to investigate: which mechanisms matter for a workload, which configurations are worth testing, and what evidence a decision still needs. In this work, we present NoeVera, an agentic Second Brain that goes beyond just one-shot retrieval by turning papers, code, benchmarks, and experimental results into a persistent, provenance-preserving knowledge base with three planes: source evidence, reusable synthesis, and agent memory. Decision-aware retrieval assembles compact evidence packs, role-specific agents reason over them and invoke a simulator (Vidur or GAUSS) whenever quantitative support is needed, and every finding is written back as a scoped evidence record, so knowledge guides experiments and experiments refine knowledge. In configuration search over four serving scenarios, NoeVera comes within 5% of the optimum in a median of 6-7 simulator calls, versus 9 for Bayesian optimization and 15 for a knowledge-free agent with the same tools; on A100 GPUs, its representative configurations deliver ~1.30x vLLM-default throughput and meet every scenario's latency objective. When reused, provenance-preserving evidence records over-generalize on only 8% of applicability traps, versus 28% for a general-purpose agent memory. On the held-out 48-task split of a 72-task benchmark, NoeVera scores 29% higher than an equally equipped agent and 36% higher than its single-call retrieval counterpart (0.80 vs. 0.62 and 0.59), and even when baselines receive NoeVera's own prompts, a statistically significant part of its evidence-evolution advantage remains.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Pinaki Prasad Guha Neogi, Spyros Mastorakis, Ankur Mallick, Saravan Rajmohan, Victor Rühle
- 发布：2026-11-22；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
