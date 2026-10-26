---
title: "InferSlice: A Reference Architecture for SLO-driven LLM Inference over a Telco Wide-Area Network"
description: "LLM inference is increasingly deployed as a core service for enterprise and interactive applications, but sovereignty, compliance, latency and resource-locality requirements can limit the suitability of centralised cloud deployments."
---

**评分：44/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2610.32638) · [PDF](https://arxiv.org/pdf/2610.32638)

## 一句话摘要

LLM inference is increasingly deployed as a core service for enterprise and interactive applications, but sovereignty, compliance, latency and resource-locality requirements can limit the suitability of centralised cloud deployments.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM inference is increasingly deployed as a core service for enterprise and interactive applications, but sovereignty, compliance, latency and resource-locality requirements can limit the suitability of centralised cloud deployments. Telco operators offer geographically distributed compute and network infrastructure for addressing these constraints. However, existing LLM serving frameworks are designed for tightly coupled data centres and provide limited support for coordinating geographically distributed and heterogeneous resources. We present InferSlice, a reference architecture for Service-Level Objective (SLO)-driven LLM inference over a telco infrastructure, integrating network slicing, GPU partitioning, elastic serving and observability. Led by BT in collaboration with the University of Bristol and NVIDIA, and realised on the JOINER UK national-scale wide-area network (WAN), InferSlice is evaluated on service differentiation across tiers, elastic scale-out, client-edge bandwidth as a bottleneck, and the reach of tensor, pipeline, data parallelism, and prefill/decode disaggregation over the WAN. Our results show that, on a general-purpose telco network, tiers yield distinct latency-throughput regimes, and weight streaming shortens scale-out time. Replication is placement-insensitive but memory-bound; pipeline parallelism tolerates near- and mid-cross-site hops, while tensor parallelism and disaggregation fail beyond a single subnet hop. We share practical insights from operating SLO-driven inference on a telco network, lessons learned and open questions, and hope to encourage further research on distributed and heterogeneous LLM inference systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Juan Parra-Ullauri, Anthony Chiu, Hari Madhukumar, Zhaozhou Wu, Anderson Bravalheri, Alex Healing, Andy Corston-Petrie, Dimitra Simeonidou, Nektaria Efthymiou
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
