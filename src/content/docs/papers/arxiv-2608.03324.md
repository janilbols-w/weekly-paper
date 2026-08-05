---
title: "AS-FedBridge: Pseudo-Spike Bridge Distillation for Heterogeneous ANN-SNN Federated Learning"
description: "Federated learning enables collaborative model training across distributed edge devices while strictly preserving data privacy."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 能耗、成本与散热

[论文原文](https://arxiv.org/abs/2608.03324) · [PDF](https://arxiv.org/pdf/2608.03324)

## 一句话摘要

Federated learning enables collaborative model training across distributed edge devices while strictly preserving data privacy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Federated learning enables collaborative model training across distributed edge devices while strictly preserving data privacy. To facilitate practical deployment on resource-constrained edge devices, Spiking Neural Networks (SNNs) have emerged as a promising alternative to traditional Artificial Neural Networks (ANNs) due to their sparse computing mechanisms and high energy efficiency. However, jointly training ANNs and SNNs exposes a challenge of representational misalignment, which is intrinsically caused by differences in information representation, specifically the semantic gap between continuous real-valued activations in ANNs and discrete spatio-temporal spikes in SNNs. To overcome this barrier, we propose AS-FedBridge, a novel federated learning framework tailored for mixed ANN-SNN clients. AS-FedBridge features a lightweight Bridge equipped with a Pseudo-Spike Interface, which effectively projects continuous signals into a spike-compatible space to facilitate ANN-SNN alignment. Given the absence of existing mixed ANN-SNN federated frameworks, we establish a comprehensive benchmark to evaluate against multiple advanced heterogeneous FL methods. Our empirical analysis demonstrates a positive correlation between the degree of ANN-SNN alignment and the collaborative FL performance. Across four datasets, AS-FedBridge consistently demonstrates advanced accuracy while mitigating extreme scale, architecture, and client heterogeneity challenge. Furthermore, our framework enables a highly controllable trade-off between model performance and resource efficiency. AS-FedBridge accomplishes these robust performance gains while introducing only marginal computational overhead, establishing a robust and practical foundation for mixed ANN-SNN federated learning systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: energy efficiency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shengyang Li, Yiting Dong, Liuyang Song, Ximing Wang, Luyuan Xie, Cong Li, Qingni Shen, Zhaofei Yu
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
