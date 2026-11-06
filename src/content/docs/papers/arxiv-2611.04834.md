---
title: "Feeling of Knowing in Large Language Models"
description: "Post-training updates change what large language models (LLMs) can answer, but may leave their answerability judgments misaligned."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2611.04834) · [PDF](https://arxiv.org/pdf/2611.04834)

## 一句话摘要

Post-training updates change what large language models (LLMs) can answer, but may leave their answerability judgments misaligned.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training updates change what large language models (LLMs) can answer, but may leave their answerability judgments misaligned. We study this knowledge-judgment desynchronization through functional feeling of knowing (FoK), which supports selective generation, retrieval triggering, and model routing without implying subjective experience. We propose two trainable channels: a knowledge channel that changes answerability and a FoK channel that judges the current knowledge state. Three stages train them: on-policy supervised fine-tuning (OP-SFT) updates knowledge from corrected on-policy answers; knowledge-delta FoK training (K$\Delta$-FT) adapts judgments across intermediate knowledge states; and FoK-guided policy optimization (FGPO) trains the subsequent answer or explanation. Factual-QA experiments, cross-dataset evaluation, and three sequential updates show that explicit FoK alignment improves judgment quality on updated knowledge. MMLU and ARC-Easy separately assess capability preservation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zichuan Fu, Xian Wu, Jingtong Gao, Wenlin Zhang, Jiaxuan Li, Binhao Wang, Yimin Deng, Guojing Li, Xiaopeng Li, Derong Xu, Yefeng Zheng, Xiangyu Zhao
- 发布：2026-11-04；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
