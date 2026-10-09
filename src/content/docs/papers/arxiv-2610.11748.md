---
title: "DEX: Digit-Level Early Exit for Energy-Efficient MSDF Neural Network Inference"
description: "U-Net inference for brain-tumor segmentation requires billions of multiply-accumulate operations, motivating hardware that can reduce computation dynamically rather than relying only on fixed precision or static model compression."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.11748) · [PDF](https://arxiv.org/pdf/2610.11748)

## 一句话摘要

U-Net inference for brain-tumor segmentation requires billions of multiply-accumulate operations, motivating hardware that can reduce computation dynamically rather than relying only on fixed precision or static model compression.

## 为什么值得关注

待编辑增强。

## 摘要原文

U-Net inference for brain-tumor segmentation requires billions of multiply-accumulate operations, motivating hardware that can reduce computation dynamically rather than relying only on fixed precision or static model compression. Most-significant-digit-first (MSDF) arithmetic exposes the leading digits of a result during computation, enabling output-dependent decisions before the full value is generated. This paper presents an MSDF accelerator for quantized U-Net segmentation with a two-stage grouped processing element supporting signed INT8 operands and in-stream bias accumulation. Four runtime mechanisms operate directly on the output digit stream: exact early negative detection (END) in ReLU layers, exact sign-only decision making in the segmentation head, calibrated low-order-digit skipping, and calibrated pruning. The two approximate mechanisms are selected offline under an accuracy constraint, while execution requires only lightweight control and does not modify the stored weights. On a residual U-Net trained with nnU-Net for BraTS, the proposed mechanisms reduce digit cycles by 38.38\% while achieving a mean Dice score of 80.58\% on 73 held-out cases, compared with 81.20\% for the floating-point model; the exact mechanisms alone reduce cycles by 18.79\% without altering the quantized output. Synthesized in 45~nm, the processing element operates at 500~MHz, occupies 0.858~mm$^2$, and consumes 0.726~mJ per $192\times192$ patch under switching-activity-annotated power analysis. A projected eight-output accelerator with shared activation delivery achieves 16.6~ms latency and 1.67~mJ per patch.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yousef Sadegheih, Dorit Merhof, Muhammad Usman
- 发布：2026-10-09；更新：2026-10-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
