---
title: "Network Contention State Aware Dynamic Optimizer for Accelerator Collective Communication Libraries"
description: "Collective Communication Libraries (CCL) are critical for large-scale distributed AI/ML training, yet their configurations are determined by static heuristics that do not account for real-time network conditions."
---

**评分：46/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.10984) · [PDF](https://arxiv.org/pdf/2611.10984)

## 一句话摘要

Collective Communication Libraries (CCL) are critical for large-scale distributed AI/ML training, yet their configurations are determined by static heuristics that do not account for real-time network conditions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Collective Communication Libraries (CCL) are critical for large-scale distributed AI/ML training, yet their configurations are determined by static heuristics that do not account for real-time network conditions. Our empirical study shows that these heuristics perform near-optimally in contention-free environments, but degrade substantially under background traffic. To address this, we present a cooperative multi-agent run-time optimizer for accelerator collective communication. Our approach employs a two-agent architecture: (i) detector- a Long Short Term Memory(LSTM) recurring neural network fed classifier head with a sequential probability ratio test that distinguishes sustained contention from transient spikes; and (ii) selector- a configuration selector built on a Dueling Double DQN (D3QN) with Conservative Q-Learning that adapts configuration parameters in response. We implemented this dynamic tuner over NCCL, a widely used CCL developed by NVIDIA. When evaluated on Chameleon Cloud's isolated bare-metal cluster, this dynamic tuning approach reduces AllReduce latency by 36% over NCCL and 32% over a fully converged AutoCCL. We further evaluated it across six real AI workloads spanning convolutional networks, transformers, and recommendation architectures. Our multi-agent tuner approach delivers up to 65% speedups on Delta cluster with NVIDIA A100 GPUs and Slingshot-11 fabric internode connectivity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rajat Bisht (Tennessee Technological University), Tevfik Kosar (University at Buffalo), Anthony Skjellum (Tennessee Technological University), Gene Cooperman (Northeastern University), MD S Q Zulkar Nine (Arkansas Tech University)
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
