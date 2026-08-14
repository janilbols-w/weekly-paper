---
title: "Tevatron-Elastic: A Unified Abstraction for Training Elastic Retrievers and Rerankers"
description: "A single model scale challenges the flexibility of a production retrieval system: some settings need it faster, others need a smaller index, and the right trade-off changes with the workload."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.08809) · [PDF](https://arxiv.org/pdf/2608.08809)

## 一句话摘要

A single model scale challenges the flexibility of a production retrieval system: some settings need it faster, others need a smaller index, and the right trade-off changes with the workload.

## 为什么值得关注

待编辑增强。

## 摘要原文

A single model scale challenges the flexibility of a production retrieval system: some settings need it faster, others need a smaller index, and the right trade-off changes with the workload. In the context of information retrieval (IR), a transformer-based model can be made smaller in three ways---using fewer layers, passing fewer tokens through the upper layers, or producing a shorter embedding---and each way saves a different compute resource. These options have been studied one at a time, each as its own method with its own code and training setup, which makes them hard to combine or adapt to a new model. We present~\ours to bring all three under one simple abstraction: a single object names any size the model can run at, and a short schedule lists the sizes to train. Training then produces one checkpoint that serves all of those sizes, and at deployment the user picks any of them. The same abstraction covers both retrievers and rerankers and both encoder and decoder models, as it works through interfaces that Hugging Face transformers already expose; a new backbone is a configuration change, not new modeling code. Prior methods---Matryoshka embeddings, early exit, 2D~Matryoshka (e.g., Starbucks), and layerwise token compression---become special cases of our unified abstraction. The same interface also enables Matryoshka~LTC (MLTC), which jointly trains several token-compression ratios in one retriever checkpoint. To validate our framework, we train 20 checkpoints across three backbones and two tasks: the quality curves are smooth, one checkpoint costs little over a model trained for a single size, and a controlled study confirms the wallclock speedups. We release the framework and all checkpoints as a resource for building elastic retrieval systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yu Wang, Shengyao Zhuang, Xueguang Ma, Zongyu Wu, Jimmy Lin, Vivek Srikumar, Zhichao Xu
- 发布：2026-08-09；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
