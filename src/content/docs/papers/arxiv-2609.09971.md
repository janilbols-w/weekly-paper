---
title: "Deep Neural Networks for Learning Intent from sEMG Signals to Support Hardware Devices for Post-Stroke Neurorehabilitation"
description: "Finger-specific motor intent is a clinically meaningful control signal for post-stroke neurorehabilitation, where residual muscle activity may remain measurable despite weak or incomplete movement."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.09971) · [PDF](https://arxiv.org/pdf/2609.09971)

## 一句话摘要

Finger-specific motor intent is a clinically meaningful control signal for post-stroke neurorehabilitation, where residual muscle activity may remain measurable despite weak or incomplete movement.

## 为什么值得关注

待编辑增强。

## 摘要原文

Finger-specific motor intent is a clinically meaningful control signal for post-stroke neurorehabilitation, where residual muscle activity may remain measurable despite weak or incomplete movement. We study five-finger multilabel intent decoding from impaired-arm high-density surface electromyography (sEMG) in PhysioMio, a bilateral longitudinal dataset collected from stroke patients. A common processing protocol aligns movement labels, applies 20--450 Hz Butterworth filtering and Symlet-4 wavelet denoising, segments overlapping 200 ms windows, and extracts twelve time- and frequency-domain descriptors per channel. Direct LSTM, CNN, and GNN baselines reveal complementary behavior: the LSTM attains the highest subset accuracy (0.545), whereas the GNN attains the highest macro F1 (0.706) and macro AUPRC (0.776). Architecture search then identifies CNN-Large as the strongest single-split CNN, with 0.593 subset accuracy and 0.714 macro F1, while CNN-Micro provides a compact architecture for embedded inference. To match a four-sensor hardware design, we retrain CNN-Micro using channels associated with ECRB, ECRL, FDS, and FDP and exclude the ground electrode from model input. Across five seeds, cross-channel knowledge distillation improves the four-channel student over direct training, reaching $0.5219 \pm 0.0114$ subset accuracy, $0.7612 \pm 0.0038$ finger accuracy, and $0.6095 \pm 0.0058$ macro F1. The selected 123K-parameter model accepts nine windows of 48 features and has been exported to ONNX. These results establish a reproducible software path from post-stroke sEMG to compact five-finger intent prediction for subsequent hardware-in-the-loop evaluation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zakariyya Brewster, Divy Wadhwani, Emily Yan, Aidan Wang, Karma Namgyal, Shuting Xie, Markiyan Konyk, Tala Abdelmaguid
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
