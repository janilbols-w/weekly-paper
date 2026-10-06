---
title: "Which Decisions Low-Bit Quantization Breaks, and How to Predict Them"
description: "Quantization saves memory by storing model weights with fewer bits."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.06564) · [PDF](https://arxiv.org/pdf/2608.06564)

## 一句话摘要

Quantization saves memory by storing model weights with fewer bits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization saves memory by storing model weights with fewer bits. It can also change model decisions, such as whether to call a tool or which option to choose from a finite set. We study these decision changes in 16 language models from 8 families at 4, 3 and 2 bits, across several post-training quantization settings. Our evaluation covers tool use, safety, general knowledge and social bias, using BFCL, XSTest, MMLU, BoolQ, BBQ and synthetic tasks. The decision margin is the score difference between two possible first tokens, measured before and after quantization. Writing the margin before quantization as $m$ and the margin after quantization as $m'$, we find an approximately linear relationship across decisions: $m' \approx c m + b$. The slope $c$ is usually below one and becomes smaller as precision falls, so quantization progressively shrinks decision margins. The offset $b$ is the same for every decision of one kind. Quantization therefore does not simply add random noise, and even a strong preference at full precision can flip. Quantization also affects different kinds of decisions to different degrees. Within tool use, whether to call a tool is often more sensitive than which tool to call: on 400 BFCL tasks, three of five models lose more completed calls than correct tool selections at 3-bit round-to-nearest. Under GPTQ and GGUF far fewer whether-to-call decisions flip than under plain rounding, so there is no single 3-bit failure point. The same relationship predicts how often decisions flip. Across 1,082 combinations of models, quantization settings, bit-widths and decision types, we fit the slope, the offset and the spread around the fitted line on half of the decisions and predict the flip rate on the other half. The predicted flip rate differs from the observed flip rate by a median of 1.0 percentage point, while reusing the flip rate of the first half misses by 1.3.

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

- 作者：Zekun Wu, Swati Dhiman, Adriano Koshiyama
- 发布：2026-09-30；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
