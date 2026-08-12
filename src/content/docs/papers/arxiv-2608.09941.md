---
title: "The Multilingual Quantization Tax: Structural Collapse and Typological Fragility in Edge SLMs"
description: "While 4-bit weight quantization is critical for deploying Small Language Models (SLMs) on edge devices, evaluations of the resulting performance degradation-the quantization tax-remain overwhelmingly English-centric."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.09941) · [PDF](https://arxiv.org/pdf/2608.09941)

## 一句话摘要

While 4-bit weight quantization is critical for deploying Small Language Models (SLMs) on edge devices, evaluations of the resulting performance degradation-the quantization tax-remain overwhelmingly English-centric.

## 为什么值得关注

待编辑增强。

## 摘要原文

While 4-bit weight quantization is critical for deploying Small Language Models (SLMs) on edge devices, evaluations of the resulting performance degradation-the quantization tax-remain overwhelmingly English-centric. We present a zero-shot multilingual evaluation of 4-bit quantization across the Gemma 4 and Qwen 3.5 architectures. Evaluating on eight typo-logically diverse languages using MMLU ProX Lite and GlobalPIQA, we show parameter truncation exposes deep pre-training inequalities. We identify four phenomena: (1) Typological Fragility: low-resource and specific non-Latin scripts suffer representational collapse via architecture-specific double dissociations, failing to generate valid task logits; (2) Home Language Fragility Paradox: foundational pre-training pathways provide limited precision loss protection; (3) Domain-Specific Forgetting: multi-step cross-lingual routing degrades while associative soft-science recall remains robust; and (4) Quantization Resistance: highly saturated, typologically aligned domains resist deterministic degradation, with post-quantization performance gains bounded by statistical noise.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mohammad Wathiq Soualhi
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
