---
title: "Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent"
description: "We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.18397) · [PDF](https://arxiv.org/pdf/2611.18397)

## 一句话摘要

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. We first continue pre-training on a dataset constructed from tens of thousands of hours of device-level keyboard and mouse interaction. These trajectories span simulated games and embodied environments, allowing the model to learn environmental dynamics across both physical and virtual domains. Sparse-thinking instruction tuning then substantially reduces redundant computation while preserving the reasoning needed for complex decisions. We train the policy for long-horizon interaction with a stable multi-turn reinforcement learning method that addresses finite context windows, accumulated rollout errors, and sparse rewards. For real-time interaction, a cloud-edge inference engine serves numerous simulated game environments concurrently, supports unbounded-context execution, and keeps online inference latency low. Across multiple challenging 3D open-world games, Gamer demonstrates solid generalization and operational efficiency comparable to skilled players. It also achieves competitive results on a range of conventional 2D game benchmarks. These results suggest that even repetitive keyboard and mouse trajectories can support substantial gains from scaling data and learning algorithms. Training on these trajectories helps Gamer learn complex skills more steadily in environments with both physical and digital properties. This approach offers a path toward generalist agents that can interact across digital and physical worlds.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine, online inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, Yufei Zhang, Renrong Hu, Yi Zhang, Guiyu Ma, Tianyu Fan, Longze Chen, Hao Sun, Jiaming Li, Jiaming Yang, Xiaohao Liu, Tao Tan, Minzheng Wang, Hangtian Jia, Shuai Yuan, Lvdi Wang, Xiao Liu, Chao Ma, Yuting Zou, Yinhe Zheng, Xiaobo Xia, Dawei Jiang, Shaoqing Ren
- 发布：2026-11-16；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
