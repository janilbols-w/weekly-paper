---
title: "HBFSim: A Simulator for Exploring HBF in Memory Hierarchies for LLMs"
description: "High Bandwidth Flash (HBF) has recently emerged as a promising technology that provides terabyte-scale accelerator-local capacity at bandwidths approaching HBM, with a potential cost-per-bit advantage over HBM."
---

**评分：46/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.23503) · [PDF](https://arxiv.org/pdf/2610.23503)

## 一句话摘要

High Bandwidth Flash (HBF) has recently emerged as a promising technology that provides terabyte-scale accelerator-local capacity at bandwidths approaching HBM, with a potential cost-per-bit advantage over HBM.

## 为什么值得关注

待编辑增强。

## 摘要原文

High Bandwidth Flash (HBF) has recently emerged as a promising technology that provides terabyte-scale accelerator-local capacity at bandwidths approaching HBM, with a potential cost-per-bit advantage over HBM. However, its NAND foundation brings long latency, out-of-place updates, and finite write endurance directly into the accelerator memory hierarchy, making its effects on performance and lifetime difficult to predict. To study this emerging design space, we present HBFSim, an LLM-aware event-driven simulator for heterogeneous HBM+HBF memory systems that preserves application-level memory semantics while modeling flash-internal behavior. HBFSim models HBM, HBF with host-managed flash translation, and conventional capacity tiers in one simulation driven by a calibrated serving frontend. Using HBFSim, we study decoding of Llama-3.1-70B and Qwen3-235B-A22B under three workloads that differ in their input and output lengths. HBF serves data that does not fit in HBM 11.0--19.0$\times$ faster than host DRAM; HBM is better used to hold the running sequences' KV cache than as a cache for HBF; and at a published peak load of Llama-3.1-70B, HBF lasts 2.0 to 6.9 years, in proportion to the stacks that share the KV writes. The artifact is available at https://github.com/FlashLabAE/HBFSim and will track public HBF device data as it becomes available.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jinheng Li, Guosheng Wang, Hongchao Du, Shangyu Wu, Qiao Li, Chun Jason Xue
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/FlashLabAE/HBFSim](https://github.com/FlashLabAE/HBFSim)
- 阅读深度：metadata
