---
title: "IA-MoE: An Intensity-Aware Mixture of Experts for DNN Inference"
description: "IA-MoE 面向边云协同 DNN 推理，按端到端时延与能耗为每个层—虚拟机组合评分并逐层放置；以“剩余请求时间”作为训练目标，缓解只看单层收益导致的短视决策。"
---

**评分：56/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2611.19669) · [PDF](https://arxiv.org/pdf/2611.19669)

## 一句话摘要

IA-MoE 面向边云协同 DNN 推理，按端到端时延与能耗为每个层—虚拟机组合评分并逐层放置；以“剩余请求时间”作为训练目标，缓解只看单层收益导致的短视决策。

## 为什么值得关注

它展示了在边缘负载和跨云带宽波动时，调度目标的设计会显著影响卸载策略，可为动态边云推理编排提供一种低训练成本的决策思路。

## 摘要原文

In edge-cloud collaborative inference, the layers of a deep neural network (DNN) are placed on edge and cloud virtual machines (VMs) for every request, while the edge load and the cross-cloud bandwidth change over time. We propose IA-MoE, an intensity-aware Mixture of Experts (MoE) framework that scores each layer-VM pair by end-to-end delay and energy and places the layers one at a time on the best-scoring VM. Such greedy placement is myopic when trained on per-layer labels: offloading to the cloud slows the first offloaded layer while the gain appears only in later layers, so the policy keeps too many requests at the edge. Training on the remaining request time after each decision removes this myopia and reduces the mean delay by 12-56% on congested workloads. In CloudSimSDN simulations with three DNNs and two public request traces, IA-MoE has the lowest mean delay of all compared methods on congested VGG16 workloads, across cross-cloud bandwidths of 150-600 Mbps, fluctuating bandwidth and saturated edge servers. A random forest trained on the same label is 5-27% slower, and only a heuristic that sends whole requests to the cloud uses less energy, at up to 20 times the delay. When the edge is lightly loaded, offloading does not pay and simple heuristics perform as well. IA-MoE also beats a Double Deep Q-Network (DQN) agent with the same features in all 19 tested settings, with a mean delay lower by a factor of 1.3 to 10.5, and trains in minutes instead of hours.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 6 |

## 证据与限制

- taxonomy keywords: mixture of experts
- quantitative claim detected
- no code link detected in metadata
- 限制：证据来自 CloudSimSDN 仿真、3 个 DNN 和 2 条请求轨迹，并非真实 LLM 服务部署；轻载时该方法相对简单启发式没有优势，泛化范围仍有限。

## 元数据

- 作者：Meiyan Zeng, Sasu Tarkoma, Xiaoli Liu
- 发布：2026-11-14；更新：2026-11-18
- 来源：arXiv RSS；Venue：Proceedings of the 2025 IEEE International Conference on Networking, Sensing and Control (ICNSC), 2025
- 代码：未发现
- 阅读深度：abstract
