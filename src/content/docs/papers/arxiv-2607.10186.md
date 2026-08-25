---
title: "FlashAccel: Leveraging High-Bandwidth Flash (HBF) for High-Throughput LLM Inference"
description: "Large language model (LLM) inference is increasingly limited by the capacity of High-Bandwidth Memory (HBM) in GPUs, as model weights and KV cache grow rapidly."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.10186) · [PDF](https://arxiv.org/pdf/2607.10186)

## 一句话摘要

Large language model (LLM) inference is increasingly limited by the capacity of High-Bandwidth Memory (HBM) in GPUs, as model weights and KV cache grow rapidly.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) inference is increasingly limited by the capacity of High-Bandwidth Memory (HBM) in GPUs, as model weights and KV cache grow rapidly. High-Bandwidth Flash (HBF) provides higher capacity than HBM while offering comparable bandwidth, making it a promising substrate for capacity-constrained LLM inference. However, its inherently high access latency, low bandwidth utilization, and lack of support for heterogeneous resource management make it difficult to integrate HBF into GPUs for LLM inference. We present FlashAccel, a co-designed system that enables efficient LLM inference using HBF. FlashAccel integrates HBF into HBM-based GPUs, providing architectural support to mitigate access latency. It improves bandwidth utilization through specialized data layouts for both model weights and KV cache, and introduces an HBF-aware storage management layer together with a programming model to organize persistent data in HBF and coordinate heterogeneous memory resources at the system level. Experimental results demonstrate that integrating six HBF stacks into the GPU enables FlashAccel to deliver an average improvement of 2.49$\times$ and 1.93$\times$ in throughput per GPU and energy efficiency over the HBM-only GPU under a 100ms latency constraint, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xinyu Wang, Yalong Xue, Xiaotian Sun, Xiaoyu Zhang, Xinjiang Zhang, Chunmeng Dou, Xueqi Li, Xiaoming Chen
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
