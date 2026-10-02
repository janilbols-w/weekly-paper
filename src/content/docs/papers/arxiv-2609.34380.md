---
title: "DPS: Dual-Mode Precision LLM Serving with Semi-Unified Memory"
description: "Existing LLM serving systems virtualize and optimize KV-cache memory, but treat model-weight memory as fixed throughout execution."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](http://arxiv.org/abs/2609.34380v1) · [PDF](https://arxiv.org/pdf/2609.34380v1)

## 一句话摘要

Existing LLM serving systems virtualize and optimize KV-cache memory, but treat model-weight memory as fixed throughout execution.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing LLM serving systems virtualize and optimize KV-cache memory, but treat model-weight memory as fixed throughout execution. Recent work on multi-precision model representations challenges this design by allowing a single stored model to support both full-accuracy and lower-precision execution, making the effective weight footprint runtime-dependent. This creates an opportunity under bursty workloads, where temporary spikes in KV-cache demand often determine throughput and SLO compliance. We present DPS, a dual-precision LLM serving system that turns weight memory into an elastic resource: under normal load, DPS serves the full-accuracy model; under KV pressure, it switches to a nested, lower-precision variant and repurposes unused weight memory for KV cache blocks. DPS is built on Semi-Unified Memory (SUM), which partitions the weight region into a persistent lower-precision sub-region and a shared region that alternates between residual weight tensors and KV-cache blocks, preserving compatibility with paged KV-cache management. We implement DPS on top of vLLM and evaluate it across both dense and MoE models and various production workload traces. Our results show that \sysname improves sustained throughput by $2.1$--$3.3\times$ and effective pass@1 by up to $+41$\,pp over Static FP16, while preserving FP16-class accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: unified memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuan Truong Nguyen, Tien Son Pham, Tuan Duc Chu, Wookeun Jung, Thanh Tuan Dao
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
