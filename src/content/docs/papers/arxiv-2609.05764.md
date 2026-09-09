---
title: "Interface-Aware KV Cache Quantization for Dense On-Chip NVM in Long-Context LLM Decoding"
description: "The key-value (KV) cache is the dominant memory bottleneck in long-context large language model (LLM) decoding: every step reads it entirely, so decoding is memory-bandwidth bound."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.05764) · [PDF](https://arxiv.org/pdf/2609.05764)

## 一句话摘要

The key-value (KV) cache is the dominant memory bottleneck in long-context large language model (LLM) decoding: every step reads it entirely, so decoding is memory-bandwidth bound.

## 为什么值得关注

待编辑增强。

## 摘要原文

The key-value (KV) cache is the dominant memory bottleneck in long-context large language model (LLM) decoding: every step reads it entirely, so decoding is memory-bandwidth bound. Holding a quantized KV cache in dense on-chip non-volatile memory (NVM) removes the off-chip transfer. Existing KV quantization methods, however, were designed for GPU-style memory systems: KIVI attaches per-group metadata, adding about 25% to the stored KV cache; KVQuant keeps sparse full-precision outliers that a dense array cannot hold in place. This paper examines what these structures cost when the KV cache resides in NVM behind fixed-range converters, and designs a quantization scheme matched to that interface. The architecture stores the quantized KV cache in dense on-chip NVM, uses a small static analog crossbar only for the fixed rotation, and keeps attention in on-chip digital logic. A randomized rotation and per-vector normalization give every coordinate the same range, so one fixed codebook for keys and one for values, each shared across all tokens of the corresponding tensor type, serve the entire KV cache. The codebook thresholds are programmed once as the read converter's reference levels, enabling fixed-range digitization with no per-token converter reconfiguration. Dequantization is a sixteen-entry lookup and one norm multiply; the only per-vector metadata is one scalar, about 3%. Across models from 3B to 14B and contexts to 32k tokens, the four-bit KV cache maintains accuracy under storage and crossbar noise simulated at realistic device levels. KIVI and KVQuant remain more accurate in software; the advantage of our format lies at the memory interface: 3.1-3.6x lower KV read energy than both mapped to the same NVM, and 8x lower metadata overhead than KIVI. The contribution is a KV quantization co-designed with the NVM memory interface rather than a new accuracy record.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jiahao Zheng, Yifan Qin, Xiaobo Sharon Hu, Yiyu Shi
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
