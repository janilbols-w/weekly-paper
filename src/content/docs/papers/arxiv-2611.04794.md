---
title: "Accelerating Offloading-Based MoE Inference by Interleaving Concurrent Requests"
description: "Expert offloading enables large mixture-of-experts (MoE) language models to run locally, but conventional batching stalls the GPU while missing experts are fetched."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.04794) · [PDF](https://arxiv.org/pdf/2611.04794)

## 一句话摘要

Expert offloading enables large mixture-of-experts (MoE) language models to run locally, but conventional batching stalls the GPU while missing experts are fetched.

## 为什么值得关注

待编辑增强。

## 摘要原文

Expert offloading enables large mixture-of-experts (MoE) language models to run locally, but conventional batching stalls the GPU while missing experts are fetched. A popular remedy, known as prefetching, is to predict what experts will be needed soon and fetch them using idle link bandwidth. Imprecise prediction, however, wastes bandwidth and GPU memory on fetching unnecessary experts. Our key finding is that prefetching can be harmful when there is an expert cache in GPU memory. This is because as the cache includes more necessary experts, expert prediction becomes less precise. Our key insight is that proper request scheduling beats prefetching. Building on this insight, we present Bevy, an MoE inference system based on runahead inference for concurrent requests. A request whose experts are available can run ahead to later layers while other requests wait for fetches, revealing the experts it needs next. Bevy can then fetch the missing experts so identified while computing ready requests, overlapping computation and fetching without predicting expert selections. Running requests separately, however, repeats reads of shared weights in GPU memory and increases compute time. To limit this cost, Bevy's self-balancing scheduler batches ready requests at each layer and prioritizes lagging requests, adapting their grouping as expert availability changes. Across two local platforms, Bevy delivers up to 3.46$\times$ the decode throughput of llama.cpp and up to 1.55$\times$ that of the fastest prefetching baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory, offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongseung Yu, In Gim, Kyunghan Lee, Lin Zhong
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
