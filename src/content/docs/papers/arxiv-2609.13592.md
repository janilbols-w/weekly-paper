---
title: "BOOST: Concurrent Access to Host Memory and HBM to Accelerate LLM Inference"
description: "GPU memory bandwidth and capacity limit throughput in large language model (LLM) inference."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.13592) · [PDF](https://arxiv.org/pdf/2609.13592)

## 一句话摘要

GPU memory bandwidth and capacity limit throughput in large language model (LLM) inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPU memory bandwidth and capacity limit throughput in large language model (LLM) inference. The GPU memory system consists of a primary tier of high-bandwidth memory (HBM) and a secondary tier of host memory connected via CPU-to-GPU interconnect. Current serving systems treat the tiers hierarchically: they serve exclusively from HBM when data fits, and otherwise prefetch data from host memory to HBM before use. In both cases, the host memory bandwidth is never well utilized. Prefetching expands capacity by utilizing host memory, but consumes HBM bandwidth for writes, reducing the bandwidth available for demand loads. We observe that fully utilizing both host and HBM bandwidth requires each wave of GPU threadblocks to access both tiers concurrently and in proportion to their bandwidth ratio. Existing bandwidth-proportional placement strategies fail to provide concurrency because they are not aware of GPU waves, and the large 2MB GPU page size. This paper presents BOOST, the first runtime system that provides concurrent and proportional access to both GPU memory tiers, extracting the combined bandwidth of host memory and HBM for LLM inference without kernel changes. The key insight in BOOST is to use kernel access patterns to make page allocation and runtime data management wave-aware. For static model weights, BOOST applies modulo-based page placement that eliminates access-ratio variance; for dynamically provisioned attention key-value (KV) pairs, it makes the free KV page pool wave-aware. We integrate BOOST into vLLM and evaluate on a Grace Hopper system. At iso-batch size, BOOST improves Time-per-Output-Token (TPOT) by 4.3% over HBM-only serving, whereas prefetching degrades TPOT by 6%. In high-throughput serving, BOOST improves throughput by 31% on average, outperforming prefetching by 15%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anish Saxena, Jae Hyung Ju, Hritvik Taneja, Po-An Tsai, Aamer Jaleel, Christos Kozyrakis, Moinuddin Qureshi
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
