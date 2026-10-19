---
title: "Accelerated Execution of Bayesian Neural Networks using a Single Probabilistic Forward Pass and Code Generation"
description: "Machine learning models perform well across domains such as diagnostics, weather forecasting, NLP, and autonomous driving, but their limited uncertainty handling restricts use in safety-critical settings."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2511.23440) · [PDF](https://arxiv.org/pdf/2511.23440)

## 一句话摘要

Machine learning models perform well across domains such as diagnostics, weather forecasting, NLP, and autonomous driving, but their limited uncertainty handling restricts use in safety-critical settings.

## 为什么值得关注

待编辑增强。

## 摘要原文

Machine learning models perform well across domains such as diagnostics, weather forecasting, NLP, and autonomous driving, but their limited uncertainty handling restricts use in safety-critical settings. Traditional neural networks often fail to detect out-of-domain (OOD) data and may output confident yet incorrect predictions. Bayesian neural networks (BNNs) address this by providing probabilistic estimates, but incur high computational cost because predictions require sampling weight distributions and multiple forward passes. The Probabilistic Forward Pass (PFP) offers a highly efficient approximation to Stochastic Variational Inference (SVI) by assuming Gaussian-distributed weights and activations, enabling fully analytic uncertainty propagation and replacing sampling with a single deterministic forward pass. We present an end-to-end pipeline for training, compiling, optimizing, and deploying PFP-based BNNs on embedded ARM CPUs. Using the TVM deep learning compiler, we implement a dedicated library of Gaussian-propagating operators for multilayer perceptrons and convolutional neural networks, combined with manual and automated tuning strategies. Ablation studies show that PFP consistently outperforms SVI in computational efficiency, achieving speedups of up to 4200x for small mini-batches. PFP-BNNs match SVI-BNNs on Dirty-MNIST in accuracy, uncertainty estimation, and OOD detection while greatly reducing compute cost. These results highlight the potential of combining Bayesian approximations with code generation to enable efficient BNN deployment on resource-constrained systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Bernhard Klein, Falk Selker, Hendrik Borras, Sophie Steger, Franz Pernkopf, Holger Fr\"oning
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
