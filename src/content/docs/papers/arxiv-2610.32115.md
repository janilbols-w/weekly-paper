---
title: "EDWARD-NMT: Elastic Dimensions With Adaptive Routing and Dual-consistency for Neural Machine Translation"
description: "Sparse Mixture-of-Experts (MoE) is a powerful paradigm for scaling Neural Machine Translation (NMT) and managing language heterogeneity."
---

**评分：42/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.32115) · [PDF](https://arxiv.org/pdf/2610.32115)

## 一句话摘要

Sparse Mixture-of-Experts (MoE) is a powerful paradigm for scaling Neural Machine Translation (NMT) and managing language heterogeneity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Sparse Mixture-of-Experts (MoE) is a powerful paradigm for scaling Neural Machine Translation (NMT) and managing language heterogeneity. However, practical limitations hinder its deployment on resource-constrained devices: the entire expert pool must remain in memory, and the per-token compute budget is statically fixed during training by rigid top-k routing. We introduce EDWARD-NMT (Elastic Dimensions With Adaptive Routing and Dual-consistency for NMT), a novel MoE encoder-decoder architecture designed for a train once, deploy anywhere paradigm that exposes a family of deployable sub-networks at inference time. EDWARD-NMT integrates three key innovations: (i) Matryoshka-style elastic dimensions to flexibly reduce the memory footprint; (ii) an adaptive sigmoid router with a learned, task-conditioned threshold, allowing each token to dynamically determine its active expert count; and (iii) a dual-consistency objective to maximize the performance of the extracted sub-networks. Extensive experiments on PhoMT (En-Vi), WMT-14 (En-De), multilingual OPUS-16, and a multi-domain De-En benchmark validate our approach. The full-capacity architecture matches or exceeds strong MoE baselines with improved parameter efficiency. Furthermore, the sub-networks seamlessly extracted from a single checkpoint consistently outperform comparably sized dense Transformers without any retraining.

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

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Edward Nguyen, Thai Tran, Kiet Anh Hoang, Duy Hoang, Duy Vo, Khanh Le, Vu Le
- 发布：2026-10-26；更新：2026-10-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
