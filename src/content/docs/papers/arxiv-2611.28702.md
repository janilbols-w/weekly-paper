---
title: "HiPerfCC-KVCache: Accelerating Confidential LLM Serving with Hierarchical KV Caching"
description: "Hierarchical key-value (KV) caching reduces repeated prefill computation in large language model serving by retaining reusable state beyond GPU memory."
---

**评分：49/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.28702) · [PDF](https://arxiv.org/pdf/2611.28702)

## 一句话摘要

Hierarchical key-value (KV) caching reduces repeated prefill computation in large language model serving by retaining reusable state beyond GPU memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hierarchical key-value (KV) caching reduces repeated prefill computation in large language model serving by retaining reusable state beyond GPU memory. Under GPU confidential computing (CC), however, protected transfers can erase this benefit. We show that bulk KV copies hold driver locks during prolonged CPU-side processing, stalling independent serving operations despite separate threads and streams. Our characterization on Hopper and Blackwell GPUs shows how lock scope, copy granularity, and allocation ownership affect foreground progress and transfer parallelism. Guided by these findings, we present HiPerfCC-KVCache, which manages resource lifetimes, prioritizes ready token readback between bounded backup submissions, and parallelizes KV restores through auxiliary contexts with shared GPU staging. Implemented in SGLang, HiPerfCC-KVCache uses existing protected transfer interfaces without hardware or driver changes. Across three models and three workloads on H200, HiPerfCC-KVCache achieves a geometric-mean output-token throughput speedup of $1.74\times$ (up to $2.72\times$) over the staged KV-transfer HiCache-Workers baseline at the highest tested loads. Mean time to first token decreases by 36% on average and up to 59%. The benefits generalize to RTX PRO 6000 Blackwell, with a geometric-mean throughput speedup of $1.28\times$ (up to $2.20\times$) over the same baseline. A capacity analysis further models and explains variation in gains and remaining gaps to CC-off serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haoxuan Xu, Shaoyu Wang, Minghao Lin, Beijie Liu, Potung Yu, Yongqin Wang, Vincent Quentin Ulitzsch, Seo Jin Park, Murali Annavaram, Mengyuan Li
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
