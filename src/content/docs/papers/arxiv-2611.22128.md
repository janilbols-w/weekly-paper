---
title: "TempQuant: Learning Adaptive Temperatures for Quantized Language Models"
description: "Large language models are increasingly deployed at low precision, yet quantization can degrade their performance."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.22128) · [PDF](https://arxiv.org/pdf/2611.22128)

## 一句话摘要

Large language models are increasingly deployed at low precision, yet quantization can degrade their performance.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are increasingly deployed at low precision, yet quantization can degrade their performance. We study how quantization interacts with decoding settings such as the sampling temperature and top-p by examining how it distorts the model's next-token probabilities. Measuring entropy during generation across deployed temperatures, we find that quantization warms the model on average, and that temperature matters much more for the performance of a quantized model than for its full-precision counterpart. Because quantization and temperature both shape the next-token distribution, we investigate how much the sampling settings can undo what quantization changes, through our method TempQuant, which learns the quantized model's temperature and top-p to bring its next-token probabilities closer to the full-precision model's. We learn these settings at two granularities. The first is a single global setting per requested temperature, which finds nearly the same temperatures that tuning on labeled answers would, without any labels. Model cards typically recommend sampling a quantized model with the same settings as its full-precision counterpart, while we find that different settings can substantially improve its accuracy. On 3-bit Qwen3-4B, for example, global TempQuant raises MATH accuracy from 34% under the configuration recommended for Qwen's quantized releases to 51%. The second sets the temperature and top-p for every token, motivated by our finding that tokens whose rankings flip under quantization tend to need warming, while tokens whose rankings are preserved tend to need cooling. When quantization degrades accuracy substantially, TempQuant recovers much of it, and when degradation is lighter, it still brings the quantized model's behavior closer to the full-precision model's.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: low precision, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mukund Athmaram, Liang Ma, Manoj Rao
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
