---
title: "HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks"
description: "Large language models leak parametric knowledge of what followed a historical date into decision tasks indexed by that date -- not necessarily a lookup of the realized outcome, but knowledge of the period all the same."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.18867) · [PDF](https://arxiv.org/pdf/2607.18867)

## 一句话摘要

Large language models leak parametric knowledge of what followed a historical date into decision tasks indexed by that date -- not necessarily a lookup of the realized outcome, but knowledge of the period all the same.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models leak parametric knowledge of what followed a historical date into decision tasks indexed by that date -- not necessarily a lookup of the realized outcome, but knowledge of the period all the same. Existence is settled; what users lack is a cheap way to audit a given model. We present HindsightBench, a black-box audit protocol that profiles parametric hindsight in any time-indexed LLM decision task at probe-level cost (no backtests, no logprobs, no corpus access). It chains a four-arm date-manipulation matrix (revealed/date-only/masked/transplanted), dual memory probes (date recovery; outcome recall), and six metrics -- trigger strength, transplant effect, post-cutoff placebo, recoverability, behaviorally effective cutoff, and recall-accuracy dissociation -- with explicit gates where identifiability is data-dependent. Applied to 15 models from seven vendors on a 258-node vintage-correct macro panel, it yields three patterns: (i) the date-trigger reflex is not a scale phenomenon -- it tracks training recency, though what installs it is not identified here: absent across every 2024 open-weight row where it is measurable, including a 70B tier with cutoff-aligned recall propensity, present in every tested 2026-generation model, and switching on within one vendor lineage (Qwen3 -> Qwen3.6) in the same MoE family at ~3B active; (ii) effective cutoffs span 22 months across vendors and precede vendor-reported dates by up to eight months, invalidating calendar-window placebos; (iii) results are not invariant to serving -- BF16 serving of an FP8-referenced model breaks the trigger estimate's stability while AWQ-INT4 preserves it, and a provider-locked reasoning regime makes one probe non-convergent -- so the protocol pins quantization and thinking regime as part of its contract. We release the panel, preregistrations, audit rows, transcripts, and one-command regeneration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8, int4, quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Haozhe Jia
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
