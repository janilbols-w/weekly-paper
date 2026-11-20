---
title: "Rethinking KV Caching for LLM Decode: Free-Space Optical KV Regeneration for Reduction of Memory Traffic"
description: "Long-context large language model (LLM) decoding repeatedly reads the historical key-value (KV) cache, making multi-head attention (MHA) memory-bandwidth-bound."
---

**评分：48/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.19279) · [PDF](https://arxiv.org/pdf/2611.19279)

## 一句话摘要

Long-context large language model (LLM) decoding repeatedly reads the historical key-value (KV) cache, making multi-head attention (MHA) memory-bandwidth-bound.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context large language model (LLM) decoding repeatedly reads the historical key-value (KV) cache, making multi-head attention (MHA) memory-bandwidth-bound. Caching layer-input activations instead halves historical-cache storage and traffic, but requires regenerating KV from each cached activation. On digital accelerators such as GPUs, this regeneration takes far longer than fetching the activation from HBM. The KV regeneration overhead outweighs the savings from reduced memory traffic, shifting decode attention from a memory bottleneck to a compute bottleneck. We present OptiDecode, a hybrid optoelectronic decode-attention accelerator that regenerates historical KV using free-space optics and computes attention digitally. Projection weights remain resident on optical tiles, exploiting reuse across historical tokens for high-throughput optical regeneration. Scaling to large models introduces two challenges. First, distributing weights across tiles requires sending the same activations to every head group, while each readout die produces only partial KV. Activation replay shares one set of electrical-to-optical converters across head groups without costly broadcast. In-situ attention avoids transferring partial KV from readout dies to reducers by computing on them locally and exchanging only partial scores, probabilities, and partial outputs. Second, processing an activation chunk through all dependent stages takes longer than one activation-fetch interval. Chunk pipelining overlaps successive chunks so that OptiDecode sustains the HBM activation-fetch rate. OptiDecode demonstrates 1.92-1.99x decode-attention speedup over an ideal GPU KV-read baseline at equal peak HBM bandwidth (A100-B200), for 32K-token contexts across evaluated 30B-175B MHA models, approaching the 2x upper bound from halving historical memory traffic.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 16 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Aritra Bagchi, Bin Gao, James Spall, Jakub Pietrak, Weng-Fai Wong, Tulika Mitra
- 发布：2026-11-14；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
