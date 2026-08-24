---
title: "DAOP: Data-Aware Offloading and Predictive Pre-Calculation for Efficient MoE Inference"
description: "Mixture-of-Experts (MoE) models, though highly effective for various machine learning tasks, face significant deployment challenges on memory-constrained devices."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2501.10375) · [PDF](https://arxiv.org/pdf/2501.10375)

## 一句话摘要

Mixture-of-Experts (MoE) models, though highly effective for various machine learning tasks, face significant deployment challenges on memory-constrained devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixture-of-Experts (MoE) models, though highly effective for various machine learning tasks, face significant deployment challenges on memory-constrained devices. While GPUs offer fast inference, their limited memory compared to CPUs means not all experts can be stored on the GPU simultaneously, necessitating frequent, costly data transfers from CPU memory, often negating GPU speed advantages. To address this, we present DAOP, an on-device MoE inference engine to optimize parallel GPU-CPU execution. DAOP dynamically allocates experts between CPU and GPU based on per-sequence activation patterns, and selectively pre-calculates predicted experts on CPUs to minimize transfer latency. This approach enables efficient resource utilization across various expert cache ratios while maintaining model accuracy through a novel graceful degradation mechanism. Comprehensive evaluations across various datasets show that DAOP outperforms traditional expert caching and prefetching methods by up to 8.20x and offloading techniques by 1.35x while maintaining accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yujie Zhang, Shivam Aggarwal, Tulika Mitra
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
