---
title: "SemKV: Semantic Mixed-Precision KV Cache Quantization Guided by the Quality Cliff for Long-Context LLM Inference"
description: "The key-value (KV) cache is the dominant memory bottleneck of long-context large language model (LLM) inference, growing linearly with context length."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.28911) · [PDF](https://arxiv.org/pdf/2608.28911)

## 一句话摘要

The key-value (KV) cache is the dominant memory bottleneck of long-context large language model (LLM) inference, growing linearly with context length.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache is the dominant memory bottleneck of long-context large language model (LLM) inference, growing linearly with context length. We show that uniform KV quantization on a fractional-bit grid does not degrade gracefully: under a prespecified multi-seed statistical protocol, Llama-3.1-8B-Instruct with an affine quantizer is statistically indistinguishable from FP16 KV down to 2.322 code bits/value and collapses at 2.0 bits - a quality cliff in (2.0, 2.322] that reappears in generation-time quantization and multi-turn dialogue and transfers to Mistral-7B. The cliff reframes importance-aware mixed precision: above it, eight model-internal importance indicators are statistically interchangeable, so the benefit of mixing is grid interpolation, reaching average precisions uniform quantization cannot realize. SemKV preserves every token, ranks tokens by a model-internal score, and assigns two adjacent above-cliff precisions, achieving a measured 6.0x storage reduction with no statistically detectable quality difference from full KV (n=900, three seeds), and outperforming FP16 token pruning granted a 1.5x larger memory budget. Replacing the affine base with a distortion-optimized quantizer (TurboQuant-MSE) lowers the cliff in every protocol tested, raising the no-detectable-loss operating point to 7.9x. The recipe: measure the cliff for the target deployment setting, then interpolate above it.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixed precision, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Daeha Lee, Do-Hyung Kim, Jae-Hong Kim
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
