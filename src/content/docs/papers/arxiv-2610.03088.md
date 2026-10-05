---
title: "Coda: Exploiting Admission Flexibility for Coding-Agent Serving"
description: "Coding agents powered by large language models (LLMs) repeatedly alternate between model inference and tool calls, creating long-lived sessions with reusable key-value (KV) states and asynchronous request resumptions."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.03088) · [PDF](https://arxiv.org/pdf/2610.03088)

## 一句话摘要

Coding agents powered by large language models (LLMs) repeatedly alternate between model inference and tool calls, creating long-lived sessions with reusable key-value (KV) states and asynchronous request resumptions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Coding agents powered by large language models (LLMs) repeatedly alternate between model inference and tool calls, creating long-lived sessions with reusable key-value (KV) states and asynchronous request resumptions. Logical readiness, however, does not ensure efficient admission in a shared serving system. Through direct trace analysis and trace-driven replay, we identify two mismatches: reusable KV states reside across storage tiers and incur unequal computational costs for state preparation, while requests with heterogeneous context lengths can decode inefficiently together. Our central insight is that exploiting admission flexibility can improve serving performance while preserving request progress. We present Coda, a coding-agent serving system that realizes this insight through a readiness-informed admission layer incorporating two mechanisms. Tiered-Aging state admission exploits bounded flexibility in admission order to improve admission efficiency and preserve request progress. Compatibility-Aware execution admission exploits flexibility in attention grouping within each model iteration to reduce mixed-context interference and improve shared decoding efficiency. For multi-worker configurations, Coda introduces a separate routing layer that considers KV-state residency, worker load, and request-to-worker context-length compatibility to guide efficient request placement. We evaluate Coda across different models and workloads against state-of-the-art coding-agent serving systems and vLLM. Across the single-worker and multi-worker experiments, Coda improves output-token and SLO-compliant throughput by 20.3% and 70.5% on average, with peak gains of 29.3% and 140.2%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Youhe Jiang, Fangcheng Fu, Binhang Yuan, Krishna Malladi, Ehsan K. Ardestani, Zhan Shu, Adnan Aziz, Yi Xu
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
