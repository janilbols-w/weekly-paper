---
title: "A Calibrated Instrument for Measuring How Inference Optimizations Affect Output Quality"
description: "Large language model optimization is an active research area, spanning quantization of model weights, early-exit methods for skipping layers, and speculative decoding."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](http://arxiv.org/abs/2609.18005v1) · [PDF](https://arxiv.org/pdf/2609.18005v1)

## 一句话摘要

Large language model optimization is an active research area, spanning quantization of model weights, early-exit methods for skipping layers, and speculative decoding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model optimization is an active research area, spanning quantization of model weights, early-exit methods for skipping layers, and speculative decoding. Each track uses its own quality measures, typically an idiosyncratic benchmark score. Few approach the measurement precision required by other scientific disciplines. We propose a rigorous methodology for measuring output quality, suitable for cross-system and cross-technique comparison. We score outputs with an LLM as a judge, but calibrate the judge formally: we compare its scores on two ordinary runs of a model given the same prompts, verifying that it shows no systematic preference between statistically equivalent outputs and measuring its per-sample noise. Each design also includes a 'null' condition, provably identical in distribution to the unmodified model, whose measured difference must be zero. With this one instrument we measure several acceleration techniques on the same prompts, so their quality costs can be compared. Perceived quality proves highly dependent on the domain of discourse. A 4-bit model was indistinguishable from its 16-bit original down to our design's +/-0.3-point resolution, in English prose and Chinese alike. At 3-bit precision the same prompts lost 0.5 points in English prose, 0.9 in Chinese, and 1.1 on multi-step math; early exit that cost 0.7 points on prose cost 2.5 on math, cutting correctly solved problems from 19 of 27 to 6. The pattern held for models from Alibaba and from Meta, but not its magnitude: the same quantizer cost Meta's model 1.8 points where it cost Alibaba's 0.7. A model's certainty about a token predicts how likely it is to differ from the full model's choice, but not how much that difference affects judged quality, so acceptance rules relying on certainty cannot distinguish errors that matter from errors that don't.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jerry Kaplan
- 发布：2026-09-16；更新：2026-09-16
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/jerrykaplan/Calibrated-Instrument](https://github.com/jerrykaplan/Calibrated-Instrument)
- 阅读深度：metadata
