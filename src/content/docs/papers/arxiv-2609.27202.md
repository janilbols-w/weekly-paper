---
title: "Reliable Federated TinyML Deployment for IoT Security"
description: "The growing deployment of Internet of Things (IoT) devices has increased the need for privacy-preserving intrusion detection systems that operate directly on resource-constrained hardware."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.27202) · [PDF](https://arxiv.org/pdf/2609.27202)

## 一句话摘要

The growing deployment of Internet of Things (IoT) devices has increased the need for privacy-preserving intrusion detection systems that operate directly on resource-constrained hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

The growing deployment of Internet of Things (IoT) devices has increased the need for privacy-preserving intrusion detection systems that operate directly on resource-constrained hardware. Federated Learning enables collaborative model training without sharing raw data, but conventional federated models are often too large and unstable for deployment on microcontroller-class devices. TinyML techniques enable compact neural networks but are typically designed for inference-only workloads. This work investigates combining Federated Learning with TinyML-based model compression for intrusion detection in IoT environments. We evaluate compression strategies including knowledge distillation, structured pruning, and quantization within a federated training pipeline. Preliminary results show that training stability plays a critical role in federated TinyML systems. In particular, server-coordinated cosine learning-rate scheduling improves Attack Recall from 46.7% to 93.85% while enabling substantial model compression and efficient edge deployment. These findings provide insights for designing lightweight and privacy preserving intrusion detection systems for IoT devices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation, pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Younsoo Park, Seokhyoen Bae, Shasi Kumar Ramachandran Prabhu, Suman Saha, Peilong Li
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
