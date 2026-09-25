---
title: "NAVIR: Neuromorphic Audio-Visual Speech Recognition for Robust Human-Robot Interaction on Edge Hardware"
description: "Voice-controlled interaction in industrial settings is hampered by acoustic noise, which severely degrades audio-only speech recognition."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.24391) · [PDF](https://arxiv.org/pdf/2609.24391)

## 一句话摘要

Voice-controlled interaction in industrial settings is hampered by acoustic noise, which severely degrades audio-only speech recognition.

## 为什么值得关注

待编辑增强。

## 摘要原文

Voice-controlled interaction in industrial settings is hampered by acoustic noise, which severely degrades audio-only speech recognition. Audio-visual speech recognition (AVSR) addresses this by fusing lip-motion cues with the audio stream, but state-of-the-art pipelines rely on three-dimensional convolutions, recurrent units, and attention modules that exceed the budget of typical edge devices. We present NAVIR, an end-to-end AVSR system targeting the BrainChip Akida neuromorphic processor, which natively supports only sequential two-dimensional convolutional inference. The pipeline factorises spatial and temporal encoding into separate AkidaNet-based modules: a per-frame visual encoder, a temporal video encoder, and a spectrogram audio encoder, fused by a lightweight predictor head and decoded by constrained beam search. Models are trained with connectionist temporal classification on noise-augmented audio and then fine-tuned with quantization-aware training. On the GRID benchmark, the quantized audio-visual model reaches 14.0% word error rate (WER) under noise on the unseen-speaker split and 3.3% WER on the overlapped-speaker split, against 22.5% and 11.8% for audio-only baselines, and it attains 98.6% command accuracy at 1.5% WER on a task-specific industrial-command corpus. Operation-count analysis indicates a 13-fold energy advantage of the spiking formulation over its artificial neural network counterpart at 27.6% mean firing rate. On-board measurements show roughly 5-fold lower energy per inference than a Raspberry Pi central processing unit on the lip-reading model, and over 100-fold lower than a laptop graphics processing unit, while sustaining 14.5 inferences per second. To the best of our knowledge, this is the first complete multimodal AVSR pipeline running on neuromorphic hardware of this class.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Leonidas Delimpasis, Panagiota Moraiti, Antonis Porichis, Panos Chatzakos, Michail Karamousadakis
- 发布：2026-09-21；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
