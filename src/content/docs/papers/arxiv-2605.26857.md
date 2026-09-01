---
title: "Generalist Graph Anomaly Detection via Prototype-Based Distillation"
description: "Driven by the pressing demand for graph anomaly detection (GAD) in high-stakes domains, the generalist GAD paradigm, which trains a single detector transferable across new graphs, has recently gained growing attention."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.26857) · [PDF](https://arxiv.org/pdf/2605.26857)

## 一句话摘要

Driven by the pressing demand for graph anomaly detection (GAD) in high-stakes domains, the generalist GAD paradigm, which trains a single detector transferable across new graphs, has recently gained growing attention.

## 为什么值得关注

待编辑增强。

## 摘要原文

Driven by the pressing demand for graph anomaly detection (GAD) in high-stakes domains, the generalist GAD paradigm, which trains a single detector transferable across new graphs, has recently gained growing attention. However, existing methods often rely on scarce and costly annotations for training and sometimes even require few-shot support at inference, which limits their robustness to diverse and unseen anomaly patterns. To address this limitation, we introduce ProMoS, the first unsupervised generalist GAD framework, which detects anomalies by modeling the abundant normality in unlabeled data. ProMoS adopts a knowledge-distillation paradigm to distill normality priors from a frozen self-supervised graph neural network (GNN) teacher to a mixture-of-students model with shared global and lightweight personalized branches, enabling efficient and expressive normality modeling without learning from scratch. We further propose prototype-guided soft-label distillation to align teacher and student in a shared prototype space, enhancing cross-graph generalizability. During inference, ProMoS performs zero-shot anomaly detection on unseen graphs via distillation bias and prototype geometric deviation. Extensive experiments show the effectiveness and efficiency of ProMoS, charting a practical path toward label-free, zero-shot generalist GAD.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiming Xu, Zihan Chen, Zhen Peng, Song Wang, Bin Shi, Bo Dong, Chao Shen
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
