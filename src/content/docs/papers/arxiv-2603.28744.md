---
title: "Stop Probing, Start Coding: Why Linear Probes and Sparse Autoencoders Fail at Compositional Generalisation"
description: "The linear representation hypothesis states that neural network activations encode high-level concepts as linear mixtures."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2603.28744) · [PDF](https://arxiv.org/pdf/2603.28744)

## 一句话摘要

The linear representation hypothesis states that neural network activations encode high-level concepts as linear mixtures.

## 为什么值得关注

待编辑增强。

## 摘要原文

The linear representation hypothesis states that neural network activations encode high-level concepts as linear mixtures. However, under superposition, this encoding is a projection from a higher-dimensional concept space into a lower-dimensional activation space, and a linear decision boundary in the concept space need not remain linear after projection. In this setting, classical sparse coding methods with per-sample iterative inference leverage compressed sensing guarantees to recover latent factors. Sparse autoencoders (SAEs), on the other hand, amortise sparse inference into a fixed encoder, introducing a systematic gap. We show this amortisation gap persists across training set sizes, latent dimensions, and sparsity levels, causing SAEs to fail under out-of-distribution (OOD) compositional shifts. Through controlled experiments that decompose the failure, we identify dictionary learning as the limiting factor (not the inference procedure): SAE-learned dictionaries point in substantially wrong directions, and replacing the encoder with per-sample FISTA on the same dictionary does not close the gap. An oracle baseline proves the problem is solvable with a good dictionary at all scales tested. Our results, including experiments with real LLM activations (Pythia-70M, Gemma-2-2B) reframe the SAE failure as a dictionary learning challenge, not an inference problem, and point to scalable dictionary learning as the key open problem for sparse inference under superposition.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparse inference, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vit\'oria Barin-Pacela, Shruti Joshi, Isabela Camacho, Simon Lacoste-Julien, David Klindt
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
