---
title: "LayerRoute: Adaptive Layer-Skipping with LoRA-Preserved Quality for Efficient LLM Inference"
description: "We introduce LayerRoute, a parameter-efficient method for adaptive transformer layer-skipping that combines per-layer hard-gated routing (trained via a straight-through estimator) with joint LoRA fine-tuning."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.13682) · [PDF](https://arxiv.org/pdf/2609.13682)

## 一句话摘要

We introduce LayerRoute, a parameter-efficient method for adaptive transformer layer-skipping that combines per-layer hard-gated routing (trained via a straight-through estimator) with joint LoRA fine-tuning.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce LayerRoute, a parameter-efficient method for adaptive transformer layer-skipping that combines per-layer hard-gated routing (trained via a straight-through estimator) with joint LoRA fine-tuning. LayerRoute augments each of the 24 transformer blocks in Qwen2.5-0.5B-Instruct with a lightweight per-layer router (~21.5K parameters) and LoRA adapters (rank 8, ~1.08M parameters), training both jointly under a gate-regularized language-modeling objective. Across 10 independently-seeded training runs, LayerRoute converges to an identical skip-pattern structure in every run - a consistent set of 9 middle layers (8-16) becomes skip-eligible in all 10 seeds - and delivers genuine, verified wallclock speedup in every run (1.02x-1.06x, mean 1.04x). Quality is preserved or improved in every configuration tested: joint LoRA adaptation yields a perplexity improvement over the unmodified backbone in all 10 seeds (mean delta = -1.16 and -1.11 across the two evaluation splits used). We further verify the router performs genuine, non-trivial per-input computation: gate decisions in skip-eligible layers change the actual skip/run outcome for 87-100% of held-out samples, confirming real input-dependent routing rather than a fixed pruning pattern. LayerRoute trains in under 7 minutes on a single A100 and adds negligible overhead beyond the routing decision itself. We report our full reproducibility methodology, including a systematic diagnostic investigation into what determines the router's per-input decisions, as part of this work.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Prateek Kumar Sikdar
- 发布：2026-09-12；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
