---
title: "T2D: Target-to-Draft Model Pruning & Adaptation for Efficient Speculative Decoding"
description: "Speculative decoding significantly accelerates autoregressive text generation in Large Language Models (LLMs), but its efficacy depends largely on two key factors: the distributional alignment between the draft and the target model, and the draft model's latency during inference."
---

**评分：50/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2610.34103) · [PDF](https://arxiv.org/pdf/2610.34103)

## 一句话摘要

Speculative decoding significantly accelerates autoregressive text generation in Large Language Models (LLMs), but its efficacy depends largely on two key factors: the distributional alignment between the draft and the target model, and the draft model's latency during inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding significantly accelerates autoregressive text generation in Large Language Models (LLMs), but its efficacy depends largely on two key factors: the distributional alignment between the draft and the target model, and the draft model's latency during inference. However, existing approaches typically utilize independently pretrained small draft models or seek to prune the target model to a manually chosen architecture, thereby failing to explicitly balance the trade-off between draft model alignment and token generation efficiency. To address this gap, we formulate draft model design as an optimization problem and propose T2D, a framework that constructs draft models directly from the target model using latency-aware structured pruning and knowledge distillation. In this manner, T2D obtains draft models that are jointly optimized for both measured inference latency and cross-entropy loss on the target model's responses, resulting in superlative speculative decoding performance. Through extensive experiments on multi-domain speculative decoding benchmarks and across several target model families of differing scale, we demonstrate how T2D prunes up to 92\% of the target model to obtain highly performant draft models compared to competitive baselines. Moreover, draft models obtained via T2D can also be utilized by other speculative decoding token-alignment and knowledge distillation methods in a plug-and-play fashion, leading to further gains. Our findings underscore the importance of jointly navigating the draft model architecture-alignment frontier to unlock the full potential of speculative decoding for LLMs.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Shahriar Kabir Nahin, Xiao Ye, Muhao Chen, Ben Zhou, Anshuman Chhabra
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
