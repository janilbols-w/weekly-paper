---
title: "BnBERT-iPET: Sparse Few-Shot Language Modeling for Bengali via Lottery Ticket Pruning"
description: "Deep neural networks have shown impressive success in NLP tasks owing to their complex structure and huge number of edges."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.05104) · [PDF](https://arxiv.org/pdf/2608.05104)

## 一句话摘要

Deep neural networks have shown impressive success in NLP tasks owing to their complex structure and huge number of edges.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep neural networks have shown impressive success in NLP tasks owing to their complex structure and huge number of edges. Achieving state-of-the-art performance in natural language processing with a large pre-trained model such as BERT is expensive and time-consuming, carries a large carbon footprint, and is difficult to realize on machines with minimal computational capability. This creates a barrier to training complex models for resource-constrained languages such as Bengali. However, in a complex neural model, not all edges are equally impactful, and the contributions of some of them can be neglected. Pruning promises to reduce the memory footprint of regular networks, shorten the training time of ever-growing networks, and increase inference efficiency without sacrificing comparable performance. In this work, we introduce BnBERT-iPET, a sparse few-shot language modeling approach for Bengali, and experimentally show that a lightweight few-shot-learned language model retaining only 10% of the edges of an initial model such as BERT can perform neck and neck with much larger models on challenging tasks for a resource-constrained language such as Bengali. By learning from few shots through iterative pattern exploiting training and achieving 90% sparsity with the Lottery Ticket Hypothesis pruning technique, our pruned BnBERT-iPET model proves to be a tough competitor to state-of-the-art language models such as Bangla Electra, Indic-BERT, and XLM-RoBERTa on downstream tasks over standard benchmark datasets of the Bengali language.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning, sparsity
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sajib Hossain, Md Kamrus Samad, Anan Ghosh, Labib Imam Chowdhury, Nabeel Mohammed
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
