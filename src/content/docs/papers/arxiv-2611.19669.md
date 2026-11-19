---
title: "IA-MoE: An Intensity-Aware Mixture of Experts for DNN Inference"
description: "In edge-cloud collaborative inference, the layers of a deep neural network (DNN) are placed on edge and cloud virtual machines (VMs) for every request, while the edge load and the cross-cloud bandwidth change over time."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2611.19669) · [PDF](https://arxiv.org/pdf/2611.19669)

## 一句话摘要

In edge-cloud collaborative inference, the layers of a deep neural network (DNN) are placed on edge and cloud virtual machines (VMs) for every request, while the edge load and the cross-cloud bandwidth change over time.

## 为什么值得关注

待编辑增强。

## 摘要原文

In edge-cloud collaborative inference, the layers of a deep neural network (DNN) are placed on edge and cloud virtual machines (VMs) for every request, while the edge load and the cross-cloud bandwidth change over time. We propose IA-MoE, an intensity-aware Mixture of Experts (MoE) framework that scores each layer-VM pair by end-to-end delay and energy and places the layers one at a time on the best-scoring VM. Such greedy placement is myopic when trained on per-layer labels: offloading to the cloud slows the first offloaded layer while the gain appears only in later layers, so the policy keeps too many requests at the edge. Training on the remaining request time after each decision removes this myopia and reduces the mean delay by 12-56% on congested workloads. In CloudSimSDN simulations with three DNNs and two public request traces, IA-MoE has the lowest mean delay of all compared methods on congested VGG16 workloads, across cross-cloud bandwidths of 150-600 Mbps, fluctuating bandwidth and saturated edge servers. A random forest trained on the same label is 5-27% slower, and only a heuristic that sends whole requests to the cloud uses less energy, at up to 20 times the delay. When the edge is lightly loaded, offloading does not pay and simple heuristics perform as well. IA-MoE also beats a Double Deep Q-Network (DQN) agent with the same features in all 19 tested settings, with a mean delay lower by a factor of 1.3 to 10.5, and trains in minutes instead of hours.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Meiyan Zeng, Sasu Tarkoma, Xiaoli Liu
- 发布：2026-11-17；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
