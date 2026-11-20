---
title: "OMNIS+: Semantic RAN Slicing and Quantization for Dynamic Split Neural Networks"
description: "Edge computing enables resource-constrained devices to execute machine learning (ML) applications via task offloading, with radio access network (RAN) slicing playing a crucial role in provisioning joint communication and computing resources."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.23977) · [PDF](https://arxiv.org/pdf/2611.23977)

## 一句话摘要

Edge computing enables resource-constrained devices to execute machine learning (ML) applications via task offloading, with radio access network (RAN) slicing playing a crucial role in provisioning joint communication and computing resources.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge computing enables resource-constrained devices to execute machine learning (ML) applications via task offloading, with radio access network (RAN) slicing playing a crucial role in provisioning joint communication and computing resources. However, existing RAN slicing frameworks rely on static computing models, limiting their ability to exploit dynamic semantic data representations enabled by modern neural architectures. To address this limitation, we propose OMNIS+, a semantic RAN slicing framework for multi-cell edge computing built upon a new generation of dynamic split neural models. OMNIS+ incorporates dynamic neural compression paired with adaptive quantization for task offloading, providing a versatile decision space across communication payload and compute dimensions. We leveraged a novel ``box'' quantization scheme that markedly enhances resilience to transmission bit errors across diverse compression rates. Considering partial system observability and distinct node objectives, we formulate two interdependent optimization problems: (i)~mobile devices (MDs) maximize inference accuracy under quality-of-service (QoS) and queue-stability constraints by jointly adapting dynamic split deep neural network (DNN) branches and cell association; and (ii)~each edge server (ES) allocates bandwidth, graphics processing unit (GPU) frequency, and modulation and coding scheme (MCS) to maximize the max--min inference accuracy among associated MDs under cell capacity limits. We solve these problems using a multi-agent distributed optimization framework, where MDs act as causal contextual multi-armed bandit (MAB) agents under backlog-aware Lyapunov control, while each ES executes resource allocation via block coordinate descent (BCD). Compared with state-of-the-art baselines, OMNIS+ reduces the QoS violation probability by up to 1.75 while achieving a better accuracy--violation trade-off.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Langtian Qin, Avishkar Dnyaneshwar Kawadgave, Ian Andrew Harshbarger, Leïla Nasraoui, Carla Fabiana Chiasserini, Marco Levorato
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
