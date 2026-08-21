---
title: "UniFed-VLM: Federated Instruction Tuning for Vision-Language Models with Multiple Heterogeneity"
description: "Vision-Language Models (VLMs) have demonstrated strong performance in multimodal understanding and generation."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.15516) · [PDF](https://arxiv.org/pdf/2608.15516)

## 一句话摘要

Vision-Language Models (VLMs) have demonstrated strong performance in multimodal understanding and generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language Models (VLMs) have demonstrated strong performance in multimodal understanding and generation. However, fine-tuning of VLMs typically relies on centralized data, which raises privacy concerns in certain domains (e.g. healthcare). Federated Learning (FL) provides a natural solution by enabling model training without sharing raw data. However, applying FL to VLM instruction tuning is highly challenging. VLMs have substantial parameter scales, and in real-world scenarios, clients exhibit significant heterogeneity in tasks, modalities, and model architectures. Existing methods mainly focus on simplified settings and are unable to handle such multi-dimensional heterogeneous scenarios. In this work, we study federated instruction tuning under joint heterogeneity in tasks, modalities, and model architectures. We propose UniFed-VLM, a unified federated instruction tuning framework for VLMs that addresses multiple types of heterogeneity. It consists of two key components: 1) Federated Compensated Subspace Aggregation (FedCSA), which performs subspace-aligned aggregation of parameter-efficient adapters with dynamic weighting and compensation to mitigate heterogeneity-induced conflicts; 2) Two-stage Collaborative Distillation (TCoD), which enables effective knowledge transfer across heterogeneous models via a Mutual Distillation Adapter (MDA) and a mixture-of-experts-based distillation strategy. We conduct experiments on multiple benchmark datasets, and the results show that UniFed-VLM achieves stronger average performance across diverse tasks compared with existing FL methods. The source code is available at: https://github.com/wangpengyu2004/UniFed-VLM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Pengyu Wang, Baochen Xiong, Xiaoshan Yang, Yifan Xu, Zhang Qimeng, Haifeng Chen, Changsheng Xu
- 发布：2026-08-16；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/wangpengyu2004/UniFed-VLM](https://github.com/wangpengyu2004/UniFed-VLM)
- 阅读深度：metadata
