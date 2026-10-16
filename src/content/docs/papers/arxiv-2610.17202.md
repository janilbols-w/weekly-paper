---
title: "MLAfication: Efficiently Enabling High-Fidelity MLA for Modern LLMs"
description: "Multi-Head Latent Attention (MLA) compresses the KV cache into a latent representation, reducing inference memory and bandwidth."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.17202v1) · [PDF](https://arxiv.org/pdf/2610.17202v1)

## 一句话摘要

Multi-Head Latent Attention (MLA) compresses the KV cache into a latent representation, reducing inference memory and bandwidth.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-Head Latent Attention (MLA) compresses the KV cache into a latent representation, reducing inference memory and bandwidth. Existing MHA2MLA/TransMLA methods do not support QKNorm and require costly recovery on modern LLMs, especially MoE. We present MLAfication, a QKNorm-compatible, parameter-efficient extension of MHA2MLA. It combines calibrated KNorm, parameter-efficient distillation, contribution-aware Partial-RoPE, and activation-aware joint KV initialization. Across MHA and GQA models, including QKNorm- and MoE-equipped variants, MLAfication preserves performance under substantial KV-cache compression, surpasses the current SOTA on commonsense and long-context benchmarks, and extends MLA conversion to modern architectures. On Qwen3-30B-A3B, MLAfication delivers up to $5.35\times$ the serving throughput of BF16 GQA and, combined with 4-bit KV quantization, reduces the KV-cache footprint by $94.73\%$. Our code is available at https://github.com/JT-Ushio/MLAfication.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Zile Wang, Zhide Xie, Tao Ji
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/JT-Ushio/MLAfication](https://github.com/JT-Ushio/MLAfication)
- 阅读深度：metadata
