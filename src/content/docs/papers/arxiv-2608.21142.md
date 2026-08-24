---
title: "COEC: Calibrated Orthogonal-Equivalence Compensation for Structured Pruning of Large Language Models"
description: "Structured pruning reduces the size and inference cost of large language models (LLMs) by removing weight columns, but the resulting output error can degrade accuracy."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.21142) · [PDF](https://arxiv.org/pdf/2608.21142)

## 一句话摘要

Structured pruning reduces the size and inference cost of large language models (LLMs) by removing weight columns, but the resulting output error can degrade accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Structured pruning reduces the size and inference cost of large language models (LLMs) by removing weight columns, but the resulting output error can degrade accuracy. Existing training-free compensation methods use an additive bias or a single orthogonal rotation on the output side of the retained weight. These corrections leave its input singular frame unchanged and therefore limit how the retained weight can adapt after column removal. We propose COEC (Calibrated Orthogonal-Equivalence Compensation), a training-free compensation framework that applies alternating left and right orthogonal rotations to the retained weight. The right rotation is optimized on a reduced Stiefel manifold, while singular values are rescaled using generalized cross-validation to select the regularization strength for each layer. COEC further tempers the calibration Gram matrix to reduce the dominance of high-energy activation directions and introduces an alignment penalty that preserves the geometric relation between adjacent attention projections.All components use second-order statistics from a small calibration set and require neither backpropagation through the LLM nor retraining of the model parameters. COEC is independent of the column pruning criterion and can be applied to multiple structured pruning methods. Experiments on the Llama-3, Llama-3.1, and Qwen2.5 model families across multiple structured sparsity levels show that COEC improves perplexity on every model and zero-shot accuracy in most settings over existing compensation methods, with larger gains at higher sparsity. These results show that post-pruning compensation can recover part of the performance lost to column removal.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Peiqi Yu, Nam Ling, Wei Wang, Wei Jiang
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
