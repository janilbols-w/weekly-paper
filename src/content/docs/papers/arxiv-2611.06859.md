---
title: "Balancing hierarchical representation and quantization: A performance trade-off in text embeddings"
description: "Hierarchical text embedding models offer variable-length representations, while quantization reduces numerical precision; both aim to improve computational efficiency."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.06859) · [PDF](https://arxiv.org/pdf/2611.06859)

## 一句话摘要

Hierarchical text embedding models offer variable-length representations, while quantization reduces numerical precision; both aim to improve computational efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hierarchical text embedding models offer variable-length representations, while quantization reduces numerical precision; both aim to improve computational efficiency. This work is an empirical benchmark study of how these two orthogonal, already-established techniques interact. We evaluate 38 tasks from the Massive Text Embedding Benchmark (MTEB) using four transformer-based embedding models, covering 1D and 2D hierarchical representations combined with 32-bit, 8-bit, and binary quantization, for 168 configurations per task. We report each efficiency dimension separately: theoretical per-vector storage and end-to-end evaluation time. Under a Friedman test with Nemenyi post-hoc analysis, int8 quantization is statistically indistinguishable from float32 for pair classification and re-ranking and costs at most 1.5 percentage points overall, whereas binary quantization is significantly worse across every task category. Halving the embedding dimension once is not statistically detectable above $m=16$; two successive halvings always are. Combining an 8x dimensionality reduction with int8 yields a 32x reduction in per-vector storage at 94.4% of baseline effectiveness. Because evaluation times were measured once, we treat them as indicative: we find no evidence that quantization speeds up evaluation, whereas sampling from intermediate layers shortens it substantially. Retrieval degrades far faster than every other category, so we report findings per task category.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Kai Ponel, Marco Polignano, Erasmo Purificato, Aylin Julia Temizkan, Marco Levantesi, Giovanni Semeraro, Ernesto William De Luca
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
