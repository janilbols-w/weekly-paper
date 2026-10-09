---
title: "Adaptive Multi-Discriminator WGAN Framework for Resource-Constrained Internet of Vehicles Using Reinforcement Learning and Game Theory"
description: "Managing machine learning workloads as a network service introduces a resource-orchestration problem distinct from conventional model training; which nodes should be allocated to a task, how communication and computation budgets should be divided among them, and how service quality should be sustained as connectivity and node availability change with mobilit"
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.10926) · [PDF](https://arxiv.org/pdf/2610.10926)

## 一句话摘要

Managing machine learning workloads as a network service introduces a resource-orchestration problem distinct from conventional model training; which nodes should be allocated to a task, how communication and computation budgets should be divided among them, and how service quality should be sustained as connectivity and node availability change with mobilit

## 为什么值得关注

待编辑增强。

## 摘要原文

Managing machine learning workloads as a network service introduces a resource-orchestration problem distinct from conventional model training; which nodes should be allocated to a task, how communication and computation budgets should be divided among them, and how service quality should be sustained as connectivity and node availability change with mobility. Deploying Generative Adversarial Networks (GANs) in Internet of Vehicles (IoV) environments is a demanding instance of this problem; resource constraints, dynamic network topologies, and competing optimization objectives mean that traditional GAN architectures cannot simultaneously achieve high accuracy, efficient resource use, low delay, and low communication overhead. This paper introduces an adaptive multi-discriminator Wasserstein GAN (MD-WGAN) framework that integrates reinforcement learning with game-theoretic coordination to address these challenges jointly. In our framework, roadside units host generators paired with Deep Q-Network (DQN) agents that select discriminator subsets and manage distributed training across mobile vehicular nodes, while a game-theoretic coordination step allocates training epochs between generators and discriminators. A unified optimization objective ties adversarial learning quality to resource efficiency, communication overhead, and latency under vehicular constraints, allowing the framework to continuously adapt its training behavior as network conditions change. Evaluation on real-world NGSIM trajectory data shows that the framework attains prediction accuracy comparable to state-of-the-art GAN baselines - the lowest RMSE (1.029) and MAE (0.894) among all evaluated methods - while markedly improving resource efficiency: average CPU utilization is reduced by roughly 28% and mean memory usage by roughly 6%, at competitive communication overhead and latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed training
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Farhoud Jafari Kaleibar, Amr M. Zaki, Marin Litoiu
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
