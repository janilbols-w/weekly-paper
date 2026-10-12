---
title: "TTS-Q: Perception-Guided Post-Training Quantization of Text-to-Speech Diffusion Transformers"
description: "Zero-shot text-to-speech (TTS) can clone a voice from seconds of audio."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.12474) · [PDF](https://arxiv.org/pdf/2610.12474)

## 一句话摘要

Zero-shot text-to-speech (TTS) can clone a voice from seconds of audio.

## 为什么值得关注

待编辑增强。

## 摘要原文

Zero-shot text-to-speech (TTS) can clone a voice from seconds of audio. Yet the quality comes from billion-parameter diffusion transformers whose size and multi-step sampling put them out of reach of the on-device, assistive, and real-time applications that need them most. Post-training quantization (PTQ) shrinks such models without retraining, but it has been built for language and vision, not speech. At 4 bits, a strong quantizer leaves intelligibility close to full precision but consistently erodes speaker timbre, so error rates stay low while the voice drifts from the target speaker. We ask why quantization hurts speech, where the damage lives, and whether it can be repaired without retraining. To find out, we run the first 4-bit weight-and-activation (W4A4) PTQ study of a TTS diffusion transformer at 1B and 3.5B. The timbre cost comes from both the weight and the activation quantization, but only the activation part has the timestep structure a precision schedule can exploit. We therefore introduce TTS-Q, which selects hard-to-quantize items from task-matched calibration candidates and applies a budget-balanced mixed-precision schedule that assigns higher precision to late-step feed-forward activations. TTS-Q recovers timbre best at both scales, at no cost to intelligibility. Separately, the deployed calibrated-W4A4 reference reduces peak memory on GPU, providing a practical reference for resource-constrained TTS deployment.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xiaoqin Feng, Yuqi Li, Weilun Feng, Yi-Cheng Lin, Kai Li, Xianglong Wang, Kuo Yang, Chuanguang Yang, Yingli Tian, Wei Li, Zhongwei Cheng, Lin Chen
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
