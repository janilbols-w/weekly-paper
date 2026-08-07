---
title: "QEvict: Recoverable Quantized KV Eviction for Attention-Drift-Robust Long-Context Decoding"
description: "Autoregressive large language model inference is increasingly constrained by the memory footprint of the Key-Value (KV) cache."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.05326) · [PDF](https://arxiv.org/pdf/2608.05326)

## 一句话摘要

Autoregressive large language model inference is increasingly constrained by the memory footprint of the Key-Value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive large language model inference is increasingly constrained by the memory footprint of the Key-Value (KV) cache. A dominant line of work reduces this footprint by evicting tokens that appear unimportant under attention-derived scores. However, such policies make an implicit irreversible decision: once a token is evicted, it cannot become useful again. We show that this assumption is brittle during decoding. Token and window importance drift as generated queries evolve, causing standard eviction policies to permanently discard states that later receive substantial attention under the full-cache model. To characterize this behaviour, we introduce Future Missed Mass and Global LIR, two diagnostics that measure future attention assigned to discarded states and the reactivation of historically inactive regions. We propose QEvict, a three-tier KV-cache management scheme that replaces binary retain-or-delete eviction with recoverable eviction. QEvict maintains high-confidence windows in full precision, stores intermediate windows in a quantized recoverable tier, and deletes only the lowest-confidence windows. During decoding, cumulative attention scores update window importance and when a quantized window becomes important again, it is dequantized and promoted to the full-precision. Under a fixed memory budget, this design preserves broader historical context while retaining exact full precision for the most important regions. Across long-context understanding, retrieval, and reasoning benchmarks, QEvict consistently improves over representative eviction and quantization baselines, reducing missed attention and improving information retention

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 8 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ayushman Garg, Akshita Gupta, Shaswata Bhattacharya, Abhishek Gupta, Sandeep Kumar, Manoj Kumar
- 发布：2026-08-05；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
