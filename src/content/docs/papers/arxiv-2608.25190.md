---
title: "BanglaMamba: Exploring State Space Models for Bangla Fake News Detection"
description: "Fake news detection has become an important Natural Language Processing (NLP) task due to the rapid spread of misinformation through online news platforms and social media."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.25190) · [PDF](https://arxiv.org/pdf/2608.25190)

## 一句话摘要

Fake news detection has become an important Natural Language Processing (NLP) task due to the rapid spread of misinformation through online news platforms and social media.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fake news detection has become an important Natural Language Processing (NLP) task due to the rapid spread of misinformation through online news platforms and social media. While transformer-based models such as BanglaBERT achieve strong performance for Bangla text classification, their quadratic computational complexity makes them less suitable for long-document processing in resource-constrained environments. This paper investigates Mamba-based State Space Models (SSMs) as an efficient alternative for Bangla fake news detection. We propose BanglaMamba and compare it with pre-trained BanglaBERT and a similarly configured BERT model trained from scratch. Experimental results show that BanglaBERT achieves the highest Macro-F1 score (0.9260), while BanglaMamba (0.9029) achieves performance comparable to the from-scratch CustomBERT (0.9057) despite using a different architecture. Meanwhile, BanglaMamba achieves approximately $2.2\times$ higher inference throughput and 49% lower inference peak GPU memory usage than the BERT-based models. Cross-dataset evaluation shows that BanglaBERT generalizes better to an external dataset, highlighting the importance of large-scale pretraining. These findings demonstrate that Mamba-based SSMs can provide a competitive and computationally efficient alternative to Transformer-based architectures for Bangla fake news detection, particularly in resource-constrained settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：M. K. Khalidi Siam
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
