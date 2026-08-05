---
title: "Constrained Co-Design for Photonic Bayesian Neural Networks"
description: "Classical neural networks frequently produce overconfident predictions on ambiguous or out-of-distribution (OOD) data, a liability that grows with each AI system deployed in safety-critical real-world scenarios."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.02229) · [PDF](https://arxiv.org/pdf/2608.02229)

## 一句话摘要

Classical neural networks frequently produce overconfident predictions on ambiguous or out-of-distribution (OOD) data, a liability that grows with each AI system deployed in safety-critical real-world scenarios.

## 为什么值得关注

待编辑增强。

## 摘要原文

Classical neural networks frequently produce overconfident predictions on ambiguous or out-of-distribution (OOD) data, a liability that grows with each AI system deployed in safety-critical real-world scenarios. Bayesian neural networks (BNNs) provide a principled framework for uncertainty-aware prediction by replacing deterministic parameters with probability distributions, but repeated sampling increases latency, memory traffic, and energy consumption. Photonic probabilistic computing offers a promising alternative by exploiting intrinsic optical stochasticity for fast and parallel sampling. However, photonic BNNs are not ideal samplers: analog constraints on quantization, programming error, dynamic range, and representable mean and variance restrict the variational families that can be implemented in hardware. In this work, we study which hardware-imposed constraints limit scalable photonic BNN inference, how these constraints can be represented, and which ranges can be tolerated by photonic BNNs beyond small proof-of-concept networks. We formulate photonic BNN inference as constrained stochastic variational inference and perform a systematic ablation study over stochasticity location, stochasticity modality, quantization, programming error, and mean/variance bounds. From these results, we derive concrete co-design guidelines that distinguish hardware constraints that can be compensated by training from those requiring hardware or architecture intervention. We validate these guidelines under coupled, hardware-realistic constraints on Dirty-MNIST, CIFAR-10, and CINIC-10, using Fashion-MNIST and SVHN as OOD benchmarks, showing that hardware-aware training recovers predictive performance and uncertainty quality whenever the required variational family remains representable, whereas violations of representational limits require targeted hardware modifications.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hendrik Borras, Xiao Wang, Bernhard Klein, Robin Janssen, Frank Br\"uckerhoff-Pl\"uckelmann, Wolfram Pernice, Holger Fr\"oning
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
