---
title: "Six Layers Less: Encoder Pruning for Whisper with Label-Free Recovery"
description: "Pruning large pre-trained transformer-based ASR models such as OpenAI's Whisper has seen great adoption, as pruning the decoder led to significant end-to-end transcription speedups."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.27980) · [PDF](https://arxiv.org/pdf/2609.27980)

## 一句话摘要

Pruning large pre-trained transformer-based ASR models such as OpenAI's Whisper has seen great adoption, as pruning the decoder led to significant end-to-end transcription speedups.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pruning large pre-trained transformer-based ASR models such as OpenAI's Whisper has seen great adoption, as pruning the decoder led to significant end-to-end transcription speedups. For instance, the {\tt whisper-large-v3-turbo} variant reduced the decoder from 32 to 4 layers, while Distill-Whisper similarly reduced the decoder to only 2 layers. Although some attention has been put towards reducing the size of the encoder, no approach has seen wide adoption. This could be due to the need for custom inference implementations to take advantage of the compressed model. We present an approach that ranks encoder layers by the leave-one-layer-out change in Word Error Rate (WER). The six layers that cause the least change are removed, corresponding to $18.5\%$ of the encoder stack. The pruned model requires no custom inference code as it is simply a more shallow encoder with fewer layers. We further distill using unlabeled monolingual speech data to recover performance degradation caused by the zero-shot layer pruning. Mean WER across four languages increases to $20.1\%$ after distillation, compared to $21.9\%$ zero-shot, going from a baseline of $18.2\%$. We release all of our code (https://github.com/rasgaard/whisper-encoder-layer-prune) and the pruned model (https://huggingface.co/rasgaard/whisper-large-v3-turbo-encoder-pruned).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: compressed model, distillation, pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Rasmus Aagaard, Nicki Skafte Detlefsen
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/rasgaard/whisper-encoder-layer-prune](https://github.com/rasgaard/whisper-encoder-layer-prune)
- 阅读深度：metadata
