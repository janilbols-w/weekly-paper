---
title: "FlashMoE: Reducing SSD I/O Bottlenecks via ML-Based Cache Replacement for Mixture-of-Experts Inference on Edge Devices"
description: "Recently, Mixture-of-Experts (MoE) models have gained attention for efficiently scaling large language models."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2601.17063) · [PDF](https://arxiv.org/pdf/2601.17063)

## 一句话摘要

Recently, Mixture-of-Experts (MoE) models have gained attention for efficiently scaling large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recently, Mixture-of-Experts (MoE) models have gained attention for efficiently scaling large language models. Although these models are extremely large, their sparse activation enables inference to be performed by accessing only a fraction of the model at a time. This property opens the possibility of on-device inference of MoE, which was previously considered infeasible for such large models. Consequently, various systems have been proposed to leverage this sparsity and enable efficient MoE inference for edge devices. However, previous MoE inference systems like Fiddler[8] or DAOP[13] rely on DRAM-based offloading and are not suitable for memory constrained on-device environments. As recent MoE models grow to hundreds of gigabytes, RAM-offloading solutions become impractical. To address this, we propose FlashMoE, a system that offloads inactive experts to SSD, enabling efficient MoE inference under limited RAM. FlashMoE incorporates a lightweight ML-based caching strategy that adaptively combines recency and frequency signals to maximize expert reuse, significantly reducing storage I/O. In addition, we built a user-grade desktop platform to demonstrate the practicality of FlashMoE. On this real hardware setup, FlashMoE improves cache hit rate by up to 51% over well-known offloading policies such as LRU and LFU, and achieves up to 2.6x speedup compared to existing MoE inference systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Byeongju Kim, Jungwan Lee, Donghyeon Han, Hoi-Jun Yoo, Sangyeob Kim
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
