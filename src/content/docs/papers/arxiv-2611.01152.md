---
title: "Capacity Planning for Resource-Constrained Clinical LLM Serving"
description: "Deploying large language models (LLMs) under a fixed accelerator budget requires jointly deciding how computational capacity is allocated across model sizes and how incoming requests are routed across that capacity."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.01152) · [PDF](https://arxiv.org/pdf/2611.01152)

## 一句话摘要

Deploying large language models (LLMs) under a fixed accelerator budget requires jointly deciding how computational capacity is allocated across model sizes and how incoming requests are routed across that capacity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying large language models (LLMs) under a fixed accelerator budget requires jointly deciding how computational capacity is allocated across model sizes and how incoming requests are routed across that capacity. Although prior work has extensively studied LLM routing and serving efficiency, the relative importance of fleet composition and routing under resource constraints remains less understood. We investigate this question using a controlled four-GPU serving environment with heterogeneous clinical NLP workloads spanning short factual verification, biomedical semantic matching, and long-context clinical summarization. We systematically vary fleet composition, routing policy, and offered load while holding the workload trace and hardware budget fixed. Across 24 configurations, descriptive main-effect shares attribute more variation to fleet composition than to the evaluated routing policies in time to first token, latency, and long-context coverage. All-small fleets provide the best responsiveness and throughput but substantially lower long-context coverage, whereas larger-model capacity improves coverage at the cost of serving efficiency. Heterogeneous fleets provide intermediate operating points but can introduce strong-model bottlenecks when large-model capacity is scarce. In a focused evaluation of this bottleneck, capacity-aware routing reduces mean latency and increases throughput while incurring a small reduction in long-context coverage. Within this measured regime, the results support prioritizing capacity allocation, with routing managing demand within the provisioned capacity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Tang, Geoffrey Martin, Yiye Zhang, Yifan Peng
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
