---
title: "Physics-Aware Distillation of a Grid Foundation Model for Real-Time Edge Inference"
description: "Grid foundation models (GridFMs) are graph transformers pretrained on a masked power-flow objective, and evaluate power flow orders of magnitude faster than an iterative solver."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.21833) · [PDF](https://arxiv.org/pdf/2610.21833)

## 一句话摘要

Grid foundation models (GridFMs) are graph transformers pretrained on a masked power-flow objective, and evaluate power flow orders of magnitude faster than an iterative solver.

## 为什么值得关注

待编辑增强。

## 摘要原文

Grid foundation models (GridFMs) are graph transformers pretrained on a masked power-flow objective, and evaluate power flow orders of magnitude faster than an iterative solver. Their size, however, targets data-centre inference, whereas low-inertia operation increasingly asks for inference at the edge, next to the measurement, at batch size one and within a single synchrophasor (PMU) reporting frame. We distil a 20.1M-parameter, 12-layer GridFM teacher into a 0.62M-parameter, 6-layer student, a $32.5\times$ parameter reduction at half the message-passing depth, using an objective that combines the masked power-flow loss with output, physics-residual, latent-state and attention transfer. The physics-residual term, which matches the teacher's power-residual profile, has not previously been applied to typed power-grid graphs. We evaluate on a renewable variant of the IEEE 118-bus benchmark grid in which 26 of the conventional (synchronous) generators are replaced by inverter-based renewables with battery flexibility and standardised reactive-power limits (IEEE 1547), giving $97\,529$ physically valid (AC-OPF-feasible) operating scenarios, and we ablate all eight combinations of the transfer terms, reporting accuracy against ground truth and fidelity to the teacher separately. Distillation lowers student error on all four predicted quantities, by up to $48\%$ on active-power dispatch, and every distilled student is more accurate than its teacher on reactive-power dispatch. The gain is largely carried by the output matching term. The physics-residual term, in the layer-aggregated form used here, is consistently harmful, which we attribute to the spatial averaging it applies to a bus-level residual field. The resulting student is $32.5\times$ smaller in parameter count and has half the message-passing depth, making it a candidate for subsequent edge-device benchmarking.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vlad Alexandru Sănduleac, Shahariya Rasheed Rayamarakkarveettil Puthanpurayil, Noman Khan, Remus Teodorescu
- 发布：2026-10-15；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
