---
title: "Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity"
description: "Linear attention models allow a fixed state size and a fixed amount of compute per token."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.07386) · [PDF](https://arxiv.org/pdf/2607.07386)

## 一句话摘要

Linear attention models allow a fixed state size and a fixed amount of compute per token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Linear attention models allow a fixed state size and a fixed amount of compute per token. However, due to their limited state size, linear attention models fall behind in long-context recall compared to softmax-attention-based transformer architectures. Increasing the state size of linear attention improves recall performance but at the cost of higher FLOPs. In this work, we introduce Sparse Delta Memory (SDM), an architecture that scales the hidden state of gated linear RNNs to orders of magnitude higher capacity using a sparse addressing scheme. SDM extends the Gated DeltaNet architecture by replacing the dense key-value outer product with sparse reads and writes to a large explicit memory. We show that, under an isoFLOP constraint and with an identical number of parameters, a higher state memory capacity significantly improves performance on in-context learning and long-context retrieval tasks. Moreover, by learning the initial state of the SDM memory and therefore using it as a parametric memory, we show that the model further improves on a wide range of common-knowledge and reasoning tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lo\"ic Cabannes, Pierre-Emmanuel Mazar\'e, Ilze Amanda Auzina, Th\'eo Le Pendeven, Gergely Szilvasy, Matthijs Douze, Maria Lomeli, Justin Carpentier, Gabriel Synnaeve, Herv\'e J\'egou
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
