---
title: "Large Language Models for AI Infrastructure"
description: "Large language models (LLMs) are increasingly used to design, optimize, and operate the infrastructure behind AI training and serving, yet the literature remains fragmented across hardware design, machine learning systems, electronic design automation, and high-performance computing."
---

**评分：47/100** · AI 基础设施 > 集群与资源系统 > GPU 调度与虚拟化

[论文原文](https://arxiv.org/abs/2611.19061) · [PDF](https://arxiv.org/pdf/2611.19061)

## 一句话摘要

Large language models (LLMs) are increasingly used to design, optimize, and operate the infrastructure behind AI training and serving, yet the literature remains fragmented across hardware design, machine learning systems, electronic design automation, and high-performance computing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are increasingly used to design, optimize, and operate the infrastructure behind AI training and serving, yet the literature remains fragmented across hardware design, machine learning systems, electronic design automation, and high-performance computing. We present a comprehensive survey of LLM-assisted AI infrastructure across its lifecycle, from accelerator design and kernel engineering to compilation, deployment, operations, data management, and energy optimization. We organize the literature by the primary resource the LLM manages: artifact-centric methods for computational artifacts, operational-centric methods for deployment context and system state, and resource-centric methods for data and energy. These categories span the lifecycle and cover AI-specific concerns such as distributed-training configuration, inference serving, GPU-cluster scheduling, and data loading. Building on this taxonomy, we conduct a cross-study quantitative synthesis of reported results. Because studies adopt heterogeneous benchmarks, baselines, hardware, and metrics, we compare methods only where evaluation conditions permit and align results along common dimensions: functional correctness, execution performance, throughput, resource and energy consumption, operational outcomes, and optimization cost, keeping each result's native metric, baseline, and setting rather than collapsing them into a single score. This comparison reveals where LLM-driven methods yield consistent gains, how reported gains in workload orchestration depend on the evaluation environment, from simulators to real clusters and production, and where evidence is still lacking. Together, the taxonomy, lifecycle perspective, and quantitative evaluation provide an evidence-grounded reference for LLM-driven engineering of AI infrastructure.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: cluster scheduling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bolin Shen, Shaoyi Huang, Yushun Dong
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
