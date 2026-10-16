---
title: "TensorDex: A Compact, Tensor-Centric Storage System for Modern AI Models"
description: "Modern model hubs store hundreds of petabytes of large language models (LLMs), with fine-tuned variants dominating the storage footprint."
---

**评分：43/100** · AI 基础设施 > 集群与资源系统 > 存储与数据平面

[论文原文](https://arxiv.org/abs/2604.17104) · [PDF](https://arxiv.org/pdf/2604.17104)

## 一句话摘要

Modern model hubs store hundreds of petabytes of large language models (LLMs), with fine-tuned variants dominating the storage footprint.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern model hubs store hundreds of petabytes of large language models (LLMs), with fine-tuned variants dominating the storage footprint. These variants contain substantial cross-model redundancy that delta compression can exploit by storing only the difference between a target and a reference model. However, compression effectiveness depends critically on choosing a similar reference. At model-hub scale, this is challenging because model lineage metadata is often missing or unreliable, and different tensors within the same model may be most similar to tensors from different models. Consequently, model-level pairing leaves substantial redundancy unexploited. We present TensorDex, a lossless, tensor-centric storage system that performs delta compression at tensor granularity. TensorDex decomposes models into tensors, uses compact bit-level fingerprints to predict tensor-pair compressibility, and incrementally organizes tensors into multi-center clusters to select effective bases as new models arrive. Evaluated on 2,890 randomly sampled Hugging Face models, TensorDex reduces storage footprint by 70.5%, 37% lower than the state-of-the-art design. It achieves 22.9 GB/s compression and 28.4 GB/s decompression throughput, 3.86x and 1.49x faster than the next-best system, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: storage system
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tingfeng Lan, Zirui Wang, Yunjia Zheng, Zhaoyuan Su, Juncheng Yang, Yue Cheng
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
