---
title: "Does synthetic pre-training pay off on a microcontroller? Accuracy, latency and energy across two MCUs"
description: "Rendered images are cheap to label, but a microcontroller classifier must survive 8-bit integer (INT8) quantisation and compute correctly on the chip."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.19931) · [PDF](https://arxiv.org/pdf/2611.19931)

## 一句话摘要

Rendered images are cheap to label, but a microcontroller classifier must survive 8-bit integer (INT8) quantisation and compute correctly on the chip.

## 为什么值得关注

待编辑增强。

## 摘要原文

Rendered images are cheap to label, but a microcontroller classifier must survive 8-bit integer (INT8) quantisation and compute correctly on the chip. Five models, from MobileNetV2 at 224 px to a 61K-parameter convolutional neural network (CNN), were fine-tuned on a six-class scene dataset with and without a synthetic stage, against thresholds fixed in advance, and deployed on an ESP32-S3 and an RP2040. With full real data the stage gave no detectable gain. For the main deployable model the INT8 difference was +0.312 percentage points (pp), its interval below the +1.6 pp gain recomputed from the source study; quantisation did not detectably change it, nor did model size. With 10% of the real data the stage paid off for the CNN, by +3.438 pp on one seed and +2.715 pp over three; its cause is open. On the ESP32-S3 the main model took 152.7 ms and 16.3 mJ above idle per inference, and adding the stage changed neither beyond preset bounds. The model's INT8 outputs matched TensorFlow Lite's reference kernels exactly, but only after a memory overrun in a vendor kernel was patched. On the RP2040 the same model took 1.80 s and 27.3 mJ above idle, about twelve times slower, and the largest 96 px model exceeded the board's flash-capacity limit. Neither the RP2040 nor the host interpreter used for scoring reproduced the reference arithmetic. A synthetic stage is worth adding only when real data are scarce, and on-device INT8 outputs should be checked against reference kernels, not inferred from host scores.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Achintya Yadav
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
