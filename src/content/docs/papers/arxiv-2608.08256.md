---
title: "AraSSM: A bidirectional state-space encoder for Arabic masked language modeling"
description: "Pretrained Transformer encoders such as AraBERT, MARBERT, and CAMeLBERT have become the standard backbone for Arabic natural language understanding, but their self-attention mechanism scales quadratically with sequence length, which limits efficiency on long documents."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2608.08256) · [PDF](https://arxiv.org/pdf/2608.08256)

## 一句话摘要

Pretrained Transformer encoders such as AraBERT, MARBERT, and CAMeLBERT have become the standard backbone for Arabic natural language understanding, but their self-attention mechanism scales quadratically with sequence length, which limits efficiency on long documents.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pretrained Transformer encoders such as AraBERT, MARBERT, and CAMeLBERT have become the standard backbone for Arabic natural language understanding, but their self-attention mechanism scales quadratically with sequence length, which limits efficiency on long documents. Mamba, a selective state-space model (SSM), offers linear-time sequence modeling as a competitive alternative to attention, yet no dedicated bidirectional Mamba encoder pretrained specifically for Arabic currently exists. We introduce AraSSM, a bidirectional Mamba encoder pretrained via masked language modeling on a corpus combining Arabic Wikipedia and CulturaX text, trained end-to-end on four consumer-grade NVIDIA RTX 2080Ti GPUs (11GB) over approximately ten days. We evaluate AraSSM by fine-tuning on four established Arabic NLU benchmarks covering sentiment classification (HARD), named entity recognition (ANERcorp), extractive question answering (ARCD), and natural language inference (XNLI-ar), following the per-task evaluation protocol introduced by AraBERT, and report results as mean +/- standard deviation across three fine-tuning seeds. AraSSM matches or exceeds published base-sized Transformer baselines on sentiment classification (96.37 +/- 0.03% accuracy on HARD), is competitive on extractive QA (32.19 +/- 1.07 EM, 63.79 +/- 0.25 F1 on ARCD) and named entity recognition (81.54 +/- 0.30 entity-level F1 on ANERcorp), and trails the base-sized Transformer range on natural language inference (72.83 +/- 0.07% accuracy on XNLI-ar), despite being trained entirely from scratch on consumer hardware rather than large-scale accelerator clusters.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ahmed Amine Aliane, Hassina Aliane, Nasredine Semmar
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
