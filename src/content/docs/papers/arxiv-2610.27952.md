---
title: "Unsupervised Head Network Personalization for Split Computing via Federated Learning"
description: "Split Computing (SC) is a distributed inference method designed for balancing computational load and reducing latency by partitioning a neural network into head and tail networks and deploying them across both a mobile device and a server, respectively."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.27952) · [PDF](https://arxiv.org/pdf/2610.27952)

## 一句话摘要

Split Computing (SC) is a distributed inference method designed for balancing computational load and reducing latency by partitioning a neural network into head and tail networks and deploying them across both a mobile device and a server, respectively.

## 为什么值得关注

待编辑增强。

## 摘要原文

Split Computing (SC) is a distributed inference method designed for balancing computational load and reducing latency by partitioning a neural network into head and tail networks and deploying them across both a mobile device and a server, respectively. Due to the limited bandwidth and computational power of mobile devices, the head network is often replaced with a neural network that requires lower computational and communication resources. However, it is challenging to prepare a sufficient quantity and quality of labeled data on the mobile device side for training the replacement head network. Furthermore, the data prepared by mobile users often contains sensitive privacy information, making data aggregation difficult. In this paper, we propose a data-efficient head network training method for SC. This method utilizes federated learning and knowledge distillation to train the head network using a small amount of non-IID and unlabeled data from mobile devices, ensuring that the training datasets are not exposed. Moreover, by introducing personalization, we enhance the accuracy to levels comparable to or exceeding those of existing methods. The experimental evaluations demonstrate that, despite data constraints imposed only on our method, it achieves accuracy comparable to the baselines. Furthermore, it significantly reduces the communication requirements by 95% on mobile devices, with only a 3-5 percentage point drop in accuracy from the original model.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yutaro Horikawa, Takayuki Nishio
- 发布：2026-10-21；更新：2026-10-21
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
