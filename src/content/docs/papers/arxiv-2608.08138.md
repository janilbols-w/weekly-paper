---
title: "EFFEKT: Efficient Federated Knowledge Transfer to Foundation Models"
description: "Recent data protection laws have accelerated the adoption of Federated Learning (FL) for privacy-preserving decentralized training."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.08138) · [PDF](https://arxiv.org/pdf/2608.08138)

## 一句话摘要

Recent data protection laws have accelerated the adoption of Federated Learning (FL) for privacy-preserving decentralized training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent data protection laws have accelerated the adoption of Federated Learning (FL) for privacy-preserving decentralized training. Nevertheless, increasing model sizes impose substantial computational demands on client devices, limiting FL applicability in resource-constrained settings. We introduce a novel multi-domain federated learning framework in which lightweight client-side proxy models collaborate with a server-side Foundation Model (FM) to learn new concepts without sharing private data. Our approach, EFFEKT, enables efficient server-side training of domain-specific LoRA adapters while preserving feature-space alignment between the FM and proxy extractors via novel bi-directional cross-distillation strategies. Experiments on multiple real-world datasets and deployments on low-power edge devices demonstrate improvements over state-of-the-art baselines in most considered domains while maintaining lightweight computation at the client side.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Matteo Caligiuri, Francesco Barbato, Pietro Zanuttigh, Francesco Restuccia
- 发布：2026-08-08；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
