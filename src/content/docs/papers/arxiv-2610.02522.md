---
title: "Beaver: Elastic GPU Sharing between ML and Latency-Critical vRAN Workloads"
description: "Within the shared industry vision of AI-RAN, AI-and-RAN seeks to co-locate virtualized radio access network (vRAN) workloads and AI services on shared GPUs."
---

**评分：46/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2610.02522) · [PDF](https://arxiv.org/pdf/2610.02522)

## 一句话摘要

Within the shared industry vision of AI-RAN, AI-and-RAN seeks to co-locate virtualized radio access network (vRAN) workloads and AI services on shared GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Within the shared industry vision of AI-RAN, AI-and-RAN seeks to co-locate virtualized radio access network (vRAN) workloads and AI services on shared GPUs. This sharing is inherently asymmetric: vRAN workload is latency-critical, whereas the machine learning (ML) workload is a throughput-oriented, best-effort co-tenant. We present Beaver, a GPU sharing system that jointly manages compute and memory resources while protecting the vRAN's strict processing deadline. Beaver sizes the vRAN's streaming multiprocessor (SM) allocation from each slot's scheduled workload, repartitions SM allocations at slot granularity, and rewrites compiled ML kernels to yield HBM bandwidth during the vRAN's memory-critical phases. We implement Beaver and evaluate it using NVIDIA Aerial with heterogeneous multi-cell workloads, real-world cellular traces, production inference kernels, and full-stack LLM serving. On an H200 GPU, Beaver keeps the vRAN's p99.9 latency within its 1.5ms uplink deadline while retaining 74% of Llama-3.3-70B serving throughput. It also incurs no observed deadline misses under replayed cellular traces, protects a 375us downlink deadline, and generalizes to other GPUs including A100, GB10 and GH200.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu sharing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuncheng Yao, Zhenzhou Qi, Junyao Zheng, Chung-Hsuan Tung, Danyang Zhuo, Tingjun Chen
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
