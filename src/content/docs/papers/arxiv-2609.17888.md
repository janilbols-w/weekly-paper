---
title: "Long-Context Demonstration Selection Using State Space Models"
description: "We study the problem of demonstration selection, which involves selecting a subset of examples for prepending to a query to a language model."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.17888) · [PDF](https://arxiv.org/pdf/2609.17888)

## 一句话摘要

We study the problem of demonstration selection, which involves selecting a subset of examples for prepending to a query to a language model.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study the problem of demonstration selection, which involves selecting a subset of examples for prepending to a query to a language model. This problem is closely related to in-context learning and language model inference. Since the inference cost of a transformer model scales quadratically with sequence length, the selection problem becomes especially challenging in a long-context scenario. In this paper, we tackle this problem by building on state space models (SSMs), which require only linear inference time given the input. Our approach involves two algorithms. The first learns a small set of SSMs through distillation of a (trained) transformer model. We partition all the layers into consecutive groups. Then for each group, we estimate a separate state space model to replicate the input-output behavior within the adjacent layers. Second, we map the distilled model outputs to a small set of tokens, and apply these embeddings for demonstration selection in downstream applications. We perform extensive experiments in both synthetic and real-world datasets to validate our approach. We demonstrate that the distilled SSMs only incur an approximation error of less than $0.7\%$ relative to the true output. In downstream evaluation, we show that on several text classification and reasoning tasks, our approach reduces FLOPs by $14.2\times$ and improves accuracy by $6.48\%$ relative to baseline demonstration selection methods.

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

- 作者：Ziniu Zhang, Zhenshuo Zhang, Ruoxuan Xiong, Gene Cooperman, Hongyang R. Zhang
- 发布：2026-09-17；更新：2026-09-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
