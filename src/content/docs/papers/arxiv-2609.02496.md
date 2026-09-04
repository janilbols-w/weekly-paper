---
title: "Debias-SparseGPT: Bias-Aware Pruning for Large Language Models"
description: "Model compression techniques such as pruning and quantization facilitate the efficient deployment and acceleration of Large Language Models (LLMs)."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.02496) · [PDF](https://arxiv.org/pdf/2609.02496)

## 一句话摘要

Model compression techniques such as pruning and quantization facilitate the efficient deployment and acceleration of Large Language Models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Model compression techniques such as pruning and quantization facilitate the efficient deployment and acceleration of Large Language Models (LLMs). However, recent studies show that weight sparsification methods, such as SparseGPT, can amplify existing biases in models, with outputs varying significantly depending on persona cues in the prompt. In this paper, we introduce Debias-SparseGPT, a post-training pruning method incorporating representational debiasing using a second-order term defined over demographically contrasting inputs. We perform empirical validation of our method over a wide range of generative LLMs. Across models and sparsity regimes (25%, 50%, and structured 2:4 sparsity), Debias-SparseGPT consistently reduces pruning-induced bias compared to SparseGPT while preserving model perplexity and zero-shot accuracy. Under the most restrictive 2:4 structured sparsity pattern, which most aggressively degrades model quality, augmenting the calibration set with long-context, content-rich examples further improves both downstream performance and fairness. Overall, Debias-SparseGPT advances the bias-performance trade-off while preserving the computational efficiency of sparse models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Irina Proskurina, Guillaume Metzler, Antoine Gourru, Julien Velcin
- 发布：2026-09-02；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/upunaprosk/debias-llm-compressor](https://github.com/upunaprosk/debias-llm-compressor)
- 阅读深度：metadata
