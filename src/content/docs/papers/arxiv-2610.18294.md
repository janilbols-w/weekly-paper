---
title: "Which Optimizer Leaks Most? Optimizer Implicit Bias as a Training-Data Privacy Controller"
description: "Releasing a neural network checkpoint can leak information about its training data, and existing reconstruction results rely on gradient-descent training."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](http://arxiv.org/abs/2610.18294v1) · [PDF](https://arxiv.org/pdf/2610.18294v1)

## 一句话摘要

Releasing a neural network checkpoint can leak information about its training data, and existing reconstruction results rely on gradient-descent training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Releasing a neural network checkpoint can leak information about its training data, and existing reconstruction results rely on gradient-descent training. We ask whether the choice of optimizer affects the ability to recover the training data. Extending work connecting Karush--Kuhn--Tucker conditions to training-data reconstruction, we show that the implicit biases of popular optimizers (SGD, Adam, Muon) leave very different fingerprints of the training data. We argue that the key distinction is the \emph{weight-specificity} of these implicit biases, namely how much continuous information about the final weights the optimizer-dependent target of the stationarity conditions encodes. The limiting stationarity conditions for models trained with SGD and Muon retain enough weight-specific information to reconstruct training examples in practice. For Adam in the $\ell_\infty$ implicit-bias regime, the optimizer-dependent part of these conditions encodes only a discrete pattern of maximal coordinates and their signs, and at nondegenerate KKT points the conditions are too few to identify the training set to first order. Experiments on MNIST and CIFAR-10 support these claims: models trained with Muon can yield stronger reconstructions at much lower training cost than models trained with SGD, although this advantage depends on the training regime and architecture, and models trained with Adam appear consistently more resistant to the evaluated attacks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sagi Habani, Yehonathan Refael, Ofir Lindenbaum
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
