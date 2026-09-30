---
title: "Beyond Selection: Token Parameterization for Extreme Visual Token Compression"
description: "Visual-token compression is effective for improving the efficiency of vision-language models, but under extreme compression budgets, token pruning can break visual grounding while learned resamplers increase parameter count, attention cost, and training complexity."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.35232) · [PDF](https://arxiv.org/pdf/2609.35232)

## 一句话摘要

Visual-token compression is effective for improving the efficiency of vision-language models, but under extreme compression budgets, token pruning can break visual grounding while learned resamplers increase parameter count, attention cost, and training complexity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Visual-token compression is effective for improving the efficiency of vision-language models, but under extreme compression budgets, token pruning can break visual grounding while learned resamplers increase parameter count, attention cost, and training complexity. We revisit compression through a token parameterization lens, separating (i) basis transformation and structured truncation (retained subspace/compressibility) from (ii) coordinate organization (optimization and cross-modal alignment). This view yields two coupled objectives, compressibility and learnability, which we formalize as unified functionals. Guided by these objectives, we design Braco, a lightweight four-step coder that combines transform-basis truncation, input-independent basis-coordinate embeddings, budget-dependent orthogonal re-parameterization, and learned spatial residual tokens from lightweight pooling. Experiments show that Braco forms the favorable empirical accuracy-efficiency frontier under $23\times$--$64\times$ compression and remains competitive at $144\times$, reaching 95.2% accuracy while reducing prefill FLOPs by 84.2%--86.7% relative to the uncompressed upper bound. Against prior methods, Braco matches or improves accuracy while achieving up to approximately 36% end-to-end speedup and using $16.6\times$/$78.8\times$ lower compressor latency/FLOPs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rui Zhong, Yu Li, Zheyu Yan, Cheng Zhuo
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
