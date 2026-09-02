---
title: "Unified Multi-Dialectal Neural Machine Translation for Bangla Using the Dwadash Benchmark Corpus"
description: "Neural Machine Translation (NMT) and Large Language Models (LLMs) excel at cross-lingual tasks but often fail to capture intra-lingual morphological variation, marginalizing dialectal speakers."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.12018) · [PDF](https://arxiv.org/pdf/2608.12018)

## 一句话摘要

Neural Machine Translation (NMT) and Large Language Models (LLMs) excel at cross-lingual tasks but often fail to capture intra-lingual morphological variation, marginalizing dialectal speakers.

## 为什么值得关注

待编辑增强。

## 摘要原文

Neural Machine Translation (NMT) and Large Language Models (LLMs) excel at cross-lingual tasks but often fail to capture intra-lingual morphological variation, marginalizing dialectal speakers. In Bangla, existing translation frameworks commonly rely on Standard Colloquial Bangla (SCB) as an intermediate pivot, which can compound errors and reduce cross-dialectal nuance. To address this gap, we introduce a unified, multi-directional NMT system for direct translation between SCB and eleven regional variants. We first review prior dialectal NLP resources to identify existing technological gaps. As a foundational contribution, we construct and release a large multi-dialect parallel corpus for Bangla, comprising 14,562 aligned rows and 51,541 non-null sentence pairs through the integration of seven prior datasets and native-speaker-verified manual augmentation. Using this corpus, we benchmark state-of-the-art sequence-to-sequence architectures with parameter-efficient Weight-Decomposed Low-Rank Adaptation (DoRA). Results show that deep monolingual pre-training is more effective than large multilingual capacity for this task. The compact BanglaT5 model outperforms NLLB-200 and mBART-50 by up to 13.96 BLEU, achieving 29.26 BLEU, 57.26 chrF++, and 49.68 METEOR. A dataset scaling study shows diminishing returns beyond 3,000 parallel pairs and indicates that linguistic proximity to Standard Bangla is more important than raw data volume for translation quality. Finally, we deploy the optimized model as an INT8-quantized web application, providing a scalable, open-source framework for inclusive language technology and equitable digital access.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rakib Ullah, Md. Ruhul Islam, Tanbir Ahmed, Nayan Kumar Nath
- 发布：2026-09-02；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
