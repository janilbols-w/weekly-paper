---
title: "How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE"
description: "Directional ablation removes an aligned language model's ability to refuse by projecting a single \"refusal direction\" out of the weights that write the residual stream."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.09793) · [PDF](https://arxiv.org/pdf/2609.09793)

## 一句话摘要

Directional ablation removes an aligned language model's ability to refuse by projecting a single "refusal direction" out of the weights that write the residual stream.

## 为什么值得关注

待编辑增强。

## 摘要原文

Directional ablation removes an aligned language model's ability to refuse by projecting a single "refusal direction" out of the weights that write the residual stream. It needs no gradient-based training and no optimization, only a few hundred contrastive prompts, which makes it the canonical white-box attack on open-weight alignment. However, it has been established only on dense models up to roughly 70B parameters. We study whether it survives the shift to frontier mixture-of-experts (MoE) models whose residual streams are no longer a single tensor and whose weights ship quantized. We apply it to GLM-5.3-Flash (320B parameters, 288 routed experts, a four-wide hyper-connection residual, block-FP8). The attack survives the architecture, but what it reaches is no longer where a reader of the original recipe would look for it. Editing the attention, dense and routed-expert writers on their own removes 0.039, 0.016 and 0.148 of refusal respectively; editing all three together removes 0.776. As a result, 74% of the effect exists only under the joint intervention. The part the conventional recipe reaches by module-name matching accounts for 0.066 of that 0.776, which is why it fails silently on an MoE. The effect does not follow from removing just any direction: ablating a random direction orthogonal to it leaves refusal unchanged. A category-concentrated residue survives every edit we tried: subspaces fitted on violence, sexual content and hate leave measurable refusal at every rank from 1 to 12. We report the method, the 41-89 percentage-point reductions it achieves across seven harmful benchmarks with no detected change in capability, and the boundary where it stops.

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

- taxonomy keywords: fp8, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Shi, Tanyu Chen, Kai Shen
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
