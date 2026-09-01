---
title: "Q-Strata: Hierarchical Bit Allocation for Mixed-Precision Quantization of Mixture-of-Experts LLMs"
description: "Mixed-precision quantization (MPQ) assigns a different bitwidth to each linear layer of a large language model (LLM) to minimize the quantization-induced quality loss under a fixed budget, but Mixture-of-Experts (MoE) models contain these layers in every expert of every MoE block, so the allocation space grows far larger than in a dense model."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.30564) · [PDF](https://arxiv.org/pdf/2608.30564)

## 一句话摘要

Mixed-precision quantization (MPQ) assigns a different bitwidth to each linear layer of a large language model (LLM) to minimize the quantization-induced quality loss under a fixed budget, but Mixture-of-Experts (MoE) models contain these layers in every expert of every MoE block, so the allocation space grows far larger than in a dense model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Mixed-precision quantization (MPQ) assigns a different bitwidth to each linear layer of a large language model (LLM) to minimize the quantization-induced quality loss under a fixed budget, but Mixture-of-Experts (MoE) models contain these layers in every expert of every MoE block, so the allocation space grows far larger than in a dense model. Existing methods either allocate within each block under a uniform per-block budget, or allocate across blocks through an additive proxy, and neither directly optimizes a model-level objective over the choices that couple the blocks. We propose Q-Strata, a bi-level allocator that ranks within-block assignments with a cheap proxy and allocates across blocks with a model-level objective evaluated on the assembled quantized model. Its inner stage caches a Pareto frontier of candidates per block over finely spaced budgets, leaving the outer stage to set one budget per block instead of a bitwidth for every linear layer. With the search reduced to one budget per block, the outer stage optimizes this model-level objective directly, capturing the inter-block coupling that additive proxies miss. On Mixtral-8x7B-Instruct, Qwen1.5-MoE-A2.7B, and DeepSeek-V2-Lite, Q-Strata consistently achieves lower WikiText2 perplexity than uniform-bitwidth GPTQ and the state-of-the-art MoE MPQ methods MxMoE and GEMQ in the low-bit regime. The code is available at https://github.com/snu-mllab/Q-Strata/tree/main.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Deokjae Lee, Sihun Chu, Hyun Oh Song
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/snu-mllab/Q-Strata/tree/main](https://github.com/snu-mllab/Q-Strata/tree/main)
- 阅读深度：metadata
