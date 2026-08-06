---
title: "Understanding Fault Tolerance of Adversarially Robust Pruned Models"
description: "Deep neural networks (DNNs) deployed on resource-constrained neuromorphic hardware face three concurrent challenges: the need for model compression through pruning, vulnerability to adversarial input perturbations, and susceptibility to hardware-induced weight faults such as stuck-at-zero errors."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2608.04173) · [PDF](https://arxiv.org/pdf/2608.04173)

## 一句话摘要

Deep neural networks (DNNs) deployed on resource-constrained neuromorphic hardware face three concurrent challenges: the need for model compression through pruning, vulnerability to adversarial input perturbations, and susceptibility to hardware-induced weight faults such as stuck-at-zero errors.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep neural networks (DNNs) deployed on resource-constrained neuromorphic hardware face three concurrent challenges: the need for model compression through pruning, vulnerability to adversarial input perturbations, and susceptibility to hardware-induced weight faults such as stuck-at-zero errors. While each of these factors has been studied in isolation, their combined effects on model reliability have received little attention. This paper presents an empirical investigation of how pruning, adversarial training, and hardware fault injection interact to affect the robustness of convolutional neural networks. Using a compact three-layer CNN trained on MNIST, we conduct three experiments: (1) comparing the fault tolerance of naturally and adversarially trained models under simultaneous hardware faults and adversarial attacks, (2) evaluating how pruning affects adversarial robustness, and (3) characterizing the joint accuracy surface across fault rates, adversarial perturbation magnitudes, and pruning levels. Our results show that adversarial training improves robustness against input perturbations but increases sensitivity to stuck-at-zero weight faults. Contrary to intuition, pruning did not significantly increase fault sensitivity, and varying the pruning level had little effect across fault rates and attack strengths. These results highlight the need to jointly consider adversarial robustness and hardware reliability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Manali Dangarikar, Cory Merkel
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
