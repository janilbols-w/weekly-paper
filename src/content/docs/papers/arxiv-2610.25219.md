---
title: "gKSM: GPU Memory Deduplication at Driver Layer for Serverless LLM Inference"
description: "In serverless LLM inference, cloud providers commonly locate multiple instances on a single GPU to improve utilization."
---

**评分：51/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.25219) · [PDF](https://arxiv.org/pdf/2610.25219)

## 一句话摘要

In serverless LLM inference, cloud providers commonly locate multiple instances on a single GPU to improve utilization.

## 为什么值得关注

待编辑增强。

## 摘要原文

In serverless LLM inference, cloud providers commonly locate multiple instances on a single GPU to improve utilization. However, each instance independently maintains its model weights and runtime state, making duplicate GPU memory the primary bottleneck. Memory deduplication is a widely-used technique for eliminating duplicate data in CPU systems, but extending it to GPU memory faces fundamental challenges. Effective GPU memory deduplication must avoid redundant data movement between CPU and GPU while preserving write isolation for shared pages without native copy-on-write (COW) support. This paper presents gKSM, a transparent GPU memory deduplication framework for serverless LLM inference. gKSM addresses these challenges through CPU-GPU collaborative hash management that offloads hash computation to GPU kernels, zero-copy model weight deduplication that eliminates duplication before model weight transfer, and a cross-privilege page fault handler that combines a lightweight kernel hook and CUDA Virtual Memory Management (VMM) remapping in the user space. gKSM also designs a stable page scanning algorithm and a reuse-aware placement policy in cluster scale. Experiments show that gKSM reduces GPU memory usage by 59.8% while maintaining high throughput compared to ServerlessLLM. Under memory constrained workloads, gKSM improves aggregate throughput by 2.15X and supports five instances concurrently. In cluster level simulation, gKSM achieves a service rate of 99.97%, compared to 78.2% for SLInfer and 26.9% for ServerlessLLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, memory management
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shuheng Gao, Fan Guo, Yongkun Li, Ziye Yue, Yinlong Xu, John C. S. Lui
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
