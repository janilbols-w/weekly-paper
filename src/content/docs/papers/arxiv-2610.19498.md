---
title: "What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains"
description: "Model signing authenticates the full-precision weights W an LLM is released with, yet users run a quantized artifact Q whose producing transformation is not uniquely determined under current disclosure."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.19498) · [PDF](https://arxiv.org/pdf/2610.19498)

## 一句话摘要

Model signing authenticates the full-precision weights W an LLM is released with, yet users run a quantized artifact Q whose producing transformation is not uniquely determined under current disclosure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Model signing authenticates the full-precision weights W an LLM is released with, yet users run a quantized artifact Q whose producing transformation is not uniquely determined under current disclosure. We separate the non-environment inputs from the execution environment E and measure a quantity that, to our knowledge, has not been measured before: the Independent Verifiability Rate (IVR), the fraction of a popularity-sampled GGUF ecosystem that a third party can re-derive bit-for-bit. Across the 200 most-downloaded Hugging Face GGUF repositories (198 in scope), no artifact or model card records the build environment, so under a recorded-inputs protocol the IVR is 0/198. Yet the artifacts are not irreproducible. On four in-sample repositories that disclose their inputs, the card's information alone reproduces no Q4_K_M file, but two coordinates the card omits - the build's floating-point-contraction setting and, for hybrid models, the per-tensor quantization recipe - re-derive 7/8 target-quant files bit-for-bit on x86 (5/8 on arm64); the fp16 re-derives from the provider's checkpoint, but the calibration imatrix must be shipped and hash-bound, since recomputing it did not match. An older release additionally pins the instruction set and did not re-derive. Reproducing the divergence reported with llama.cpp PR #25353, we show that E is a necessary coordinate and that one compiler setting yields a unique output across the tested platforms at negligible quality cost (+0.06% perplexity). As a security characterization, benign floating-point non-determinism separates from uniformly placed nibble-flip tampering above a detection floor that grows with the environments a verifier must allow, but a targeted embedding edit evades the statistic, so the proposed protocol rests on exact re-derivation; adversarial-fp16 attacks lie outside it. We release the audit data and a re-runnable harness.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 9 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Wei-Liang Liu, Cheng-Yen Tsai
- 发布：2026-10-14；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Rlonglong/gguf-verifiability-artifact](https://github.com/Rlonglong/gguf-verifiability-artifact)
- 阅读深度：metadata
