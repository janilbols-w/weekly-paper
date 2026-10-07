---
title: "Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks"
description: "Spiking neural networks (SNNs) offer sparse and event-driven computation, making them attractive for energy-constrained reinforcement learning (RL) on edge devices."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2610.07808) · [PDF](https://arxiv.org/pdf/2610.07808)

## 一句话摘要

Spiking neural networks (SNNs) offer sparse and event-driven computation, making them attractive for energy-constrained reinforcement learning (RL) on edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking neural networks (SNNs) offer sparse and event-driven computation, making them attractive for energy-constrained reinforcement learning (RL) on edge devices. In value-based RL, deep spiking Q-networks (DSQNs) combine such efficiency with action-value estimation for decision making. However, existing DSQNs often require multiple simulation timesteps for competitive performance, increasing computational and energy costs, whereas reducing the timesteps can cause substantial performance degradation. We investigate this degradation from the perspective of Q-value estimation errors. By decomposing errors across actions into common-mode and differential-mode components, we find that low-timestep DSQNs suffer disproportionately from common-mode errors shared across action values, which are particularly detrimental to temporal-difference learning through bootstrapped targets. Based on this finding, we propose Common-Mode Compensation Deep Spiking Q-Network (CMC-DSQN), which uses an auxiliary ANN to compensate for common-mode errors in the SNN outputs. At inference, greedy action selection can be performed directly from the SNN outputs, allowing the auxiliary ANN to be completely removed and preserving the energy efficiency of SNNs. Extensive experiments on Atari and MiniAtar environments demonstrate substantial performance improvements under low-timestep settings. CMC-DSQN outperforms state-of-the-art DSQN baselines by nearly $20\%$ at $T=2$ and further surpasses the ANN baseline at $T=4$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zijie Xu, Bingrui Guo, Yiding Sun, Yiting Dong, Zhile Yang, Zhaofei Yu
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
