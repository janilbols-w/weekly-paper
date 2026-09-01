---
title: "Investigating Social Bias Changes in Quantized Language Models"
description: "Post-training quantization reduces the memory needed to run large language models but alters their social biases in ways that aggregate metrics fail to capture."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2602.06181) · [PDF](https://arxiv.org/pdf/2602.06181)

## 一句话摘要

Post-training quantization reduces the memory needed to run large language models but alters their social biases in ways that aggregate metrics fail to capture.

## 为什么值得关注

待编辑增强。

## 摘要原文

Post-training quantization reduces the memory needed to run large language models but alters their social biases in ways that aggregate metrics fail to capture. We present the first large-scale study of 50 quantized models evaluated on PostTrainingBiasBench, a unified benchmark of 13 closed- and open-ended bias datasets. We identify a phenomenon we term quantization-induced bias flipping, in which quantization causes models to change responses from biased to unbiased and vice versa, up to 21% of the time, despite no change in aggregate bias scores. These flips are strongly associated with model uncertainty, where the responses with high uncertainty are 3-11x more likely to change than the confident ones. Quantization strength amplifies this effect, with 4-bit quantized models exhibiting 4-6x more behavioral changes than 8-bit quantized models. Critically, these changes create asymmetric impacts across demographic groups, where bias can worsen by up to 18.6% for some groups while improving by 14.1% for others, yielding misleadingly neutral aggregate outcomes. Larger models show no consistent robustness advantage, and group-specific shifts vary unpredictably across model families. Our findings demonstrate that compression fundamentally alters bias patterns, requiring crucial post-quantization evaluation and interventions to ensure reliability in practice.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Stanley Z. Hua, Sanae Lotfi, Irene Y. Chen
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
