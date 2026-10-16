---
title: "EdgeLLM-Nano: Auditing Polar-Guided Key-Cache Compression and Consistency-Anchored Pruning on a 33.6 MB On-Device Language Model"
description: "Deploying language models (LMs) on the edge presents unique memory, latency, and power challenges absent in high-performance computing."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.14475v1) · [PDF](https://arxiv.org/pdf/2610.14475v1)

## 一句话摘要

Deploying language models (LMs) on the edge presents unique memory, latency, and power challenges absent in high-performance computing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying language models (LMs) on the edge presents unique memory, latency, and power challenges absent in high-performance computing. KV-cache compression emerges as a promising approach to address these challenges. However, the effectiveness of current KV-cache compression methods has not been thoroughly examined on edge devices. Moreover, we show that existing evaluation methods do not always involve the KV-cache under test. We propose EdgeLLM-Nano, a measurement study of KV-cache compression using a nano-scale decoder-only LM (transformer) testbed that has 8.39M parameters, i.e., 33.6 MB, to enable end-to-end examination of each backend, seed, and power sample. Our results give a negative verdict for a polar-guided key-cache quantizer (round-to-nearest (RTN) control causes an order of magnitude less damage), as well as a consistency-anchored progressive weight pruner (one-shot magnitude-based pruning performs as well as, if not better). We also introduce Long-Context Decode Fidelity (LCDF) evaluation, a token-by-token examination of teacher-forced log-losses using the KV-cache under test. Unlike perplexity that gives the same 5.461 score to all methods, LCDF distinguishes different KV-cache compression backends thanks to its paired statistics across seeds and effect sizes. Our companion Raspberry Pi 5 measurement shows all compression backends we tested to be less energy-efficient per token compared to uncompressed FP16 inference. Except for KIVI that is close to lossless in terms of LCDF, our findings indicate KV-cache compression can be improved. LCDF offers a simple and effective way of shedding light on KV-cache compression methods, whose negative impacts have been overlooked by perplexity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：S M Mahbub Murshed, Hayden Bright, Rezaul Karim, Ali Shiri Sichani
- 发布：2026-10-10；更新：2026-10-10
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
