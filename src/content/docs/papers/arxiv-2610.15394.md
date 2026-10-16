---
title: "WUSPruner: Second-Moment-Optimal Transforms for Structured Pruning"
description: "Structured pruning is typically formulated as identifying which model dimensions to remove, often within the model's original representation."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.15394v1) · [PDF](https://arxiv.org/pdf/2610.15394v1)

## 一句话摘要

Structured pruning is typically formulated as identifying which model dimensions to remove, often within the model's original representation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning is typically formulated as identifying which model dimensions to remove, often within the model's original representation. However, the effect of coordinate deletion fundamentally depends on the basis in which pruning is performed. This raises a more fundamental question: how should the basis be chosen specifically for coordinate deletion? We introduce WUSPruner, a transform-based framework for structured pruning of large language models. We formulate basis selection as a local linear reconstruction problem that directly minimizes the reconstruction loss induced by pruning. Inspired by the second-moment transformation in WUSH, we consider a WUS transform constructed jointly from activation and weight statistics. We show that under positive-definite second moments, WUS transform minimizes the local reconstruction loss over all invertible changes of basis. In the resulting basis, the activation and weight second moments are simultaneously diagonalized and balanced, causing the deletion error to decompose into independent spectral contributions and yielding a principled criterion for coordinate selection. Guided by this result, we develop a scalable pruning method based on blockwise WUS transformations and compact input projections. Experiments on Llama and Qwen models from 8B to 72B parameters show consistent improvements over structured pruning baselines across language modeling, knowledge, commonsense reasoning, mathematics, and code generation benchmarks, while also delivering practical reductions in inference latency and memory usage.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shengkun Tang, Dan Alistarh, Zhiqiang Shen
- 发布：2026-10-11；更新：2026-10-11
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
