---
title: "RoleQ: Role-Aligned Scales for Converting Language Models to Ternary"
description: "Weight quantization below four bits shrinks memory and bandwidth at a perplexity that looks acceptable, but often at the cost of factual knowledge and task accuracy."
---

**评分：38/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.21808) · [PDF](https://arxiv.org/pdf/2610.21808)

## 一句话摘要

Weight quantization below four bits shrinks memory and bandwidth at a perplexity that looks acceptable, but often at the cost of factual knowledge and task accuracy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Weight quantization below four bits shrinks memory and bandwidth at a perplexity that looks acceptable, but often at the cost of factual knowledge and task accuracy. Ternary weights have mostly been obtained by training from scratch or long fine-tuning. We introduce RoleQ, a quantization framework that places scales by the functional roles of Transformer units rather than by the layout of the weight matrix, as conventional formats do. Vectors that read from the residual stream take one scale per output unit; those that write to it, one per input unit. The rule is structural, needs no search, calibration or stored state, and holds on integer and ternary grids. In a rotated basis it matches a per-layer axis search at half the solver work, and at ternary it cuts perplexity by up to half against layout-based placement in two families at every size from 0.6B to 14B, where per-row scales leave MMLU at chance. Our lightweight post-training pipeline converts an existing checkpoint to 1.59 bits per weight in a few GPU-hours, a fraction of the cost of learned ternarization, and leads every post-training ternary method at matched or lower memory-resident bits on perplexity, zero-shot accuracy and MMLU, most widely on knowledge. A sparse second ternary plane placed by a per-unit Fisher saliency keeps the matmul multiplication-free and recovers what ternary loses first: at 8B, a fraction of a bit returns about half the MMLU that conversion costs, well ahead of random or Hessian-based placement at equal bits.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Johannes Knittel, Alec Helbling, Hanspeter Pfister
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
