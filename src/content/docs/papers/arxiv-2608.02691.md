---
title: "Output-Aware Rotation for INT2 KV-Cache Quantization"
description: "The key-value (KV) cache has become a major memory and bandwidth bottleneck in long-context large language model inference, making ultra-low-bit quantization increasingly important."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.02691) · [PDF](https://arxiv.org/pdf/2608.02691)

## 一句话摘要

The key-value (KV) cache has become a major memory and bandwidth bottleneck in long-context large language model inference, making ultra-low-bit quantization increasingly important.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache has become a major memory and bandwidth bottleneck in long-context large language model inference, making ultra-low-bit quantization increasingly important. However, existing rotation-based INT2 methods optimize cache statistics or proxy errors before the complete attention readout, even though the model is ultimately affected by the error propagated through attention and the output projection $W_O$. To address this mismatch, we propose \textit{OptR}, an output-aware rotation method that minimizes post-$W_O$ attention-output error. OptR decomposes the post-$W_O$ attention-output error into key- and value-induced terms and learns per-head orthogonal corrections through the full INT2 quantization and attention path. OptR further applies an attention-equivalent key reparameterization to reduce large channel-wise offsets without changing the softmax distribution. Across three models and five reasoning and coding benchmarks, OptR consistently improves both QuaRot and OSCAR and strengthens long-context retrieval, while preserving the paged KV-cache format with negligible inference overhead.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vincent-Daniel Yun, Woosang Lim, Minsoo Cheong, Sunwoo Lee, Murali Annavaram, Sai Praneeth Karimireddy, Sungjoo Yoo
- 发布：2026-08-05；更新：2026-08-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
