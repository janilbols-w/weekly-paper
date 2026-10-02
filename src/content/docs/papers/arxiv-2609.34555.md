---
title: "PulseInfer: I/O-Centric Sparse KV Cache Offloading for Efficient Long-Context LLM Decoding"
description: "Long-context LLM serving is increasingly bottlenecked by decode, where large KV caches limit batch size and underutilize GPUs."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.34555) · [PDF](https://arxiv.org/pdf/2609.34555)

## 一句话摘要

Long-context LLM serving is increasingly bottlenecked by decode, where large KV caches limit batch size and underutilize GPUs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM serving is increasingly bottlenecked by decode, where large KV caches limit batch size and underutilize GPUs. Sparse KV cache offloading expands effective capacity by storing most historical KV blocks in CPU DRAM and recalling only selected blocks on demand. However, we find that existing offloading systems shift the bottleneck to CPU-GPU recall I/O: recall volume varies widely across layers, decode steps and requests, while headwise sparse selection fragments recalls into many small PCIe transfers. This paper presents PulseInfer, an I/O-centric sparse KV cache offloading system. PulseInfer hides variable recall latency with interruptible layer-wise scheduling, adapts offloading decisions with IO-Adaptive Offloading Admission, and coalesces fragmented transfers using SoloHead sparse selection and a gather-scatter I/O engine. Implemented on SGLang, PulseInfer improves decode throughput by up to 4.7x over SGLang and 2.6x over the best existing offloading baseline, while reducing TPOT by up to 76% and preserving near-lossless accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Qiuyang Zhang, Kai Zhou, Kai Lu, Haocheng Lu, Jian Zhou, Yuanpeng Su, Kun Bao, Jiguang Wan, Fei Wu
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
