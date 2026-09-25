---
title: "Automatic Rank Allocation for Low-Rank Adaptation in Large Language Models via lp Regularization"
description: "Low-rank adaptation (LoRA) has become a popular parameter-efficient fine-tuning method for large language models."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.28998) · [PDF](https://arxiv.org/pdf/2609.28998)

## 一句话摘要

Low-rank adaptation (LoRA) has become a popular parameter-efficient fine-tuning method for large language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Low-rank adaptation (LoRA) has become a popular parameter-efficient fine-tuning method for large language models. A key challenge in LoRA is how to determine the rank of each adaptation matrix, as rank directly controls its capacity and efficiency. Existing adaptive-rank methods typically allocate ranks according to manually designed importance scores, which are not directly derived from an optimization objective. In this work, we propose $\ell_p$-LoRA, a principled rank-allocation method based on $\ell_p$ regularization with $0 <1$, which is a classical sparsity-inducing technique in signal processing and statistics. Specifically, we regularize the energy of each rank-one LoRA component, encouraging redundant components to vanish while preserving important ones. We derive the corresponding proximal subproblem and reduce the matrix optimization to a two-dimensional problem, leading to an implicit thresholding criterion for identifying redundant components. Experiments on natural language understanding and question-answering tasks demonstrate that the proposed method achieves competitive performance with existing LoRA baselines.

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

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zebang Xie, Chuanyang Zheng, Yik-Chung Wu, Yihang Gao
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
