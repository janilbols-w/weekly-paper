---
title: "LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference"
description: "The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads."
---

**评分：46/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.33475) · [PDF](https://arxiv.org/pdf/2610.33475)

## 一句话摘要

The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads. However, serving massive foundation models under stringent Service Level Objectives (SLO) exposes critical physical and system bottlenecks. These challenges include the persistent High Bandwidth Memory (HBM) wall, operational asymmetry between compute-bound prefilling and memory-bandwidth-bound decoding, explosive Key-Value (KV) cache expansion, prohibitive serverless cold starts, and hardware reliability vulnerabilities. Existing literature reviews remain layer-siloed, decoupling low-level accelerator virtualization from cluster orchestration and runtime inference, while largely overlooking defining advancements from 2024 to 2026. To address these limitations, this study presents a comprehensive, cross-layer systematic review guided by the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 framework. We synthesize a holistic taxonomy unifying hardware virtualization, cluster-level scheduling, and runtime inference optimizations, including iteration-level continuous batching, prefill-decoding disaggregation, and hierarchical KV cache offloading. Furthermore, we evaluate resilient cloud-native service architectures, examining scale-to-zero serverless paradigms, fault-tolerant checkpointing against silent data corruption, and hardware-enforced Trusted Execution Environments (TEEs) for multi-tenant isolation. Finally, we formalize the multi-dimensional Pareto trade-offs governing throughput, latency, monetary cost, and confidentiality, outlining a forward-looking research roadmap spanning Compute Express Link (CXL) memory pooling, in-memory computing, and autonomous multi-agent control planes to guide future cloud LLM infrastructure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant, slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jannatun Noor, Athar Noor Mohammad Rafee, Md. Sadman Haque, Sreezon Das Gupta, Atiar Osman, Md. Abu Obaida Zishan
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
