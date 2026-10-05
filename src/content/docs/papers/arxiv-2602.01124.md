---
title: "ChronoSpike: An Adaptive Spiking Graph Neural Network for Dynamic Graphs"
description: "Dynamic graph representation learning requires capturing both structural relations and temporal evolution, yet existing approaches face a core trade-off: attention-based methods offer expressiveness at O(T^2) complexity, while recurrent architectures suffer from gradient pathologies and dense state storage."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.01124) · [PDF](https://arxiv.org/pdf/2602.01124)

## 一句话摘要

Dynamic graph representation learning requires capturing both structural relations and temporal evolution, yet existing approaches face a core trade-off: attention-based methods offer expressiveness at O(T^2) complexity, while recurrent architectures suffer from gradient pathologies and dense state storage.

## 为什么值得关注

待编辑增强。

## 摘要原文

Dynamic graph representation learning requires capturing both structural relations and temporal evolution, yet existing approaches face a core trade-off: attention-based methods offer expressiveness at O(T^2) complexity, while recurrent architectures suffer from gradient pathologies and dense state storage. Spiking neural networks provide event-driven efficiency but are constrained by sequential propagation, binary information loss, and local aggregation that lacks global context. We propose ChronoSpike, an adaptive spiking graph neural network that integrates learnable LIF neurons with per-channel membrane dynamics, multi-head spatially-attentive aggregation over continuous features, and a lightweight Transformer temporal encoder. This design enables fine-grained local modeling and long-range dependency capture with O(T.d) activation/state memory and an additional O(T^2) per-node attention term that remains small for the horizons evaluated here. ChronoSpike outperforms twelve state-of-the-art baselines on three large benchmarks by 2.0%~Macro-F1 and 2.4%~Micro-F1 on average while achieving 3-10 times faster training than recurrent methods with a constant 105K-parameter budget independent of graph size. We provide theoretical guarantees for membrane potential boundedness, gradient flow stability under contraction factor \r{ho}<1, and BIBO stability; interpretability analyses reveal heterogeneous temporal receptive fields and a learned primacy effect with 83-88% sparsity. Our code is publicly available at: https://github.com/Abrar2652/ChronoSpike

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Md Abrar Jahin, Taufikur Rahman Fuad, Jay Pujara, Craig Knoblock
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Abrar2652/ChronoSpike](https://github.com/Abrar2652/ChronoSpike)
- 阅读深度：metadata
