---
title: "Implementation of Zero-shot Semantic Communication on Software Defined Radio"
description: "Semantic communication has recently gained traction for its ability to reduce the amount of data transmitted over a communication link by transmitting a task-oriented representation instead of the raw source."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.05764) · [PDF](https://arxiv.org/pdf/2610.05764)

## 一句话摘要

Semantic communication has recently gained traction for its ability to reduce the amount of data transmitted over a communication link by transmitting a task-oriented representation instead of the raw source.

## 为什么值得关注

待编辑增强。

## 摘要原文

Semantic communication has recently gained traction for its ability to reduce the amount of data transmitted over a communication link by transmitting a task-oriented representation instead of the raw source. Zero-shot semantic communication sends a general embedding from a vision-language model (VLM), so the same transmitter can serve new classification tasks without retraining. Most evidence for this advantage, however, comes from numerical simulation. We implement zero-shot semantic communication on a software-defined radio platform: a Raspberry Pi drives a pair of Analog Devices Active Learning Module (ADALM)-Pluto transceivers, with an image encoder at the transmitter and a text encoder at the receiver, and determines the zero-shot classification results via cosine similarity. We compare two VLMs, CLIP and MobileCLIP, across various channel conditions, i.e., different signal-to-noise ratios (SNRs). We validate that the semantic link spends 9x fewer channel uses per image than a JPEG plus 16-ary quadrature amplitude modulation baseline and still reaches 82% accuracy on CIFAR-10 at 22.3 dB, where the baseline scores 0%. On the traffic sign recognition dataset (TSRD), MobileCLIP correctly classifies 98.3% of unseen images at the same SNR. Offloading the image encoder to a neural processing unit reduces encoding to 13.4 ms per image, 49x faster than a Raspberry Pi 4 CPU, placing the transmitter within a real-time budget. Our implementation is publicly available at https://github.com/thanhlexyz/zsscsdr.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Thanh Le, Arif Dataesatu, Homare Murakami, Takeshi Matsumura
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/thanhlexyz/zsscsdr](https://github.com/thanhlexyz/zsscsdr)
- 阅读深度：metadata
