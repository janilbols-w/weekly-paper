---
title: "Deterministic, Reproducible Inference in Exact Integer Arithmetic, and Verifiable Distributed Inference as Its Consequence"
description: "Optimized floating-point inference is not reproducible across environments: the same model on different hardware, compilers or thread counts can produce different bits."
---

**评分：42/100** · LLM 高效推理 > Serving 与分布式推理 > 并行与通信

[论文原文](https://arxiv.org/abs/2611.13730) · [PDF](https://arxiv.org/pdf/2611.13730)

## 一句话摘要

Optimized floating-point inference is not reproducible across environments: the same model on different hardware, compilers or thread counts can produce different bits.

## 为什么值得关注

待编辑增强。

## 摘要原文

Optimized floating-point inference is not reproducible across environments: the same model on different hardware, compilers or thread counts can produce different bits. We present tritify, an open-source runtime that executes the forward pass of real models -- decoder-only language models, Mixture-of-Experts decoders, and the Segment Anything 2.1 image/video stack -- with the entire run-time path in exact integer arithmetic; floating point is confined to offline quantization and the float reference used for verification. We make three separate claims and verify each. (1) Cross-hardware reproducibility: the integer path produces bit-identical output run to run, across CPU instruction-set architectures, and across CPU/GPU, carried by a reproducing SHA-256 of the output. (2) Decision fidelity: the integer path reproduces the float reference's decision on the models and inputs tested, with the numeric exceptions measured; per-layer fidelity through sixteen layers of OLMoE-1B-7B and of a 106-billion-parameter MoE shows no fidelity cliff. (3) Location independence: a model's computation can be split across instruction sets, CPU and GPU, and networked machines with zero effect on the output bits. GLM-4.5-Air (106,852,251,264 parameters, 427 GB of integer codes) generated its answer across three machines, none of which can hold its integer codes in RAM, bit-identically to a single-host reference. The consequence is verifiable distributed inference: an untrusted server or a fleet of devices runs the model while an open scalar oracle re-derives the exact bytes; a guarantee against a dishonest server is future work. We do not claim a per-device speed-up, bit-equality of floating-valued intermediates, or confidentiality. Code: https://github.com/pelloran-inc/tritify

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distributed inference
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Sayed Amir Karim (Pelloran Inc.)
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/pelloran-inc/tritify](https://github.com/pelloran-inc/tritify)
- 阅读深度：metadata
