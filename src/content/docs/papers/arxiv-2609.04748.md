---
title: "Same Request, Different Answer: Quantization Amplifies Cache-Induced Divergence in LLM Serving"
description: "Major open-source serving stacks reuse the key-value tensors of a shared prefix by default."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.04748) · [PDF](https://arxiv.org/pdf/2609.04748)

## 一句话摘要

Major open-source serving stacks reuse the key-value tensors of a shared prefix by default.

## 为什么值得关注

待编辑增强。

## 摘要原文

Major open-source serving stacks reuse the key-value tensors of a shared prefix by default. We measure what this prefix reuse costs in reproducibility. Holding model, decoding, seed and request order fixed at batch size one, we ran an eighty-episode multi-turn agentic tool-use workload with prefix reuse on and off across two engines and four weight formats. Without prefix reuse, repeated runs reproduced every token and log-probability in all ten configurations. With it, cache-hit and recompute paths diverged on both engines. On llama.cpp with GGUF weights this path divergence rises with quantization: for Qwen2.5-7B over ten independent server histories, it reached 37.4 percent of episodes at 16-bit and 82.5 percent at four-bit. Near-tie decisions became only about 1.2 times as common, while the cache-path change in top-two margins grew 4.9-fold from 16-bit to three-bit. Serving four-bit weights through 16-bit kernels left divergence not detectably different from 16-bit, placing the amplification mainly in the quantized execution path. At Q4_K_M, run-to-run divergence came mainly from llama.cpp's server-level prompt cache: under the canonical episode order it moved divergence by 37.5 points, and at its default, divergence spanned 20.0 to 28.7 percent under five random orders. With cache state restored, each path reproduced exactly while the two still differed. In the tested stacks, cached serving is irreproducible because the cache state is absent from the request and not reset by default. A single-turn bridge shows path divergence reaching task outcomes with no detectable net change in accuracy. We release the harness, logs, and analysis pipeline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aditi Patodiya
- 发布：2026-09-07；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
