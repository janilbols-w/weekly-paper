---
title: "MORTIS: Compiler-Guided KV-Cache Management for LLM Agent Programs"
description: "Existing agent serving systems divide each prompt into a reusable prefix and an opaque suffix, managing the KV-cache at this coarse granularity without distinguishing the components within each part."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.08638) · [PDF](https://arxiv.org/pdf/2611.08638)

## 一句话摘要

Existing agent serving systems divide each prompt into a reusable prefix and an opaque suffix, managing the KV-cache at this coarse granularity without distinguishing the components within each part.

## 为什么值得关注

待编辑增强。

## 摘要原文

Existing agent serving systems divide each prompt into a reusable prefix and an opaque suffix, managing the KV-cache at this coarse granularity without distinguishing the components within each part. We observe that prompt components differ in which LLM calls share their values and how long those values remain reusable, a property we term intra-prompt heterogeneity. Our key insight is that, in frameworks that generate prompts from typed LLM function calls, these components correspond to program variables, allowing compiler analysis to recover their sharing patterns and lifetimes. We present MORTIS, a compiler-serving co-design that combines this analysis with runtime observations to improve KV-cache management. MORTIS reorders prompt components to expose additional prefix reuse and uses their predicted reuse and lifetimes to guide cache retention, eviction, and prefetching. Our evaluation shows that MORTIS achieves up to 1.99x job completion time (JCT) speedup and 1.97x throughput improvement over SGLang, with geometric-mean speedups of 1.45x and 1.49x, respectively.

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

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xiaoyu Ma, Jayanaka L. Dantanarayana, Savini Kashmira, Baichuan Li, Lingjia Tang, Jason Mars
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
