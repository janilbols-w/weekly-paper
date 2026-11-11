---
title: "MambaLoc: Lightweight Indoor Localization Using Cross-Modal Knowledge Distillation"
description: "Accurate indoor localization on resource-constrained edge devices remains challenging due to the tension between modeling fidelity and computational efficiency."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.10360) · [PDF](https://arxiv.org/pdf/2611.10360)

## 一句话摘要

Accurate indoor localization on resource-constrained edge devices remains challenging due to the tension between modeling fidelity and computational efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Accurate indoor localization on resource-constrained edge devices remains challenging due to the tension between modeling fidelity and computational efficiency. Wi-Fi Channel State Information (CSI) enables low-cost deployment using existing Wi-Fi infrastructure but is heavily distorted by multipath propagation. Transformer-based solutions mitigate these effects but their quadratic complexity limits real-time edge deployment. Ultra-Wideband (UWB) provides geometrically precise ranging yet requires dedicated infrastructure. We present MambaLoc, a cross-modal distillation framework that improves the accuracy-efficiency balance in CSI-based localization. MambaLoc uses a linear-time Selective State Space Model (Mamba) as a lightweight CSI student, guided during training by a UWB-Transformer teacher. A Feature Alignment Module bridges the representational gap between heterogeneous RF modalities, allowing the CSI model to inherit UWB-derived geometric structure without UWB hardware at inference. A probabilistic Gaussian Mixture regression head models multi-modal spatial ambiguity from multipath effects, avoiding the physically implausible averaging of deterministic regression. Evaluations on a real-world dataset show MambaLoc achieves a median localization error of 0.230 m, reducing error by 22.2% over a standalone Mamba baseline, while requiring 65.1% fewer FLOPs and 58% lower inference latency than Transformer-based approaches.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mohab Bahnassy, Omar Saqr, Hamada Rizk, Moustafa Youssef
- 发布：2026-11-10；更新：2026-11-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
