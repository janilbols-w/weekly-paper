---
title: "When Uncertainty Isn't Enough: An Empirical Study of Self-Correction in Code Generation"
description: "Large language models for code generation often produce incorrect solutions without reliable indicators of failure."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.14659) · [PDF](https://arxiv.org/pdf/2608.14659)

## 一句话摘要

Large language models for code generation often produce incorrect solutions without reliable indicators of failure.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models for code generation often produce incorrect solutions without reliable indicators of failure. We study whether uncertainty estimation methods developed for natural language transfer to code generation, and whether such signals can improve code generation via selective self-correction. We evaluate five uncertainty methods: mean token entropy, verbalized confidence, $P(\text{True})$, entropy ensembles, and semantic entropy probes, across three small code LLMs on HumanEval and BigCodeBench. We find that multi-sample $P(\text{True})$ achieves the strongest correlation with correctness, while all the other methods, including semantic entropy probes, yield only weak correlation. We then use these uncertainty signals to drive three self-correction policies: adaptive decoding, uncertainty-based regeneration, and verification-based regeneration. Our results reveal a stronger negative finding than anticipated: uncertainty-based self-correction fails to reliably improve Pass@1, degrading accuracy in 5 of 6 configurations across both benchmarks ($-3$pp to $-10$pp), and adaptive decoding degrades accuracy in 4 of 6 configurations. Only verification-based self-correction reliably improves Pass@1, with gains of $+6$ to $+26$ percentage points on HumanEval and $+8$ to $+20$ percentage points on BigCodeBench, scaling inversely with baseline strength. These findings replicate consistently across both benchmarks and suggest that cheap uncertainty estimators are insufficient on their own to improve code correctness, and that their practical value lies in serving as gating signals for costlier execution-based correction loops rather than as standalone substitutes for verification.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Pranav Rakasi, Maanas Lalwani, Arnav Srivastava, Arya Palanivel, Tinuade Adeleke, Ruizhe Li, Sean Wu
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
