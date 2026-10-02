---
title: "CARD: Cross-component Audio Representation Distillation for Encoder-Free Audio Captioning"
description: "Modern automated audio captioning systems pair a frozen audio encoder with a large language model (LLM) via a trainable projector, incurring the encoder's inference cost and bottlenecking the model through its fixed acoustic features."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.04619) · [PDF](https://arxiv.org/pdf/2607.04619)

## 一句话摘要

Modern automated audio captioning systems pair a frozen audio encoder with a large language model (LLM) via a trainable projector, incurring the encoder's inference cost and bottlenecking the model through its fixed acoustic features.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern automated audio captioning systems pair a frozen audio encoder with a large language model (LLM) via a trainable projector, incurring the encoder's inference cost and bottlenecking the model through its fixed acoustic features. We present CARD, an encoder-free audio captioning model that removes the encoder at inference: a 13.2M projector feeds a frozen LLM with merged LoRA adapters, while the teacher used to train it is discarded. CARD distills a pre-trained audio teacher (CLAP-HTSAT) into the model, but rather than injecting it into the LLM alone, it routes the teacher's representations across components: perceptual stages to the projector and semantic stages to the LLM. This placement improves CIDEr-D by +11.9 over an LLM-only distilled model on AudioCaps and by +5.0 on Clotho, reaching 55.4 against a 66.4 encoder-kept upper bound with no encoder at inference, showing that where a teacher's knowledge is placed matters as much as its presence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ganesh Pavan Kartikeya Bharadwaj Kolluri, Yuchen Zhang, Michael Kampouridis, Ravi Shekhar
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
