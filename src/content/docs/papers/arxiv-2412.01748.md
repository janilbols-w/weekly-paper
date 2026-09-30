---
title: "Classifier-pruned Bayesian optimization for particle accelerator tuning: Exploring temporally structured manifold of 6D beam phase space"
description: "Complex dynamical systems, such as particle accelerators, require tuning over high-dimensional, nonlinear state and parameter spaces while experimental measurements and high-fidelity simulations can be expensive."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2412.01748) · [PDF](https://arxiv.org/pdf/2412.01748)

## 一句话摘要

Complex dynamical systems, such as particle accelerators, require tuning over high-dimensional, nonlinear state and parameter spaces while experimental measurements and high-fidelity simulations can be expensive.

## 为什么值得关注

待编辑增强。

## 摘要原文

Complex dynamical systems, such as particle accelerators, require tuning over high-dimensional, nonlinear state and parameter spaces while experimental measurements and high-fidelity simulations can be expensive. Learned latent representations provide a compact domain for such optimization, but poorly supported regions of the learned manifold may decode into unrealistic physical states and yield deceptively favorable objectives. To address this challenge, we propose the Classifier-pruned Bayesian Optimization-based Latent-space Tuner (CBOL-Tuner), which performs Bayesian optimization over a temporally structured latent representation of 6D beam phase-space dynamics. The CBOL-Tuner integrates a conditional variational autoencoder for latent space representation, a long short-term memory network for temporal dynamics, a lightweight neural network for parameter estimation, and a classifier-pruned Bayesian optimizer to adaptively search and filter the latent space for optimal solutions. This framework enables feasibility-aware exploration of learned scientific representations for accelerator tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mahindra Rautela, Alan Williams, Alexander Scheinker
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
