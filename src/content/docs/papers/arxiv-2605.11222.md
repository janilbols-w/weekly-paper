---
title: "ADMM-Q: An Improved Hessian-based Weight Quantizer for Post-Training Quantization of Large Language Models"
description: "Quantization is an effective strategy to reduce the storage and computation footprint of large language models (LLMs)."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.11222) · [PDF](https://arxiv.org/pdf/2605.11222)

## 一句话摘要

Quantization is an effective strategy to reduce the storage and computation footprint of large language models (LLMs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Quantization is an effective strategy to reduce the storage and computation footprint of large language models (LLMs). Post-training quantization (PTQ) is a leading approach for compressing LLMs. Popular weight quantization procedures, including GPTQ and RTN, suffer in model utility, especially at aggressive quantization levels (sub-4-bit). We propose ADMM-Q, a novel weight quantization algorithm that considers the layer-wise quantization problem. Our algorithm is based on a combinatorial variant of the Alternating Direction Method of Multipliers (ADMM). Our operator-splitting procedure updates weights continuously to minimize the layer-wise reconstruction error, while gradually enforcing the quantization constraints with convergence guarantees. We propose additional algorithmic enhancements (e.g., penalty scheduling, preconditioning, and a local search post-processing step) to make ADMM-Q efficient at LLM scale. ADMM-Q is modular and can be used as a drop-in replacement for any weight quantizer within existing quantization pipelines: ADMM-Q is fully composable with existing techniques including range clipping, learned or random rotations, and activation scaling. Using ADMM-Q in place of GPTQ on Qwen3-8B, we decrease WikiText-2 perplexity in: (i) the W3A16 weight-only setting (12.85 $\rightarrow$ 10.06); (ii) the W4A8 SmoothQuant procedure (9.29 $\rightarrow$ 8.68); and (iii) the W2A4KV4 SpinQuant procedure (66.11 $\rightarrow$ 19.42).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ryan Lucas, Mehdi Makni, Xiang Meng, Adam Deng, Rahul Mazumder
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
