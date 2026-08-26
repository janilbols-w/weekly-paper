---
title: "RetrievalFormer: A Dual-Encoder Transformer for Efficient Approximate Nearest Neighbor Retrieval and Cold-Item Recommendation"
description: "A shared search-and-recommendation index must score new items from features alone because search has no exploration slot."
---

**评分：40/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.24079) · [PDF](https://arxiv.org/pdf/2608.24079)

## 一句话摘要

A shared search-and-recommendation index must score new items from features alone because search has no exploration slot.

## 为什么值得关注

待编辑增强。

## 摘要原文

A shared search-and-recommendation index must score new items from features alone because search has no exploration slot. In a public log covering both surfaces over one catalog, $38.6\%$ of held-out query-search impressions show an item never previously shown or visited. For user-cold engagements, the feature-based tower serves this demand without measurable loss against $99$ sampled negatives ($0.9595$ Recall@20 versus $0.9510$ warm). A lexical baseline reaches similar parity, while a full-catalog check remains statistically undecided. Dual-encoder retrieval therefore keeps the index \emph{open} to new items, unlike an ID-softmax recommender that requires retraining. We price this openness on recommendation against six sequential baselines, each retrained and tuned through five rounds on corrected targets. A float32 timestamp bug had reordered leave-one-out targets for $19.7\%$ of users. On MovieLens-1M, warm accuracy trails the strongest retrained baseline by $5.2\%$ Recall@20 and $11.4\%$ NDCG@20. On MIND, the gap narrows to $0.8$--$3.6\%$ relative to the five strongest baselines, though the model ranks sixth of seven. Under strict zero-leakage cold-start evaluation, the content tower achieves $0.172 \pm 0.006$ Recall@20, $1.4\times$ the strongest retrained dedicated method ($0.124 \pm 0.007$) and $3\times$ a training-free floor, without cold-specific training. Exact full-softmax training raises Recall@20 by $54\%$ on MIND-small and $6.9\%$ on MovieLens-1M over sampled InfoNCE, but recomputes the full catalog each step and exhausts accelerator memory at $240$K items. Approximate nearest-neighbor search explains none of the remaining gap, serving cost does not regress against ID-softmax retrieval, and a history-window sweep explains half the post-recipe remainder. Exact-quality training at catalog scale remains the open problem.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Theodore Rogers, Joe Standerfer, Dmitrii Timoshenko, Haoxue Li, Zuhaib Akhtar, Soyoung Yang
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
