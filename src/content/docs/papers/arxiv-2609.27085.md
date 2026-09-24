---
title: "Crossflow: Prefill-Decode Elasticity for Agentic LLM Serving"
description: "As serving capacity demand surpasses that of training, serving efficiency becomes increasingly important."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > Prefill-Decode 解耦

[论文原文](https://arxiv.org/abs/2609.27085) · [PDF](https://arxiv.org/pdf/2609.27085)

## 一句话摘要

As serving capacity demand surpasses that of training, serving efficiency becomes increasingly important.

## 为什么值得关注

待编辑增强。

## 摘要原文

As serving capacity demand surpasses that of training, serving efficiency becomes increasingly important. Prefill-decode (P/D) disaggregation improves serving efficiency through specialization and isolation of the two phases. These benefits rest on a static partitioning. Phase demand, however, is not static. We observe that in a large LLM fleet the ratio of uncached input to output tokens has peak-to-mean ratios up to 4.7x at minute timescales, and that in a public agentic trace the hourly ratio spans a median 24.5x within a single day, while reassigning a replica takes tens of minutes. Agentic traffic sharpens the mismatch. Sizing each pool at its ninety-fifth percentile leaves up to 17% of cluster capacity unused; sizing below it converts the same imbalance into queueing and unrealized throughput. We present Crossflow, which makes this boundary elastic without changing node roles. Each decode node publishes a short-lived, revocable lease that bounds local-prefill compute, KV capacity, transfer work, and projected output. Across public and internal traces, Crossflow improves token throughput by 16.2-17.4% on geometric mean over static P/D, and by up to 43.4% at high load, while reducing mean TTFT at every evaluated point.

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

- taxonomy keywords: prefill-decode
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yi Xu, Ehsan K. Ardestani, Wenyin Fu, Martin Schatz, Krishna Malladi, Zhan Shu, Adnan Aziz, Shobhit Kanaujia, Ajit Mathews, Chunqiang Tang
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
