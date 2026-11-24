---
title: "SaturQ: Saturation-Aware Mixed-Precision Quantization"
description: "Mixed-precision quantization assigns each module of a language model its own precision format, such as NVFP4, FP8, or BF16, to minimize damage within a memory budget."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.12266) · [PDF](https://arxiv.org/pdf/2607.12266)

## 一句话摘要

Mixed-precision quantization assigns each module of a language model its own precision format, such as NVFP4, FP8, or BF16, to minimize damage within a memory budget.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixed-precision quantization assigns each module of a language model its own precision format, such as NVFP4, FP8, or BF16, to minimize damage within a memory budget. Most allocators predict the damage of a configuration by summing per-unit sensitivities measured in unquantized networks. But the sensitivity of a unit \textit{saturates} as more units are quantized, so the sum overprices the heavily quantized configurations that tight budgets require. Assuming only that damage accumulates by an associative, increasing, continuous rule restricts it to the form $g\bigl(\sum_i b_i\bigr)$, with summed sensitivities as the case of linear $g$. We propose SaturQ, which uses a concave $g$, fits the per-unit parameters $b_i$ from a single Aumann--Shapley path integral, and allocates formats with a linear program. On Qwen3-30B-A3B, SaturQ lowers KL divergence to BF16 by 11--23\% relative to ModelOpt AutoQuantize at 4.2--6.0 effective bits, and it outperforms an interaction-aware allocator that measures up to 2{,}410 configurations while measuring only three. It also predicts the damage of unmeasured configurations with a median error of 6.9--11.4\%, lower than Gaussian-process and random-forest surrogates fit to 300 configurations, and served allocations of Qwen3.6-27B and GLM-5.2 (753B) run faster than vendor NVFP4 checkpoints at comparable accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joshua Hill
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
