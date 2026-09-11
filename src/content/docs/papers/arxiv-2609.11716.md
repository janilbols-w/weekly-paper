---
title: "Why Does Post-Training Quantization Work?"
description: "Post-training quantization compresses large language models (LLMs) by storing their weights at reduced precision, and each quantized weight introduces an error into the hidden states."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.11716) · [PDF](https://arxiv.org/pdf/2609.11716)

## 一句话摘要

Post-training quantization compresses large language models (LLMs) by storing their weights at reduced precision, and each quantized weight introduces an error into the hidden states.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization compresses large language models (LLMs) by storing their weights at reduced precision, and each quantized weight introduces an error into the hidden states. Naively, these errors should accumulate with depth and corrupt next-token prediction; randomly initialized models accumulate these discrepancies rapidly, whereas quantized pretrained models accumulate much less hidden-state error and largely maintain downstream task performance, even though they were never trained with quantization noise. This raises the question we address: why does post-training quantization work? Comparing full-precision and quantized forward passes, we identify two mechanisms that characterize pretrained quantization robustness. First, the error a layer newly introduces tends to oppose the error it inherits from the layer's input. The two cancel partially such that the discrepancy between full-precision and quantized passes grows slowly. This counteracting residual interaction develops during pretraining. Our quantitative analysis identifies it as a major factor slowing hidden-error growth. Second, LM-head geometry preferentially preserves the scores and probabilities of high-ranked tokens, which typically represent the model's most confident predictions. Together, these mechanisms explain why quantization error that passes through numerous layers can still produce only small output changes, and we verify the findings across models and quantization settings.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuxiang Chen, Michael Beyer, Jun Zhu, Jianfei Chen
- 发布：2026-09-10；更新：2026-09-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
