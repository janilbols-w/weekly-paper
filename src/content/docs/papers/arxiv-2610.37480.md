---
title: "Keeping Inference in the Radio: Design and Measurement of a Spiking Accelerator for mmWave ISAC Activity Recognition"
description: "Integrated sensing and communication allows wireless networks to recognize human activity from the channel estimates that the receiver computes anyway."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.37480) · [PDF](https://arxiv.org/pdf/2610.37480)

## 一句话摘要

Integrated sensing and communication allows wireless networks to recognize human activity from the channel estimates that the receiver computes anyway.

## 为什么值得关注

待编辑增强。

## 摘要原文

Integrated sensing and communication allows wireless networks to recognize human activity from the channel estimates that the receiver computes anyway. The inference, however, runs on the general-purpose processors of the base station, access point or handset, which are the first components a device switches off to save energy. Always-on sensing therefore requires a classifier that is small enough to remain powered while the rest of the system sleeps. We investigate whether Spiking Neural Networks (SNNs) can provide such a classifier. To this end, we generate SNN accelerators for micro-Doppler activity recognition on the public DISC dataset (IEEE 802.11ay at 60 GHz) with the open-source Spiker+ framework, and implement them together with a spike encoder on a ZCU208 RFSoC, so that the complete chain from micro-Doppler frame to activity label runs in programmable logic. A fully connected SNN with 132 neurons achieves 94.7 % accuracy (90.7 % macro-F1) on unseen subjects and performs an inference in 206 microseconds. Compared to conventional networks of the same topology on the same device, it requires an eighth of the logic and 3.4X less dynamic energy per decision than a network fed the same binary spikes, at comparable accuracy, and 7.6X less than a network fed the 16-bit spectrogram, at 1.2 points lower accuracy. Quantization-aware training reduces its weights to 3 bits within half a percentage point of the 6-bit network at the same encoder threshold

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Anthony S\'anchez, Rafael Ruiz, Jos\'e A. Belloch, Jes\'us O. Lacruz, Joerg Widmer
- 发布：2026-10-28；更新：2026-10-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
