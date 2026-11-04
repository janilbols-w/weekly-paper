---
title: "PrismServe: Efficient LLM Serving on Heterogeneous Accelerator Clusters"
description: "Serving large language models across heterogeneous accelerators is challenging because partitioning a replica across device types introduces communication overhead during autoregressive decoding, while deploying complete quantized replicas can degrade model quality."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2508.09204) · [PDF](https://arxiv.org/pdf/2508.09204)

## 一句话摘要

Serving large language models across heterogeneous accelerators is challenging because partitioning a replica across device types introduces communication overhead during autoregressive decoding, while deploying complete quantized replicas can degrade model quality.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving large language models across heterogeneous accelerators is challenging because partitioning a replica across device types introduces communication overhead during autoregressive decoding, while deploying complete quantized replicas can degrade model quality. We present PrismServe, a serving system that combines request-level collaboration across heterogeneous hardware with a mixture of quantized experts derived from the same foundation model. Each expert executes within a group of same-type accelerators in a single node, while a two-level router selects an expert based on predicted response quality and then selects a replica according to load and prefix-cache locality. Implemented on unmodified vLLM, PrismServe achieves 2.0--2.6$\times$ the throughput of cross-node or cross-vendor full-precision pipelined deployments and reduces P99 time per output token by 55--65\% when serving Qwen3-14B on 48 accelerators from three vendors. Across Qwen3-8B, Qwen3-14B, and Qwen3-32B on five downstream tasks, PrismServe outperforms the best single quantization method by 2.0--4.3 points while remaining within 1.4 points of full-precision accuracy. Our code is available at https://anonymous.4open.science/r/LLM-Inference-System-B000/

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinhao Zhang, Zicheng Yan, Boyang Zhang, Zeyu Liu, Daning Cheng, Yunquan Zhang, Guangming Tan, Xiang Gao
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
