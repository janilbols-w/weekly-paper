---
title: "SACQ: Structure-Aware Codebook Quantization for Ultra-Low-Bit Vision-Language-Action Models"
description: "Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.41408) · [PDF](https://arxiv.org/pdf/2610.41408)

## 一句话摘要

Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-Language-Action (VLA) models enable capable robot behavior, but their large memory footprint limits deployment on resource-constrained robotic platforms. Weight quantization is a natural remedy, yet post-training quantization (PTQ) recipes inherited from large language models degrade when applied to VLAs at ultra-low precision. Existing low-bit PTQ methods often fail to explicitly account for the structure of downstream operations and allocate precision without considering its effect on the policy actions. We introduce SACQ, an ultra- low-bit weight-only vector-codebook quantization framework for VLAs. SACQ combines (1) structure-aware codebook fitting with role-specific quadratic metrics that reflect input statistics and downstream sensitivity; (2) action-aware mixed-bit allocation based on the increase in final-action error as individual layers are compressed; and (3) two-stage post-quantization refinement that reassigns codeword indices with second-order error compensation and calibrates codebooks and row-group scales against the decoded action. Using GR00T N1.7, SACQ achieves 93.85% average success across four LIBERO suites at 1.5 bits per language/action weight while reducing model memory by 4.83x. With INT8 activation quantization and low-precision attention, it retains 93.55% success while running 1.51x faster than BF16. On SimplER, SACQ further achieves 63.76% and 52.27% success under Visual Matching and Variant Aggregation at 2 bits per language/action weight, compared to 58.90% and 53.45% for BF16, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 20 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: int8, low precision, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Haesung Lee, Insu Han
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
