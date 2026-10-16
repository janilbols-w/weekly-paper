---
title: "Fractional Power-of-Two Quantization for Efficient and Effective Multiplier-Free LLM Inference"
description: "Large Language Models (LLMs) demand efficient inference, where the multiply-accumulate (MAC) operations in linear projections dominate compute and energy cost."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.21257) · [PDF](https://arxiv.org/pdf/2610.21257)

## 一句话摘要

Large Language Models (LLMs) demand efficient inference, where the multiply-accumulate (MAC) operations in linear projections dominate compute and energy cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) demand efficient inference, where the multiply-accumulate (MAC) operations in linear projections dominate compute and energy cost. Post-training quantization (PTQ) reduces this cost by mapping weights and activations to low-bit integers. Power-of-Two (PoT) weight quantization promises efficient multiplier-free LLM inference via shift-add logic, but suffers significant accuracy degradation at low bitwidths due to its coarse base-2 quantization grid. We introduce Fractional PoT (FPoT), a base-$\sqrt{2}$ (half-octave) fractional PoT grid that achieves practical 4-bit weight quantization while preserving a fully integer shift-add datapath. The method combines (i) the base-$\sqrt{2}$ weight grid with uniform integer activations, (ii) a calibration-time grid-alignment refinement absorbed into the static per-channel scale, and (iii) a lightweight 1-adder $\sqrt{2}$ approximation whose error is absorbed during weight calibration via approximate-grid quantization, yielding a processing element (PE) with significantly fewer gates than a 4-bit integer multiplier. On Llama-3-8B with 4-bit weight and activation quantization, FPoT improves zero-shot commonsense reasoning performance by 8.72% relative to the PoT baseline, while maintaining performance close to the uniform integer baseline, with only a negligible 0.4%p degradation. These results hold across various configurations spanning seven models and three bit-widths. Furthermore, FPoT can be integrated with state-of-the-art LLM PTQ methods, demonstrating framework-agnostic applicability.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Sunghyun Wee, Geunjae Choi, Hyeonjin Kim, Suyoung Kim, Nojun Kwak
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
