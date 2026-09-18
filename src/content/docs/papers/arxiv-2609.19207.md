---
title: "MeshKV: A Network-on-Chip KV Cache Fabric for Scalable Transformer Decoding Accelerators"
description: "Autoregressive transformer decoding is constrained by irregular key-value (KV) cache movement on tiled accelerators."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.19207) · [PDF](https://arxiv.org/pdf/2609.19207)

## 一句话摘要

Autoregressive transformer decoding is constrained by irregular key-value (KV) cache movement on tiled accelerators.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive transformer decoding is constrained by irregular key-value (KV) cache movement on tiled accelerators. Prior compression and DRAM-placement systems still concentrate traffic on centralized memory paths that bottleneck long-context serving. We present MeshKV, a KV cache fabric that moves blocks as packetized flows over a lightweight NoC. It co-designs (i) TaKV affine striping to spread homes and cut hotspot load, (ii) Mare multicast with verified duplicate suppression, and (iii) Pad, which overlaps prefetch, tile multiply, and streaming softmax behind credit-aligned FIFOs. Together they convert bisection back-pressure into useful KV transfer. On our 8x8 FPGA implementation with LLaMA-2-7B and Mistral-7B at 8K-32K, MeshKV reduces interconnect traffic by up to 58%, improves KV bandwidth utilization by 2.1x, and delivers up to 1.9x multi-stream throughput.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dong Liu, Yanxuan Yu
- 发布：2026-09-16；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
