---
title: "Text Scores Can Miss Waveform Use: A Qwen2-Audio Quantization Case Study"
description: "Post-training quantization of speech language models is often summarized with text-output scores and nominal bit widths."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.26823) · [PDF](https://arxiv.org/pdf/2609.26823)

## 一句话摘要

Post-training quantization of speech language models is often summarized with text-output scores and nominal bit widths.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization of speech language models is often summarized with text-output scores and nominal bit widths. Those numbers alone do not establish behavior that depends on information missing from a transcript, or efficiency for a particular runtime. We introduce an evaluation protocol that separately tests lexical output, a transcript-insufficient endpoint, and a measured packed implementation. In a Qwen2-Audio case study, a translation-selected 6-bit allocation improves chrF by 2.36 on a frozen English-to-German replay, with paired 95% bootstrap interval [1.04, 3.62], but loses 3.91 percentage points on speaker-disjoint emotion recognition. At the same 6-bit budget, the uniform structural control reaches higher emotion accuracy than the selected allocation, and the front-layer control is also higher by point estimate on the same frozen set. At 7 bits, chrF improves by 3.28 with interval [2.08, 4.59], the emotion interval against FP16 includes zero, and a same-budget front-layer control still exceeds the selected allocation. A separate matched-budget 4.08-bit study finds roughly 10-point emotion deficits for every tested low-bit allocation and no selected-allocation advantage over frozen controls. Finally, a dequantized average-6-bit simulation retains the FP16 peak memory. This case study identifies a precision-dependent mismatch between lexical output, waveform-dependent behavior, and nominal precision. It does not establish a general failure of low-bit speech models or a deployment benefit for the selected allocation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mengzhe Geng, Jinxi Jin, Junhao Xu
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
