---
title: "PRISM: A Geometric Risk Bound for Decomposing Drift into Scale, Shape, and Head"
description: "A single base LLM now comes with dozens of post-training variants, quantized, LoRA-adapted, or distilled, and each has to be checked before release."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2605.11608) · [PDF](https://arxiv.org/pdf/2605.11608)

## 一句话摘要

A single base LLM now comes with dozens of post-training variants, quantized, LoRA-adapted, or distilled, and each has to be checked before release.

## 为什么值得关注

待编辑增强。

## 摘要原文

A single base LLM now comes with dozens of post-training variants, quantized, LoRA-adapted, or distilled, and each has to be checked before release. Existing evaluations provide only a partial picture: benchmark scores and likelihood screens say that a variant has degraded, similarity scores such as CKA and SVCCA say how its features moved, and nothing connects the two. We connect them with one structural fact and one design choice: the prediction head is linear, so feature geometry reaches the loss, and we compare the two feature sets through an orthogonal map, which leaves the geometry being measured unchanged. From these we derive PRISM, a closed-form upper bound on the cross-entropy risk gap between a target model and a proxy variant, and prove that it splits exactly into three measurable axes: scale, shape, and head. Each axis names a failure mode and where to intervene: low-bit quantization distorts shape and, at the lowest bit-widths, also inflates activation scale; quantizing the output embedding inflates the head term, which dominates the bound at high bit-widths. Because the shape term is differentiable, the same geometry becomes a regularizer that curbs catastrophic forgetting more than experience replay. Across two model families and five benchmarks, PRISM ranks quantized and fine-tuned variants from a single forward pass at mean Spearman above 0.8, and eight reference sequences already recover the ranking that the risk gap itself needs over a hundred to reach.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chieh-Yen Lin, Shao-Hua Sun
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
