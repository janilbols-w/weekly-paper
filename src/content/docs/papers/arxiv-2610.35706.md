---
title: "TriTile: Three-Tier Attention for Video Diffusion Transformers"
description: "Attention over tens of thousands of visual tokens dominates the inference of video diffusion transformers (DiTs)."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.35706) · [PDF](https://arxiv.org/pdf/2610.35706)

## 一句话摘要

Attention over tens of thousands of visual tokens dominates the inference of video diffusion transformers (DiTs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention over tens of thousands of visual tokens dominates the inference of video diffusion transformers (DiTs). Existing methods reduce this cost through sparsity, low precision, or both, but use a single precision for all kept tiles. We observe that the output error introduced by approximation varies widely across tiles. Many tiles can be skipped with little error, others must be computed but gain little beyond low precision, and a few retain substantial error even at low precision. We present TriTile, a training-free attention method that assigns each tile one of three approximation tiers: skipping it by replacing it with its block means, skimming it in NVFP4, or refining it with NVFP4 residual correction. A lightweight router predicts each tile's error under each tier from block statistics and spends extra compute on a tile only where it removes enough error; a single knob, a price on compute, controls the whole speed-quality trade-off. A fused kernel executes all three tiers in a single pass on the FP4 tensor cores. Over dense FlashAttention, TriTile speeds up generation by 1.38-1.83x on Wan2.2 at 23.0-27.6 dB PSNR, 2.28-2.32x on HunyuanVideo at 34.5-36.0 dB, and 1.84x on LTX-2.5 at 34.1 dB, and in every setting it Pareto-dominates every baseline in speed and PSNR.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp4, low precision
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yeonjae Kim, Omin Kwon, Seong Hoon Seo, Jae W. Lee
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
