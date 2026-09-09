---
title: "AutoUVM: Automated Prefetching Framework for LLMs under UVM Oversubscription"
description: "Large language models (LLMs) increasingly exceed the memory capacity of commodity GPUs, making memory oversubscription common in practical deployments."
---

**评分：44/100** · AI 基础设施 > 集群与资源系统 > 网络、RDMA 与互联

[论文原文](https://arxiv.org/abs/2609.06172) · [PDF](https://arxiv.org/pdf/2609.06172)

## 一句话摘要

Large language models (LLMs) increasingly exceed the memory capacity of commodity GPUs, making memory oversubscription common in practical deployments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) increasingly exceed the memory capacity of commodity GPUs, making memory oversubscription common in practical deployments. NVIDIA Unified Virtual Memory (UVM) provides transparent access to host memory, but its page-fault-driven migrations introduce severe performance overhead. While UVM exposes primitives (e.g., prefetching and placement hints) to mitigate these costs, they require low-level CUDA modifications, limiting their applicability for most LLM users. Meanwhile, existing UVM optimizations operate at coarse managed-object granularity and fail to capture deep learning frameworks' internal tensor-level memory behavior, leading to excessive data movement and CPU-GPU interconnect bottlenecks. We propose AutoUVM, an automated, framework-aware UVM prefetching system for efficient LLM execution under memory oversubscription. AutoUVM bridges the semantic gap between deep learning frameworks and UVM by exposing tensor-level access information and enabling policy-driven prefetching at fine granularity. Implemented as a transparent extension, AutoUVM requires no changes to model code and dynamically adapts to runtime memory pressure. We instantiate AutoUVM with a roofline-inspired policy to identify performance-critical data transfers. Across ten LLMs, AutoUVM achieves an average 3.1x speedup over baseline UVM and consistently surpasses the best-performing prior UVM prefetcher by 1.9x, with improvements of up to 4.7x over object-level prefetchers, while significantly reducing page faults.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: interconnect
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mao Lin, Hui Feng, Xianzhong Ding, Guilherme Cox, Qian Wang, Hyeran Jeon
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
