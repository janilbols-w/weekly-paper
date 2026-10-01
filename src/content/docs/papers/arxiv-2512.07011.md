---
title: "Block Sparse Flash Attention"
description: "Modern large language models increasingly require long contexts for reasoning and multi-document tasks, but attention's quadratic complexity creates a severe computational bottleneck."
---

**评分：54/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2512.07011) · [PDF](https://arxiv.org/pdf/2512.07011)

## 一句话摘要

Modern large language models increasingly require long contexts for reasoning and multi-document tasks, but attention's quadratic complexity creates a severe computational bottleneck.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern large language models increasingly require long contexts for reasoning and multi-document tasks, but attention's quadratic complexity creates a severe computational bottleneck. We present Block Sparse Flash Attention (BSFA), a drop-in replacement that accelerates long-context inference while preserving model quality. Unlike methods that predict importance before computing scores, BSFA computes exact query-key similarities to select the top-k most important value blocks for each query. By comparing per-block maximum scores against calibrated thresholds, we skip approximately 50% of the computation and memory transfers for pruned blocks. Our training-free approach requires only a one-time threshold calibration on a small dataset to learn the per-layer and per-head attention score distributions. We provide a CUDA kernel implementation that can be used as a drop-in replacement for FlashAttention. On Llama-3.1-8B, BSFA achieves up to 1.13x end-to-end speedup on LongBench with only a 1.1% accuracy drop, and up to 1.24x on Needle-in-a-Haystack retrieval at a 1% accuracy drop. The attention kernel itself accelerates by up to 1.38x. We compare BSFA against five recent sparse attention baselines (SpargeAttention, MInference, FlexPrefill, XAttention, and BLASST), and verify the method on Qwen2.5-7B and on A6000 and H100 GPUs. The implementation is available at https://github.com/Danielohayon/Block-Sparse-Flash-Attention.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: attention kernel, flash attention
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Daniel Ohayon, Itay Lamprecht, Itay Hubara, Israel Cohen, Daniel Soudry, Noam Elata
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Danielohayon/Block-Sparse-Flash-Attention](https://github.com/Danielohayon/Block-Sparse-Flash-Attention)
- 阅读深度：metadata
