---
title: "What Matters for NVFP4 Training? A Comparative Study of Low-Precision Pretraining Recipes"
description: "Training large language models directly in 4-bit floating-point (FP) formats promises substantial improvements in throughput and energy efficiency."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.24343) · [PDF](https://arxiv.org/pdf/2610.24343)

## 一句话摘要

Training large language models directly in 4-bit floating-point (FP) formats promises substantial improvements in throughput and energy efficiency.

## 为什么值得关注

待编辑增强。

## 摘要原文

Training large language models directly in 4-bit floating-point (FP) formats promises substantial improvements in throughput and energy efficiency. While some recipe design choices have been validated at scale, many promising approaches remain untested beyond small models and short token horizons, leaving open the question of which trends will hold. We present a systematic comparison of recent NVFP4 recipes at medium model scale, evaluating dense 8B and 30B-A3B MoE models trained for up to 1T tokens, with a focus on which ingredients are necessary for accuracy recovery. We propose a final recipe grounded in the principles behind established stable NVFP4 training at scale, incorporating state-of-the-art techniques such as unbiased gradient estimation with lower quantization error than stochastic rounding. To the best of our knowledge, this is the strongest FP4 training result demonstrated at this scale to date in loss gap to BF16. Through ablation studies, we find that: (i) each technique in the optimized recipe measurably improves loss trajectory, (ii) selective high-precision layers are necessary for recovering accuracy at scale, (iii) not all tensors in the backward pass benefit equally from de-biasing, leaving room to apply complementary error-reduction techniques to the remaining tensors.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Anjulie Agrusa, Andrei Panferov, Elizabeth Wei, Keith Wyss, Paul Gibbons, Erik Schultheis, Jinhang Choi, Frank Sun, Tijmen Blankevoort, Dan Alistarh
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
