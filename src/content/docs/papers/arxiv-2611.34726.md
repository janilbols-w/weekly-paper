---
title: "Hierarchical Graph Metanetworks"
description: "The emerging field of weight space learning has demonstrated the potential to enable metanetworks, i.e."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.34726) · [PDF](https://arxiv.org/pdf/2611.34726)

## 一句话摘要

The emerging field of weight space learning has demonstrated the potential to enable metanetworks, i.e.

## 为什么值得关注

待编辑增强。

## 摘要原文

The emerging field of weight space learning has demonstrated the potential to enable metanetworks, i.e. models that process neural network (NN) data, to support several steps of the machine learning lifecycle, from model optimisation to evaluation and adaptation. However, this potential has yet to materialise beyond small-scale MLPs or CNNs: most current models, including message-passing based graph metanetworks (GMNs), operate exclusively at the finest level of granularity, processing every neuron and weight of the input model. Their cost therefore scales with the number of parameters. Yet NNs are inherently organised hierarchically, with neurons forming layers and layers forming blocks and modules. Additionally, several of their properties, such as Lipschitz upper bounds and generalisation measures, are compositions of layer- and block-level quantities. To incorporate this inductive bias, we introduce Hierarchical Graph Metanetworks (H-GMNs), which leverage the input architecture's hierarchy to coarsen and refine the graph using permutation-symmetry-preserving pooling and un-pooling layers. Further, we extend H-GMNs to Transformers by introducing a graph construction that preserves permutation symmetries and enables multi-level pooling. Our evaluation includes new ResNet-18, ViT and varying ViT model zoos of up to 86M parameters, on tasks spanning model evaluation (an analytic Lipschitz bound proxy, generalisation and robustness prediction), testing (backdoor detection) and editing (pruning). Experimental results show that, compared to non-equivariant alternatives and flat GMNs, H-GMNs are markedly more sample-efficient, and their cost remains nearly constant as metanetwork depth grows, allowing deeper and more expressive processing where flat GMNs run out of memory, without compromising accuracy, which in certain cases considerably improves.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ioannis Kalogeropoulos, Giorgos Bouritsas, Yannis Panagakis
- 发布：2026-11-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
