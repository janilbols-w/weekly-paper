---
title: "A Dependency-Aware Multi-GPU Training Framework for Temporal Graph Neural Networks"
description: "Temporal graph neural networks (TGNNs) achieve superior performance in many dynamic graph learning tasks."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](http://arxiv.org/abs/2610.15730v1) · [PDF](https://arxiv.org/pdf/2610.15730v1)

## 一句话摘要

Temporal graph neural networks (TGNNs) achieve superior performance in many dynamic graph learning tasks.

## 为什么值得关注

待编辑增强。

## 摘要原文

Temporal graph neural networks (TGNNs) achieve superior performance in many dynamic graph learning tasks. These models use node state vectors (i.e., memories) to capture and record graph changes (i.e., events), and then exploit these memories to assist prediction. However, this memory-centric design makes multi-GPU training challenging because predictions for later events often depend on memory updates from earlier events. To maintain model quality, existing multi-GPU TGNN training schemes strictly preserve all event dependencies, which limits parallelism and causes expensive cross-GPU memory synchronization. In this work, we observe that many of these dependencies can be handled more flexibly without harming training quality. Specifically, (a) dependencies in TGNN training have high locality in both time and graph topology, (b) the short-range dependencies missed within a large batch can often be recovered cheaply, and (c) many memory updates are not immediately needed. Based on these observations, we propose DepBloom to accelerate multi-GPU TGNN training with three techniques: (1) temporally bounded spatial partitioning to reduce unnecessary cross-GPU synchronization and improve parallelism; (2) intra-batch memory refinement to recover missing short-range temporal dependencies inside enlarged batches; and (3) critical-path optimization to prioritize urgent memory updates while deferring non-critical work during multi-GPU pipeline execution. Experimental results across representative models and diverse datasets show that DepBloom achieves an average speedup of 2.84$\times$ and up to 5.16$\times$ over state-of-the-art methods, while maintaining comparable or better model accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yang Zhao, Yue Dai, Liang Qiao, Buxin Tu, Bo Liu, Sen Zhang, Yi Zhang, Xiaoyu Hao, Jun Shi, Junshi Chen, Hong An
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
