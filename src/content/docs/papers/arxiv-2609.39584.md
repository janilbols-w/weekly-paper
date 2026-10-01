---
title: "Cybersecurity in Edge Computing: A Trust-Aware Federated Hybrid Intrusion Detection Framework"
description: "Edge computing has emerged as a critical computing paradigm in modern distributed systems by migrating data processing closer to end users and Internet of Things (IoT) devices."
---

**评分：46/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2609.39584) · [PDF](https://arxiv.org/pdf/2609.39584)

## 一句话摘要

Edge computing has emerged as a critical computing paradigm in modern distributed systems by migrating data processing closer to end users and Internet of Things (IoT) devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge computing has emerged as a critical computing paradigm in modern distributed systems by migrating data processing closer to end users and Internet of Things (IoT) devices. While this paradigm decentralizes processes, minimizes latency, and reduces backhaul bandwidth congestion, it exponentially enlarges the cyberattack surface. Heterogeneous, resource-constrained edge devices deployed across unmanaged administrative domains present highly vulnerable targets. To address these vulnerabilities without compromising global data privacy regulations, this paper proposes a novel Trust-Aware Federated Hybrid Intrusion Detection Framework (TA-FHIDF). The proposed framework integrates an Autoencoder, a 1D Convolutional Neural Network (1D-CNN), and a Bidirectional Long Short-Term Memory (BiLSTM) model into a unified, localized deep learning engine capable of autonomous spatial and temporal feature extraction. Model training is performed collaboratively via federated learning, ensuring raw network telemetry remains isolated at local gateways. Furthermore, to defend against adversarial model poisoning attacks, we introduce a robust server-side trust-aware aggregation mechanism that evaluates client reliability using a cosine similarity metric before global model integration. Empirical evaluations across multi-vector benchmark datasets (UNSW-NB15, CICIDS2017, and Edge-IIoTset) demonstrate the framework's superior detection accuracy, rapid convergence, and high Byzantine fault tolerance under adversarial attack scenarios.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fault tolerance
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zawad Yalmie Sazid, Robert Abbas
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
