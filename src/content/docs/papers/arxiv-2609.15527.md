---
title: "Beyond Noise: Understanding and Overcoming Temperature Effects in Analog DNN Inference"
description: "The energy efficiency of analog computing makes it one of the most promising candidates for deploying resource-intensive machine learning workloads on constrained platforms such as mobile and embedded devices."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2609.15527) · [PDF](https://arxiv.org/pdf/2609.15527)

## 一句话摘要

The energy efficiency of analog computing makes it one of the most promising candidates for deploying resource-intensive machine learning workloads on constrained platforms such as mobile and embedded devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

The energy efficiency of analog computing makes it one of the most promising candidates for deploying resource-intensive machine learning workloads on constrained platforms such as mobile and embedded devices. However, analog accelerators are inherently susceptible to noise and non-idealities arising from physical component variations, whose behavior is further sensitive to environmental factors. These effects can significantly degrade inference accuracy. In this work, we conduct a comprehensive experimental study on a representative example of analog hardware to investigate the impact of temperature. We first characterize the behavior of stochastic and systematic non-idealities across a range of operating temperatures. Following this, we compare a set of simulation-based and hardware-based mitigation strategies aimed at improving robustness against temperature-induced performance degradation. Our results suggest that temperature-induced degradation is driven primarily by systematic non-idealities rather than stochastic noise alone. Noise-aware training improves robustness, while hardware-in-the-loop training and temperature-aware calibration provide the strongest accuracy retention across varying thermal conditions.

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

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Niklas Summ, Xiao Wang, Hendrik Borras, Bernhard Klein, Holger Fröning
- 发布：2026-09-14；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
