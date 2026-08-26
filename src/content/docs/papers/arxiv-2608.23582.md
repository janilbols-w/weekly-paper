---
title: "Transformer Accelerator (TFA): A Macro-Op INT8 Hardware Chip for Transformer Inference and Machine Translation"
description: "We present the Transformer Accelerator (TFA), a synthesizable, parameterizable INT8 memory-to-memory engine for transformer inference."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.23582) · [PDF](https://arxiv.org/pdf/2608.23582)

## 一句话摘要

We present the Transformer Accelerator (TFA), a synthesizable, parameterizable INT8 memory-to-memory engine for transformer inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present the Transformer Accelerator (TFA), a synthesizable, parameterizable INT8 memory-to-memory engine for transformer inference. One time-multiplexed datapath handles prompt processing and autoregressive generation. TFA implements matrix multiplication, softmax, RMSNorm, elementwise, and copy/gather operations through eight 512-bit macro-op descriptors. Offline-compiled programs are fetched, validated, and dispatched through AXI interfaces, supporting encoder, decoder, and encoder-decoder models. The RTL combines an output-stationary multiply-accumulate array with ping-pong buffers that overlap DMA and compute, bit-exact reciprocal-square-root and divide units, key-value-cache and embedding addressing, and an abort-safe zero-padding write engine. A UVM environment byte-compares outputs against a bit-exact golden model. Across 25 tests and 34 constrained-random runs, TFA achieved zero mismatches, 100% functional coverage, and 94.96% code coverage. We compiled the t5-small encoder-decoder pipeline for English-to-French, German, and Romanian translation. On ten multilingual proverbs, TFA executed 70,320 descriptors and matched 37.9 MB of golden-model output with zero mismatches. INT8 output matched the floating-point reference token-for-token on five sentences; the rest produced valid alternative translations. Randomized-Hadamard reparameterization recovered about 11 dB of per-tensor INT8 signal-to-noise ratio across layers. The verification configuration achieved about 20x end-to-end speedup over a 22-thread CPU, while larger designs are projected to reduce energy per token by about 1000x. After RAM inference recoding, logic area fell to 2.73 mm2, and the design completed design-rule-clean synthesis and place-and-route on SkyWater sky130. TFA demonstrates end-to-end, bit-exact execution of pretrained transformers using compact hardware and compiler-managed quantization.

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

- taxonomy keywords: int8, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Shashank
- 发布：2026-08-26；更新：2026-08-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
