---
title: "Rethinking Tabular Foundation Models On Data Streams"
description: "Tabular foundation models (TFMs) outperform established machine learning models on tabular benchmarks through in-context learning."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.05352) · [PDF](https://arxiv.org/pdf/2610.05352)

## 一句话摘要

Tabular foundation models (TFMs) outperform established machine learning models on tabular benchmarks through in-context learning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Tabular foundation models (TFMs) outperform established machine learning models on tabular benchmarks through in-context learning. Building on this success, interest is growing in applying them to data streams, where data arrive continuously and evolve over time. On a stream, a TFM adapts by updating its context rather than its parameters, so its accuracy and cost depend on which examples it keeps and how often it rebuilds its context. We therefore present a systematic study of TFMs on data streams, covering memory management, computational cost, and stream-specific challenges such as concept drift and delayed labels. We find that TFMs achieve the highest predictive performance and that simply retaining the most recent examples is as effective as existing memory management techniques. They also recover faster than streaming learners after drift and keep the highest accuracy under label delay. This accuracy, however, comes at a high serving cost, since a nearly unchanged context is re-encoded at every prediction. These results point to architectural efficiency as the way forward for in-context stream learning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nilesh Verma, Daniel Nowak-Assis, Afonso Louren\c{c}o, Albert Bifet, Bernhard Pfahringer, Maroua Bahri, Nick Jin Sean Lim
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
