---
title: "Faults That Fortify: CNN Adversarial Robustness via GPU Undervolting"
description: "Convolutional Neural Networks (CNNs) face a dual challenge: vulnerability to adversarial attacks and prohibitive training cost."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.20572) · [PDF](https://arxiv.org/pdf/2608.20572)

## 一句话摘要

Convolutional Neural Networks (CNNs) face a dual challenge: vulnerability to adversarial attacks and prohibitive training cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Convolutional Neural Networks (CNNs) face a dual challenge: vulnerability to adversarial attacks and prohibitive training cost. Adversarial training is effective but expensive, a burden that grows as learning shifts to the energy-constrained edge. This paper addresses both through GPU undervolting during training. Reducing supply voltage introduces stochastic perturbations that act as implicit regularization, improving robustness while lowering power. We characterize undervolting-induced faults at the bit level, then train LeNet, VGG-6, and MobileNetV3 on MNIST and CIFAR-10 under two training regimes, standard and adversarial, each at nominal and undervolted voltage, and evaluate all models against adversarial attacks. In both regimes, the undervolted model consistently achieves higher adversarial accuracy than its nominal-voltage counterpart, showing that hardware-induced faults strengthen even adversarial training. Because dynamic power scales quadratically with supply voltage, these robustness gains arrive with substantial energy savings. GPU undervolting is therefore a readily deployable hardware-level defense requiring no algorithmic change, and opens a promising direction in which robustness and energy efficiency move together.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Behnam Omidi, Ahmad Tahmasivand, Husam Alsyouri, Saba Al-Sayouri, Chongzhou Fang, Ihsen Alouani, Khaled N. Khasawneh
- 发布：2026-08-24；更新：2026-08-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
