---
title: "Muon Sublates the Edge of Stability in LLM Pretraining: What Persists and What Changes"
description: "Muon is increasingly used for language-model pretraining, yet its large-step dynamics are not captured by the classical edge-of-stability (EoS) picture of gradient descent (GD)."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.34915) · [PDF](https://arxiv.org/pdf/2609.34915)

## 一句话摘要

Muon is increasingly used for language-model pretraining, yet its large-step dynamics are not captured by the classical edge-of-stability (EoS) picture of gradient descent (GD).

## 为什么值得关注

待编辑增强。

## 摘要原文

Muon is increasingly used for language-model pretraining, yet its large-step dynamics are not captured by the classical edge-of-stability (EoS) picture of gradient descent (GD). We study stochastic (no-momentum) Muon through theoretical analysis, controlled networks, and language models from 22M to 1B parameters, distinguishing three diagnostics: generalized sharpness, loss balance, and update alignment. We theoretically and empirically demonstrate that loss balance differs from its generalized sharpness and cannot determine update alignment across various learning rates in 130M pre-training as well as 1B runs. Besides, our experiments also show that increasing the batch size encourages update alignment towards to total reversal. Furthermore, checkpoint interventions in the 22M and 130M models show that increasing the learning rate can initially raise the loss but a lower validation loss at the end of the prescribed warmup-stable-decay continuation. These results support a split EoS picture: generalized-sharpness saturation persists in the measured runs, but loss balance and update geometry require separate characterization, allowing for learning-rate schedules design. The source code for reproducing the experiments can be found in https://github.com/cyzebra/Muon-Sublates-the-Edge-of-Stability-in-LLM-Pretraining.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yanzhe Chen, Qifang Zhao, Xiaoxiao Xu, Fanghui Liu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/cyzebra/Muon-Sublates-the-Edge-of-Stability-in-LLM-Pretraining](https://github.com/cyzebra/Muon-Sublates-the-Edge-of-Stability-in-LLM-Pretraining)
- 阅读深度：metadata
