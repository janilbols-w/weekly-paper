---
title: "Composable CXL Memory as a Kubernetes-Native Shared Memory for LLM Serving"
description: "We present a Kubernetes Dynamic Resource Allocation (DRA) driver that makes composable CXL memory a schedulable cluster resource, and evaluate the resulting shared-memory tier for cross-node KV-cache reuse in LLM serving."
---

**评分：46/100** · AI 基础设施 > 集群与资源系统 > 资源解耦

[论文原文](https://arxiv.org/abs/2609.10790) · [PDF](https://arxiv.org/pdf/2609.10790)

## 一句话摘要

We present a Kubernetes Dynamic Resource Allocation (DRA) driver that makes composable CXL memory a schedulable cluster resource, and evaluate the resulting shared-memory tier for cross-node KV-cache reuse in LLM serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present a Kubernetes Dynamic Resource Allocation (DRA) driver that makes composable CXL memory a schedulable cluster resource, and evaluate the resulting shared-memory tier for cross-node KV-cache reuse in LLM serving. The driver composes CXL regions on demand, materializes them as DAX devices on each participating host, and injects them into pods under a single Container Device Interface (CDI) name so that pods on different nodes access the same physical region. A shared-memory connector for vLLM/llm-d uses that region as a KV-cache tier with a slot directory embedded inside the shared medium, which eliminates the need for an external metadata service. On a two-node cluster with a 512\,GiB CXL appliance and Qwen2.5-7B-Instruct, cross-node prefix reuse reduces TTFT by 5.5$\times$--36.6$\times$ at an external hit rate of 95.4--99.5\,\%, while node-local tiers (GPU prefix caching, CPU-DRAM offload) fall back to full recompute. The sharing gap, defined as the latency ratio between cross-node and same-node reuse, is 1--4\%, indicating that cross-node reuse incurs little additional latency relative to same-node reuse on our testbed. Both replicas run full engines; the study demonstrates memory disaggregation rather than prefill/decode disaggregation. We report this as a feasibility study rather than a performance evaluation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cxl memory, memory disaggregation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongjian Fan, Kevin Zhang, David Habinsky, Sean Dykstra
- 发布：2026-09-09；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
