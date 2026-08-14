---
title: "Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training"
description: "Optimizer state is the largest single line item in the memory budget of mixture-of-experts (MoE) training."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2607.19058) · [PDF](https://arxiv.org/pdf/2607.19058)

## 一句话摘要

Optimizer state is the largest single line item in the memory budget of mixture-of-experts (MoE) training.

## 为什么值得关注

待编辑增强。

## 摘要原文

Optimizer state is the largest single line item in the memory budget of mixture-of-experts (MoE) training. On a 6.78B-parameter MoE language model AdamW keeps 50.6 GB of first and second moments to update 12.6 GB of bfloat16 weights. We study SkewAdam, an optimizer built on the observation that the three parameter populations of an MoE differ enough in size and gradient statistics that they should not receive the same state. Those populations are the dense backbone, the experts and the router. SkewAdam keeps float32 momentum plus a factored second moment for the backbone (5% of parameters), a factored second moment alone for the experts (95%) and an exact second moment for the router (<0.01%). The resulting state occupies 1.29 GB or 2.6% of AdamW's and peak training memory falls from 81.4 GB to 31.3 GB, within the budget of a 40 GB accelerator. In a controlled comparison from identical initializations over 82M tokens, SkewAdam reaches validation perplexity 108.4, ahead of AdamW (126.8), Muon (120.2) and Lion (393.7), and settles router load balance to within 1% of its uniform floor. The allocation is not what earns that perplexity. A tier ablation reaches the same value while carrying twenty times the state, so the tiers buy memory rather than accuracy. Same-platform runs separate what does earn it. Removing momentum costs 31 perplexity points (tuned Adafactor, 139.7) and replacing the factored second moment and its update clipping with a full second moment costs 10 (tuned AdamW, 118.5), so neither tuned baseline reaches the untuned tiered policy. Where optimizer state lives, these results suggest, matters at least as much as how much of it there is.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Nuemaan Malik
- 发布：2026-08-14；更新：2026-08-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
