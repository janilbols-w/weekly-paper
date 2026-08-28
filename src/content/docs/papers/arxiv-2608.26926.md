---
title: "A Layer Importance Metric for Quantization Accounting for the Speed-Quality Trade-off in Autoregressive Models"
description: "Small language models (sLLMs) are nowadays hosted on devices with limited memory and computational budget."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.26926) · [PDF](https://arxiv.org/pdf/2608.26926)

## 一句话摘要

Small language models (sLLMs) are nowadays hosted on devices with limited memory and computational budget.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small language models (sLLMs) are nowadays hosted on devices with limited memory and computational budget. In an autoregressive setup, inference is memory-bandwidth bound: uniform quantization is often detrimental to such models, since their architecture has limited redundancies and only a few layers are not very sensitive to lower precision. We propose a composite metric that combines two orthogonal criteria: information retention (measured in terms of a normalized SQNR-based coefficient) and throughput gains (modeled using a roofline-based latency analysis). By profiling Gemma 3 1B, we find that Feed-Forward Network blocks and the embedding matrix are the most promising targets for acceleration. For each candidate, we estimate a normalized quality score based on simulated quantization and a normalized speed score based on roofline modeling with no actual execution needed. We combine the two scores in a composite priority coefficient, allowing us to tune the trade-off between speed and quality as needed. Our metric is general and can be used to prioritize individual blocks, their projection sublayers, or transformer layers as a whole. We evaluate our approach on several model architectures, showing that our estimates have at around 4% prediction error for the accelerated speedup. We find that our method generally allocates more resources to the most expressive layers compared to evolutionary search, specialized accelerators, or Shapley-value-based approaches that require expensive approximate inference. Our analytical approach makes sLLM quantization a predictable engineering task.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Artem Safronov
- 发布：2026-08-27；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
