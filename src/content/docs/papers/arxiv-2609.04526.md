---
title: "Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs"
description: "Merging a LoRA adapter into its base model is standard deployment practice: it removes the runtime adapter's per-forward overhead and leaves a single standalone checkpoint any serving stack can load."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.04526) · [PDF](https://arxiv.org/pdf/2609.04526)

## 一句话摘要

Merging a LoRA adapter into its base model is standard deployment practice: it removes the runtime adapter's per-forward overhead and leaves a single standalone checkpoint any serving stack can load.

## 为什么值得关注

待编辑增强。

## 摘要原文

Merging a LoRA adapter into its base model is standard deployment practice: it removes the runtime adapter's per-forward overhead and leaves a single standalone checkpoint any serving stack can load. On a native 4-bit microscaling checkpoint (NVFP4, MXFP4) that step stops being free. The merged weights must be written back through a quantizer, which re-derives the checkpoint's discrete E2M1 code plane (roughly 90% of the artifact's bytes), so the deployed artifact becomes coupled to one quantization convention, and every later code-touching event in its lifecycle can move it. Done naively the step is worse than fragile: it deletes the adaptation, by up to 39 pp, because against an already-on-grid base the reconstruction optimum is that base. Scale-QLoRA instead adapts only the native per-block scale field, trains those scales on the deployment grid, and freezes every E2M1 code. Within a fixed native format, scale grid, block layout and code plane, merging is then a bit-exact identity and the merged artifact is code-invariant. Across four models and four tasks, Scale-QLoRA and merge-aware QAT-LoRA are both accuracy-lossless, so we claim no accuracy ordering between them; they differ structurally, in that QAT-LoRA re-derives the code plane through a quantizer while Scale-QLoRA preserves it exactly. That difference is what the lifecycle prices: nearest-rounding implementations disagree by about a point on the measured task, and more extreme rule mismatches can drive the weight-space artifact to ~0%, which we report as a sensitivity bound rather than a deployment frequency. Preserving the code plane also drops the weight-space straight-through estimator from training (3.9x per step on the dense 8B model) and enables exact rollback, code-plane deduplication, and a ~125x faster scale-only task swap.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 8 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: microscaling, quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Tung-Ling Li, Jiale Huang, Lee-Chi Wang, Janaki Ram Gotei
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
