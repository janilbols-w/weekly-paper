---
title: "Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving"
description: "Container-granularity scheduling leaves abundant short-lived idle slices within containers unexploited."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.15762) · [PDF](https://arxiv.org/pdf/2608.15762)

## 一句话摘要

Container-granularity scheduling leaves abundant short-lived idle slices within containers unexploited.

## 为什么值得关注

待编辑增强。

## 摘要原文

Container-granularity scheduling leaves abundant short-lived idle slices within containers unexploited. Reallocating containers is too heavyweight to utilize such fine-grained opportunities under SLA constraints, and operator-level scheduling requires reasoning about dependencies, memory safety, and cluster-wide execution dynamics in real time. In this paper, we present SliceScheduler, a dynamic operator-level scheduling system for multi-tenant model serving. The key idea is to expose cluster-wide operator execution state and enable what-if reasoning over scheduling decisions. SliceScheduler consists of four key components. First, we introduce the Global Mapping Graph (GMG), a unified abstraction that captures operator dependencies, tensor shapes, resource mappings, and execution states, providing a real-time, cluster-wide view with explicit resource semantics. Second, we build a global simulator on top of GMG to predict operator-level execution and memory evolution under candidate placements. Third, we design an incremental, simulation-based scheduling module that selects placements to exploit fragmented idle slices while avoiding memory violations and preserving SLA. Finally, we develop an operator executor that materializes scheduling decisions on GPUs and coordinates computation and cross-accelerator transfers. We implement SliceScheduler as a PyTorch backend and evaluate it using production trace replay. Experimental results show that SliceScheduler improves token throughput by 1.10--2.29$\times$ compared to existing approaches, while maintaining SLA violations within 9\%. SliceScheduler demonstrates that operator-level scheduling is a practical and effective approach to improving GPU utilization for multi-tenant LLM serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Weinan Liu, Zeyuan Ding, Dian Ding, Chengcheng Wan, Lu Tang, Guangtao Xue, Jiwu Shu, Yiming Zhang
- 发布：2026-08-16；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
