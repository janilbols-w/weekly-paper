---
title: "Factorized Delayed Streams Modeling for LLM-based Streaming ASR"
description: "Delayed Streams Modeling (DSM) enables LLM-based streaming automatic speech recognition (ASR) by aligning acoustic and text streams on a common timeline."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.04333) · [PDF](https://arxiv.org/pdf/2610.04333)

## 一句话摘要

Delayed Streams Modeling (DSM) enables LLM-based streaming automatic speech recognition (ASR) by aligning acoustic and text streams on a common timeline.

## 为什么值得关注

待编辑增强。

## 摘要原文

Delayed Streams Modeling (DSM) enables LLM-based streaming automatic speech recognition (ASR) by aligning acoustic and text streams on a common timeline. DSM adds the padding token and the word-start token to the LLM vocabulary and predicts them together with normal text tokens using the same softmax. We first show that can be removed while maintaining competitive recognition performance. Based on this result, we propose Factorized DSM (F-DSM), which separates the waiting probability for from the distribution over the original LLM vocabulary. This factorization removes ASR-specific tokens from the text prediction space and allows the large-vocabulary softmax to be skipped on waiting steps. Experiments on the Corpus of Spontaneous Japanese and LibriSpeech show that F-DSM achieves better recognition performance than DSM. It also greatly reduces GPU memory use while maintaining similar training throughput, provides a small inference speed improvement through softmax skipping, and reduces the degradation in text-only perplexity observed with DSM.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: gpu memory
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tatsunari Takagi, Kai Washizaki, Atsushi Kojima, Lianbo Liu, Koki Nikaido, Yui Sudo
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
