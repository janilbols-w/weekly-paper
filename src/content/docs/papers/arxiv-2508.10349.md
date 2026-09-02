---
title: "FlexP-SFT: A Flexible Aggregation-Free Framework for On-Device Personalized Split Federated Fine-Tuning of LLMs"
description: "To fine-tune large language models (LLMs) over private data, federated learning (FL) has emerged as a promising paradigm."
---

**评分：43/100** · AI 基础设施 > 训练与数据中心基础设施 > 容错与弹性

[论文原文](https://arxiv.org/abs/2508.10349) · [PDF](https://arxiv.org/pdf/2508.10349)

## 一句话摘要

To fine-tune large language models (LLMs) over private data, federated learning (FL) has emerged as a promising paradigm.

## 为什么值得关注

待编辑增强。

## 摘要原文

To fine-tune large language models (LLMs) over private data, federated learning (FL) has emerged as a promising paradigm. However, the prohibitive memory and communication demands of LLMs render standard FL impractical for resource-constrained edge devices. While split federated learning (SFL) alleviates the computing burdens via model partitioning, existing frameworks still suffer from communication bottlenecks and straggler problem due to the parameter aggregation process. To address these challenges, we propose FlexP-SFT, a novel aggregation-free framework for personalized split federated fine-tuning, which fundamentally eliminates the client-side aggregation process. Crucially, to ensure robust training in the absence of global synchronization, we introduce a layer-flexible alignment strategy to balance personalization and generalization capabilities. We further formulate split-ratio selection as a resource-aware discrete optimization problem that jointly accounts for personalization accuracy and system cost. Our proposed scheme simultaneously enhances personalized performance, reduces communication overhead, and resolves the straggler problem. Extensive results show that FlexP-SFT substantially outperforms baselines in both accuracy and latency, and that the optimized split ratio achieves a better resource-accuracy trade-off than static or memory-only choices.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: straggler
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaxiang Geng, Tianjun Yuan, Pengchao Han, Ying Gao, Xianhao Chen, Bing Luo
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
