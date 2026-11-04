---
title: "GateTrim: Adaptive-Rank Quantization for Large Language Models"
description: "We introduce GateTrim, an adaptive-rank post-training quantization method for large language models that learns matrix-specific ranks through gate optimization and threshold-based rank selection."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.00654) · [PDF](https://arxiv.org/pdf/2611.00654)

## 一句话摘要

We introduce GateTrim, an adaptive-rank post-training quantization method for large language models that learns matrix-specific ranks through gate optimization and threshold-based rank selection.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce GateTrim, an adaptive-rank post-training quantization method for large language models that learns matrix-specific ranks through gate optimization and threshold-based rank selection. GateTrim standardizes the low-rank factors of a quantized low-rank--residual representation, learns a separate gate vector for each target weight matrix, and uses a shared threshold to automatically determine its retained rank. The resulting ranks can differ across matrices, and the compact quantized representations are subsequently reconstructed. We evaluate GateTrim under W4A8 on Qwen3-4B/8B/14B, Llama-3.2-3B-Instruct, and Llama-3.1-8B-Instruct. Across all five models, we observe a counterintuitive finding: increasing the threshold from $\tau=0.3$ to $\tau=0.7$ reduces the mean retained rank by 46.60%--67.89% while simultaneously lowering WikiText-2 perplexity by 0.59%--5.17%. Threshold 0.7 achieves the lowest mean retained rank and final perplexity among the three tested thresholds, 0.3, 0.5, and 0.7, and reduces measured target-export size by 1.50%--4.25% relative to 0.3. GateTrim uses an $8\times512$-token fitting pool and a separate development pool of the same size. Its Qwen3-4B/8B/14B perplexities at $\tau=0.7$ are numerically below TwinQuant's published W4A8 values, reported with a $128\times2048$-token calibration pool, in a cross-study comparison. On Qwen3-8B, the threshold-0.7 configuration already has the lowest perplexity before reconstruction under both tested initialization seeds; reconstruction improves it further without increasing retained rank or export size.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Hongwei Ren, Jincheng Ren, Yuchuan Zhou, Jingchun Ling
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
