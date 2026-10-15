---
title: "A Simple Plug-in for Improving Eviction-Based KV Cache Compression"
description: "KV cache growth is a major bottleneck for long-context inference in large language models."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2605.23258) · [PDF](https://arxiv.org/pdf/2605.23258)

## 一句话摘要

KV cache growth is a major bottleneck for long-context inference in large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV cache growth is a major bottleneck for long-context inference in large language models. Existing methods are often dominated by binary eviction or representation approximation, which may underutilize tokens that are not critical for exact retention but are still reconstructable. We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction. VECTOR combines an importance signal from the base scorer with a reconstructability signal from an offline-calibrated regression-based value estimation. By leveraging reconstructability, VECTOR recovers useful value information that would otherwise be irreversibly lost under binary eviction, while preserving key vectors for attention routing stability. On LongBench, RULER with contexts up to 128K tokens, and multi-turn SCBench, VECTOR yields significant gains over its base eviction methods under high compression. At a 90% compression ratio, SnapKV augmented with VECTOR outperforms six competing compression methods, including D2O and RocketKV, on all three evaluated models. Since VECTOR makes all routing decisions at prefill, decoding runs on a standard compressed cache with no measurable overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuping Lin, Jiayuan Ding, Yue Xing, Pengfei He, Jiliang Tang, Subhabrata Mukherjee
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
