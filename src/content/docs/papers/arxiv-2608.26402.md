---
title: "SILK: Closing the Time-of-Check-to-Time-of-Use Gap in RoT-Protected AI Systems"
description: "Root-of-trust (RoT) authentication verifies a DNN model at load time, but weights may subsequently traverse DRAM, DMA, interconnect, and prefetch paths before reaching the compute engine."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.26402) · [PDF](https://arxiv.org/pdf/2608.26402)

## 一句话摘要

Root-of-trust (RoT) authentication verifies a DNN model at load time, but weights may subsequently traverse DRAM, DMA, interconnect, and prefetch paths before reaching the compute engine.

## 为什么值得关注

待编辑增强。

## 摘要原文

Root-of-trust (RoT) authentication verifies a DNN model at load time, but weights may subsequently traverse DRAM, DMA, interconnect, and prefetch paths before reaching the compute engine. Post-verification tampering along this path can therefore alter the weights actually consumed while leaving the authenticated model image unchanged, creating a time-of-check-to-time-of-use (TOCTOU) integrity gap. We present SILK (Streaming Inline Lightweight Keying), an in-place integrity mechanism that verifies the weight stream at the final pre-compute boundary. SILK repurposes quantized-weight LSBs as secret-keyed integrity bits and chains dependencies across weight bytes, so a local modification perturbs multiple integrity checks. A lightweight streaming checker recomputes these checks without separate authentication tags and uses commit gating to prevent unverified weights from reaching computation. Under a secure pseudorandom function (PRF), the forgery probability decreases exponentially with the number of affected checks, and measured miss rates closely track the analytical bound. SILK detects every stream-modifying instance in our functional attack suite. For INT8, it limits quality loss to at most 0.76 pp across evaluated CNNs and 0.17 perplexity across eight LLMs, while INT4 and MXFP4 provide a configurable security-quality tradeoff through check sparsity. On a Xilinx ZCU102, the synthesized reference pipelined implementation sustains 756 MB/s at only 1.00% of the equivalent area cost of a Caliptra 2.x RoT, while a configuration with a conservative per-attempt forgery bound of 2^-128 still sustains 678 MB/s at 6.15% of the RoT cost.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int4, int8, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruichen Qi, Xinting Jiang, Ema Dimitrova, Junyi Luo, Quan Cheng, Mehdi Saligane
- 发布：2026-08-26；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
