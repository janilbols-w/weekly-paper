---
title: "Understanding Layer Patching in Model Size Interpolation"
description: "Layer patching is a key technique for model size interpolation in large language models (LLMs), in which a subset of a distilled student model's layers is replaced with corresponding teacher-model layers to construct intermediate-sized models without additional training."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.08170) · [PDF](https://arxiv.org/pdf/2607.08170)

## 一句话摘要

Layer patching is a key technique for model size interpolation in large language models (LLMs), in which a subset of a distilled student model's layers is replaced with corresponding teacher-model layers to construct intermediate-sized models without additional training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Layer patching is a key technique for model size interpolation in large language models (LLMs), in which a subset of a distilled student model's layers is replaced with corresponding teacher-model layers to construct intermediate-sized models without additional training. Prior work largely ignores the order in which layers are patched, which we show can dramatically affect the performance and reliability of the resulting models. In this work, we study the role of layer patching in model size interpolation. We cast finding the optimal layer subset for each model size as an optimization problem and prove it can be viewed as a shortest-path problem in a certain acyclic graph. In experiments, we show that patching strongly shapes interpolation behavior, with effects that vary substantially across model families. We find that simple sequential strategies---patching either from the first layer to the last or from the last to the first---often achieve surprisingly strong performance in practice. We further introduce KLPatch, a greedy patching algorithm based on KL divergence, which often improves over last-to-first patching and approximately solves the optimization problem. Together, our results provide a principled understanding of how layer patching affects model size interpolation and offer practical guidance for constructing near-optimal interpolated models. The code and models are available at https://github.com/dcml-lab/boomerang-distillation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Sara Kangaslahti, Jonathan Geuter, Nihal V. Nayak, Marco Fumero, Francesco Locatello, David Alvarez-Melis
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/dcml-lab/boomerang-distillation](https://github.com/dcml-lab/boomerang-distillation)
- 阅读深度：metadata
