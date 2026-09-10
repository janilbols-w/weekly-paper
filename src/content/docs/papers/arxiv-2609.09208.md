---
title: "Shift-Accumulate Attention: Multiplier-Free Query--Key Products for Transformer Decoding"
description: "Power-of-two (PoT) quantisation turns a multiplication into a bit shift, so far only for the post-softmax attention--value product."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.09208) · [PDF](https://arxiv.org/pdf/2609.09208)

## 一句话摘要

Power-of-two (PoT) quantisation turns a multiplication into a bit shift, so far only for the post-softmax attention--value product.

## 为什么值得关注

待编辑增强。

## 摘要原文

Power-of-two (PoT) quantisation turns a multiplication into a bit shift, so far only for the post-softmax attention--value product. The earlier and larger product, S=QK^T, has not been reformulated the same way. We quantise the key cache to a signed power-of-two fixed-point code, so that every scalar multiplication in QK^T becomes a sign flip, a bit shift and an integer accumulation. A fixed-point head-room F>= e_max turns every shift index r=F-e into a non-negative left shift, making the accumulation exact in integer arithmetic. We add a sub-power mantissa extension that halves the score error for one extra shift-add, a shift-exact online softmax whose running maximum lives in an integer log2 domain so that every rescaling is itself an exact shift, and a log-quantised AV product. Fused CUDA kernels in a 1.1B Llama decoder on an RTX 4090: at B=8, T=32k the 4-bit kernel is 4.60x faster than FP16 scaled dot-product attention with a 2.5x smaller KV cache, and batched decoding crosses over at B=64 to 1.22x FP16 throughput at 11.02 against 13.77 GB peak memory. A matched INT8 multiply--accumulate kernel on the same tiling reaches 5.29x: on a GPU with a hardware 4-way INT8 dot product, shift-accumulate is not faster than the MAC it replaces. An iso-storage control--an 8-bit shift code of exactly one byte per key, run through the identical kernel--prices the arithmetic substitution alone at 2.02x at comparable accuracy. The advantage of the PoT representation is therefore its density and the removal of the multiplier, not raw GPU throughput. A sweep over exponent width, mantissa levels, granularity and rounding gives the design lesson: nearest-PoT relative error is scale-free, so extra exponent bits buy nothing (eps_S=0.1302 at 3, 4 and 5 bits) and accuracy must come from mantissa terms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
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

- 作者：Khubaib Ahmed, Amna Noor, Ahsan Ul haq
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
