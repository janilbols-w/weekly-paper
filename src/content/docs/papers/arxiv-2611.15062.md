---
title: "Probabilistic State Space Enumeration in Neural Network Computation"
description: "Many methods for pruning neural networks rank weights or groups of weights by importance and retain a single subset."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.15062) · [PDF](https://arxiv.org/pdf/2611.15062)

## 一句话摘要

Many methods for pruning neural networks rank weights or groups of weights by importance and retain a single subset.

## 为什么值得关注

待编辑增强。

## 摘要原文

Many methods for pruning neural networks rank weights or groups of weights by importance and retain a single subset. We study how channel groups contribute jointly to the output of multilayer perceptrons (MLPs) in Transformer language models. Inspired by network reliability analysis, probabilistic state space enumeration (PSSE) represents the dense MLP output as the expected importance-corrected masked output over $2^G$ joint states of $G$ channel groups. Summing the most probable states' probability-weighted outputs gives an approximation whose absolute error is bounded by the omitted probability mass times the maximum masked-output norm. NORDER-II adapts ORDER-II to enumerate states in decreasing probability without sorting the full space. Its first $B$ states maximize the probability mass captured at that budget. A weight-entropy scorer fixes each layer's ordering from pretrained weights. We evaluate all 168 MLP layers across six models from the Llama, Gemma, and Qwen families on two datasets with 8, 16, and 32 channel groups. In all 1,008 comparisons, the 95%-mass prefix yields lower mean relative error than uniform sampling at the same state count, with or without bias correction. At all three group counts, it also yields lower median and 99th-percentile relative error than a single top-$k$ mask. For downstream inference, we use the number of distinct channels in each prefix to set pruned MLP widths. With one validation-selected group count per model, PSSE achieves lower perplexity than both top-$k$ pruning baselines in all 36 matched-FLOP settings. Our pruned decoder MLPs achieve mean speedups of $1.11\times$, $1.23\times$, and $1.36\times$ over dense MLPs at 10%, 20%, and 30% target MLP projection FLOP savings, respectively. PSSE offers a principled path toward both probability-mass-controlled approximation and more efficient inference in pretrained language models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Victor O. K. Li, Yang Han, Jacqueline C. K. Lam
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
