---
title: "Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft Context Compression in RAG"
description: "Retrieval-Augmented Generation (RAG) improves knowledge-intensive generation by conditioning language models on retrieved documents, but processing these documents becomes increasingly expensive as retrieval depth grows."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.05152) · [PDF](https://arxiv.org/pdf/2609.05152)

## 一句话摘要

Retrieval-Augmented Generation (RAG) improves knowledge-intensive generation by conditioning language models on retrieved documents, but processing these documents becomes increasingly expensive as retrieval depth grows.

## 为什么值得关注

待编辑增强。

## 摘要原文

Retrieval-Augmented Generation (RAG) improves knowledge-intensive generation by conditioning language models on retrieved documents, but processing these documents becomes increasingly expensive as retrieval depth grows. Soft context compression reduces this cost by encoding documents into compact continuous representations that can be precomputed and reused across queries. However, many existing methods train compressed models by distilling from a full-context teacher. When the teacher is wrong, such distillation can reinforce its errors, while teacher imitation provides no direct signal for improving beyond the teacher. We propose DEX-Comp, a two-stage training recipe that separates reliable imitation from targeted exploration. Pure Distillation learns only from teacher-correct questions to mitigate error propagation, while Hard Exploration applies outcome-based reinforcement learning to teacher-failed questions to directly optimize answer correctness. Across five open-domain QA benchmarks and retrieval depths from top-$5$ to top-$30$, DEX-Comp at $16\times$ compression outperforms all evaluated compression baselines and surpasses the untuned full-context RAG model in average accuracy, while reducing time-to-first-token by $4.4\times$--$23.7\times$. Evaluations across additional datasets and backbones further demonstrate its generalization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shuyu Guo, Shuo Zhang, Zhaochun Ren
- 发布：2026-09-07；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
