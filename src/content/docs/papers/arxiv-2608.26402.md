---
title: "SILK: Streaming Authentication with In-Place Checks for Low-bit LLM Inference"
description: "A root-of-trust (RoT) supports model authentication at load time but does not guarantee integrity during inference."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.26402) · [PDF](https://arxiv.org/pdf/2608.26402)

## 一句话摘要

A root-of-trust (RoT) supports model authentication at load time but does not guarantee integrity during inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

A root-of-trust (RoT) supports model authentication at load time but does not guarantee integrity during inference. We present SILK, a quantization-aware in-place integrity framework protecting low-bit large language model (LLM) weights, activations, and KV caches against runtime tampering by embedding keyed checks directly into quantized data. Weight checks are embedded during second-order post-training quantization (GPTQ) to minimize distortion, while runtime tensors use redundant codes or fallback least significant bits (LSBs). An Ascon-based authentication chain absorbs each unit's cover bits into the next unit's authentication state, enabling single-pass verification. A streaming guard permits computation after bounded-strength confirmation and holds results until full authentication. Across evaluated symmetric INT4 models, mean perplexity increases remain below 0.4% with 0.2% weight metadata. Against Dual MAC guards, SILK cuts time overhead on Qwen2.5-0.5B weight reads at 4 B/cycle from 1.95% to 0.41% (Dual MAC-256) and energy-delay product (EDP) overhead at 4-8 B/cycle by 28-69% with DDR (up to 37% with HBM2), with 28% more guard-logic area.

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

- taxonomy keywords: int4, quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ruichen Qi, Xinting Jiang, Ema Dimitrova, Junyi Luo, Quan Cheng, Mehdi Saligane
- 发布：2026-08-26；更新：2026-11-26
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
