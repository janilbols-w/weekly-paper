---
title: "Towards Fast and Disentangled Counterfactuals for Visual Foundation Models"
description: "Foundation models remain vulnerable to spurious correlations and ``Clever Hans'' strategies."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.00895) · [PDF](https://arxiv.org/pdf/2610.00895)

## 一句话摘要

Foundation models remain vulnerable to spurious correlations and ``Clever Hans'' strategies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Foundation models remain vulnerable to spurious correlations and ``Clever Hans'' strategies. Explainable machine learning can find and remove such strategies for classifiers without metadata. For foundation models, no such option exists yet. We propose Disentangled Diffusion Autoencoders (DiDAE). DiDAE wraps a frozen foundation model in a conditional diffusion decoder. A counterfactual is one closed-form edit along a direction of a disentangled dictionary, followed by decoding. The dictionary can be supervised (Procrustes) or unsupervised (Singular Value Decomposition, Sparse Autoencoders). No gradients are needed, so DiDAE is up to 2000 times faster than the state of the art. We evaluate on six datasets, two synthetic and four real-world. In a desiderata-driven benchmark on three of them, its counterfactuals are on par with or better than the state of the art, and they repair downstream classifiers through Counterfactual Knowledge Distillation (CFKD), where they beat metadata-based correction. The same machinery can rank a pretrained dictionary against a trained classifier. It returns the few directions the classifier actually reads, each causally verified by a counterfactual that flips the decision, and repairs the classifier along those a teacher marks spurious. The workflow is plug-and-play in our open-source Peal library we publish alongside the paper. With a public dictionary and a pretrained decoder, all that remains is a cheap linear distillation of the classifier and its own fine-tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Sidney Bender, Benedikt Kunz, Ahmed Zeid, Shinichi Nakajima, Klaus-Robert M\"uller, Marco Morik
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
