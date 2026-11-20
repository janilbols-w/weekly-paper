---
title: "MiSTiQ: MicroScaling Trellis Quantization for Extreme KV Cache Compression"
description: "Modern large language models (LLMs) increasingly support longer contexts and serve more concurrent requests, increasing both sequence lengths and batch sizes."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2611.21216) · [PDF](https://arxiv.org/pdf/2611.21216)

## 一句话摘要

Modern large language models (LLMs) increasingly support longer contexts and serve more concurrent requests, increasing both sequence lengths and batch sizes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern large language models (LLMs) increasingly support longer contexts and serve more concurrent requests, increasing both sequence lengths and batch sizes. Both trends increase KV-cache size and memory traffic during inference. KV-cache quantization reduces these costs, with recent approaches using codebook-based vector quantization to achieve extremely low bit widths. However, hardware constraints limit codebook size, and most methods reconstruct the cache in higher-precision floating-point formats for attention, limiting the computational benefits of quantization. To address these limitations, we introduce MiSTiQ, a drop-in replacement for codebook-based vector quantizers that combines trellis-coded storage with microscaling (MX) formats for low-precision computation. We combine trellis quantization with beam search to encode the KV cache over large reconstruction spaces without large codebooks. To support MX computation, we derive MX-Hash functions that generate reconstruction values directly in the target MX element format. These functions use the scale-conditioned marginal distribution of block-normalized Gaussian inputs. On Llama3 and Qwen3, MiSTiQ achieves lower WikiText perplexity and higher GSM8K accuracy than the evaluated baselines across several block-scale formats at approximately 1.25 effective bits per element. With NVFP4, it also achieves the highest LongBench average on both models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 22 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: microscaling, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ofir Gordon, Lior Dikstein, Paul Balanca, Idan Achituve, Douglas Orr, Hai Victor Habi
- 发布：2026-11-16；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
