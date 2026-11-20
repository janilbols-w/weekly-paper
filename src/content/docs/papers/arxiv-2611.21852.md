---
title: "The Hidden Cost of MoE Diffusion Decoding: Profiling and Fixing the Sampler"
description: "Masked diffusion language models (dLLMs) decode by iteratively denoising a full canvas of tokens, so every forward pass runs a per-token sampling and stopping pipeline over the entire canvas-by-vocabulary logits tensor."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.21852) · [PDF](https://arxiv.org/pdf/2611.21852)

## 一句话摘要

Masked diffusion language models (dLLMs) decode by iteratively denoising a full canvas of tokens, so every forward pass runs a per-token sampling and stopping pipeline over the entire canvas-by-vocabulary logits tensor.

## 为什么值得关注

待编辑增强。

## 摘要原文

Masked diffusion language models (dLLMs) decode by iteratively denoising a full canvas of tokens, so every forward pass runs a per-token sampling and stopping pipeline over the entire canvas-by-vocabulary logits tensor. We profile single-user decoding of a 26B-parameter diffusion Mixture-of-Experts model on a bandwidth-bound edge accelerator (NVIDIA GB10) and report a result that is easy to miss: after weight quantisation, this logits pipeline, not the expert GEMMs, is the single largest consumer of decode time. Unlike autoregressive decoding, where sampling touches one position's logits per committed token, diffusion decoding processes S times as many logit entries per output token, where S is the number of denoising steps. We show this pipeline is largely redundant or fusable and remove it in two lossless tiers: a bit-exact tier whose output is byte-identical to the reference decoder, and an accuracy-parity tier using a fused single-pass entropy kernel and Gumbel-max sampling. Combined with a W4A16 expert kernel, the full stack reaches 2.4-2.7 times end-to-end speedup over bf16 at unchanged benchmark accuracy on GSM8K, HumanEval, and MATH, on a single 273 GB/s device. We confirm the finding on a second, independently built diffusion MoE (LLaDA2.0-mini: pipeline 28.8% of decode, fused W4A16 3.3 times at accuracy parity) and show it disappears on a dense diffusion model (3.6%). The cost is specific to MoE diffusion, where quantisation makes the backbone cheap. Code and quantised weights are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Harshit Samrat, Ramakrishna Paramahamsa Kompella
- 发布：2026-11-16；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
