---
title: "Ember: Making Unified Virtual Memory Practical for Discrete-Memory GPUs"
description: "GPU working sets have outgrown GPU memory, so applications must oversubscribe it, keeping only hot data on the GPU."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.13408) · [PDF](https://arxiv.org/pdf/2610.13408)

## 一句话摘要

GPU working sets have outgrown GPU memory, so applications must oversubscribe it, keeping only hot data on the GPU.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPU working sets have outgrown GPU memory, so applications must oversubscribe it, keeping only hot data on the GPU. NVIDIA's Unified Virtual Memory (UVM) supports oversubscription, but its performance degrades once data exceeds the GPU's memory. This stems from its fault-driven data placement, wasting interconnect bandwidth, and underutilizing the GPU. This raises the question: can UVM oversubscription become practical on stock GPUs, exploiting GPU memory speed and minimizing wasted interconnect bandwidth, without placement hints, profiling runs, or application changes? To this end, we present Ember, a UVM management framework for oversubscribed workloads. Ember introduces a hybrid address space; allocations start as mapped into host memory, omitting data migration. Ember's counter-driven region promotion uses GPU's hardware counters to fetch hot regions to the GPU, its decay-based eager reclamation proactively evicts cold regions in batches, while via online region re-placement, Ember tracks the hot set at runtime. We implement Ember within NVIDIA's open-source UVM driver for unmodified applications and as a userspace variant on stock CUDA. At 1.5x oversubscription, it is 6.8-10.6x faster than UVM on six applications across three PCIe GPUs, and generates LLM tokens 4.7-16x faster at sizes where manual placement cannot run at all. Without a profiling run, it beats a profile-guided alternative by 2.1x on kernel time.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Senad-Leandro Lemes Galera, Michail Georgoulakis Misegiannis, Ferdinand Gruber, Jana Giceva, Dimitrios Stavrakakis
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
