---
title: "Efficient GPU Retrieval for Semantic Search"
description: "Semantic Search on LinkedIn must retrieve relevant profiles from a corpus of hundreds of millions in response to natural-language queries such as \"a fintech founder in Berlin who worked in payments.\" The deployed relevance policy is bottleneck-oriented: every active non-negotiable facet must be satisfied, and a pre-existing LLM Graded Relevance (GR) judge op"
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.28968) · [PDF](https://arxiv.org/pdf/2608.28968)

## 一句话摘要

Semantic Search on LinkedIn must retrieve relevant profiles from a corpus of hundreds of millions in response to natural-language queries such as "a fintech founder in Berlin who worked in payments." The deployed relevance policy is bottleneck-oriented: every active non-negotiable facet must be satisfied, and a pre-existing LLM Graded Relevance (GR) judge op

## 为什么值得关注

待编辑增强。

## 摘要原文

Semantic Search on LinkedIn must retrieve relevant profiles from a corpus of hundreds of millions in response to natural-language queries such as "a fintech founder in Berlin who worked in payments." The deployed relevance policy is bottleneck-oriented: every active non-negotiable facet must be satisfied, and a pre-existing LLM Graded Relevance (GR) judge operationalizes this through a fixed min/median aggregation over facet grades. Cosine similarity instead averages evidence, letting a strong match on one facet mask failure on another, capping the recall of the first-stage (L0) retriever. We present a policy-aligned retrieval framework: embeddings are partitioned into eight category-supervised segments whose scores follow the same min/median rule at serving time; for multi-vector retrieval, this segment score is computed independently per tagged document slot and maximized across slots. A lightweight single-slot Stage-1 scorer generates high-recall candidates, while scale-invariant relative-norm gating keeps category activation consistent across training, evaluation, and serving. On 21K held-out queries, this representation improves offline relevance over a matched-capacity baseline, with gains broadly distributed across facet combinations. We serve this framework with a two-stage GPU architecture: an FP8 coarse ranker scores the full corpus, increasing per-shard capacity by 71% and Stage-1 matmul throughput by 36%, then an FP16 stage exactly re-ranks an oversampled candidate set, recovering 99.6-99.8% of full-FP16 recall at over 500 QPS per shard replica. In a member-randomized A/B test, exploratory-query Precision@10 under the unchanged GR judge rises from 63.7% to 79.0% and navigational Precision@1 from 65.5% to 74.7%, with a blinded human evaluation independently confirming the Precision@10 gain.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dhritiman Das, Chujie Zheng, Ronak Kaoshik, Pratik Dixit, Vishal Shah, Yanbo Li, Jiahao Xu, Manika Agarwal, Chinmay Naik, Lingyu Zhang, Chetan Bhole, Chirag Bhanuprasad Mehta, Meng Zheng, Puneet Singh Ahluwalia, Shirisha Singh, Ping Jin, Manas Apte, Gokulraj Mohanasundaram, Tugrul Bingol, Raghavan Muthuregunathan, Fedor Borisyuk
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
