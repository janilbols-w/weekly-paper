---
title: "Soft-NBCE: Entropy-Weighted Chunk Fusion for Long-Context"
description: "The quadratic complexity of self-attention remains a bottleneck for Large Language Models (LLMs) processing ultra-long contexts."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.01101) · [PDF](https://arxiv.org/pdf/2606.01101)

## 一句话摘要

The quadratic complexity of self-attention remains a bottleneck for Large Language Models (LLMs) processing ultra-long contexts.

## 为什么值得关注

待编辑增强。

## 摘要原文

The quadratic complexity of self-attention remains a bottleneck for Large Language Models (LLMs) processing ultra-long contexts. The Naive Bayes Cognitive Engine (NBCE) parallelizes long-context inference by chunking documents and routing to the lowest-entropy chunk at each decoding step. This hard-selection strategy causes semantic fragmentation during cross-chunk reasoning, as abrupt routing changes between adjacent tokens disrupt the model's contextual grounding. We present Soft-NBCE, a lightweight extension that replaces discrete chunk selection with soft entropy-weighted chunk fusion. A temperature-scaled Softmax over predictive entropies assigns continuous weights to all chunks, enabling log-space aggregation across chunk-conditioned distributions. To partially compensate for the conditional independence assumption introduced by chunking, we propose Consistency Distillation, a LoRA-based self-distillation that constrains the chunked logit distribution toward a full-context teacher via KL-divergence. On LongBench multi-hop benchmarks, Soft-NBCE with Consistency Distillation improves consistently over NBCE-style baselines (MuSiQue F1: 0.310 vs.\ 0.275 for Vanilla NBCE; HotpotQA F1: 0.479 vs.\ 0.427) while maintaining retrieval accuracy (NIAH-32K: 0.909) at O(L^2/n) peak memory.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shihao Ji, Mingyu Li, Zihui Song
- 发布：2026-08-25；更新：2026-08-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
