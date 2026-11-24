---
title: "CarrierKV: An Edge LLM Accelerator with Positional Carrier Decomposition for Low-Bit KV Cache"
description: "Long-context decoding on edge devices is limited by DRAM, because every generated token reads the whole, growing KV cache."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.26857) · [PDF](https://arxiv.org/pdf/2611.26857)

## 一句话摘要

Long-context decoding on edge devices is limited by DRAM, because every generated token reads the whole, growing KV cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context decoding on edge devices is limited by DRAM, because every generated token reads the whole, growing KV cache. 4-bit block-scaled formats such as NVFP4 reduce this traffic but degrade accuracy: on Qwen3-4B, NVFP4 lowers 32K RULER (seven tasks) from 92.6 to 79.4, and a Hadamard rotation lowers it further to 57.7. We observe that most of the key energy is a positional carrier, one per-head vector that rotary position embedding (RoPE) rotates with position. In NVFP4, it sets the shared scale of most key blocks and lowers the signal-to-quantization-noise ratio of the content by about 5 dB, nearly one bit, yet it depends only on that vector and the position. We therefore introduce positional carrier decomposition, which removes the carrier before RoPE and stores only the content residual. We design a KV path that rotates and quantizes keys only after this removal and computes each attention score directly on the 4-bit code. We also design a positional phase engine that regenerates the carrier's score term for one key per cycle. At the same cache size as NVFP4, CarrierKV raises 32K RULER on Qwen3-4B from 79.4 to 91.1 and lowers the 32K PG19 perplexity increase of NVFP4 by 1.8 to 5.9 times on four models, outperforming SageAttention and P3-LLM on all four. Its loss also stays nearly flat as the cache grows, while that of NVFP4 rises. In a 22 nm FDSOI process at 600 MHz, CarrierKV's hardware increases the area of the NVFP4 accelerator by 2.9% and the energy of a 20K-token reasoning request on Qwen3-4B by 0.12% at the same decode latency. On Qwen3-4B at 32K, CarrierKV has a better RULER score than FP8 keys (91.1 against 89.3) and uses 13.7% less energy per token. The decomposition also lowers the 32K perplexity increase of 3-bit TurboQuant keys on Qwen3-4B from 69.7 to 0.76.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Junyi Luo, Xinting Jiang, Ruichen Qi, Gregory Kielian, Quan Cheng, Mehdi Saligane
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
