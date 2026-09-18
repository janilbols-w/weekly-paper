---
title: "Exploring Sparsity and Smoothness of Arbitrary Lp Norms in Adversarial Attacks"
description: "Adversarial attacks against deep neural networks are commonly constructed under $\\ell_p$ norm constraints, most often using $p=1$, $p=2$ or $p=\\infty$, and potentially regularized for specific demands such as sparsity or smoothness."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2602.06578) · [PDF](https://arxiv.org/pdf/2602.06578)

## 一句话摘要

Adversarial attacks against deep neural networks are commonly constructed under $\ell_p$ norm constraints, most often using $p=1$, $p=2$ or $p=\infty$, and potentially regularized for specific demands such as sparsity or smoothness.

## 为什么值得关注

待编辑增强。

## 摘要原文

Adversarial attacks against deep neural networks are commonly constructed under $\ell_p$ norm constraints, most often using $p=1$, $p=2$ or $p=\infty$, and potentially regularized for specific demands such as sparsity or smoothness. These choices are typically made without a systematic investigation of how the norm parameter $p$ influences the structural and perceptual properties of adversarial perturbations. In this work, we study how the choice of $p$ affects sparsity and smoothness of adversarial attacks generated under $\ell_p$ norm constraints for values of $p \in [1,2]$. To enable a quantitative analysis, we adopt two established sparsity measures from the literature and introduce three smoothness measures. In particular, we propose a general framework for deriving smoothness measures based on smoothing operations and additionally introduce a smoothness measure based on first-order Taylor approximations. Using these measures, we conduct a comprehensive empirical evaluation across multiple real-world image datasets and a diverse set of model architectures, including both convolutional and transformer-based networks. We show that the choice of $\ell_1$ or $\ell_2$ is suboptimal in most cases and the optimal $p$ value is dependent on the specific task. In our experiments, using $\ell_p$ norms with $p\in [1.3, 1.5]$ yields the best trade-off between sparse and smooth attacks. These findings highlight the importance of principled norm selection when designing and evaluating adversarial attacks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Christof Duhme, Florian Eilers, Xiaoyi Jiang
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
