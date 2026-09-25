---
title: "TrafficFab: An Autonomic Edge-Cloud Testbed Fabric forAI-Driven Traffic Management"
description: "Traffic management in emerging megacities requires real-time analytics over thousands of CCTV video streams under latency, bandwidth, compute and energy constraints."
---

**评分：38/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.29223) · [PDF](https://arxiv.org/pdf/2609.29223)

## 一句话摘要

Traffic management in emerging megacities requires real-time analytics over thousands of CCTV video streams under latency, bandwidth, compute and energy constraints.

## 为什么值得关注

待编辑增强。

## 摘要原文

Traffic management in emerging megacities requires real-time analytics over thousands of CCTV video streams under latency, bandwidth, compute and energy constraints. We present TrafficFab, an autonomic edge--cloud testbed for AI-driven traffic management, designed to validate a representative slice of a megacity deployment. TrafficFab combines RTSP stream emulation, heterogeneous edge inference using DNNs, cloud-based nowcasting and forecasting using Spatio-Temporal Graph Neural Network (ST-GNN), and continual model adaptation through foundation-model (FM)-assisted Federated Learning (FL). Its autonomic control enables fine-grained scale-out/in of edge inference through energy- and migration-aware scheduling, elastic scale-up/down of GNN forecasting on public clouds, and periodic adaptation of the DNN on edge accelerators and private cloud, without centralized video collection. We evaluate TrafficFab on a Bangalore-city inspired deployment, spanning Raspberry Pis, Jetson accelerators, GPU fogs, private cloud servers, and cloud VMs, sustaining real-time analytics for $\approx 400$ live camera streams (10% of Bangalore) and analytically characterize larger setups. The results demonstrate that TrafficFab offers a practical validation-scale platform for closed-loop traffic analytics, short-term operational decision support, and longer-horizon planning analyses in megacity scales.

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

- taxonomy keywords: edge inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mayank Arya, Pranjal Naman, Priyanshu Pansari, Roopkatha Banerjee, Daksh Mehta, Manjil Nepal, Akash Sharma, Yogesh Simmhan
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
