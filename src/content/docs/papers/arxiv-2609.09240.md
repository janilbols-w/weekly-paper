---
title: "Scaling Post-Training Ternarisation to Qwen3-8B Capability Retention, Reproduction, Lossless Packing, and Packed Execution"
description: "Ultra-low-bit language models promise reductions in storage and memory traffic, but a nominal \"1.58-bit\" label does not specify the deployed representation or its execution cost."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.09240) · [PDF](https://arxiv.org/pdf/2609.09240)

## 一句话摘要

Ultra-low-bit language models promise reductions in storage and memory traffic, but a nominal "1.58-bit" label does not specify the deployed representation or its execution cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Ultra-low-bit language models promise reductions in storage and memory traffic, but a nominal "1.58-bit" label does not specify the deployed representation or its execution cost. We study a scale-up of an aggressive post-training conversion pipeline from Qwen3-4B to Qwen3-8B. The conversion uses KOTMS rotation, E2M-ATQ adaptive ternarisation, and GPTQ-style error compensation in a weight-only A16 configuration. We do not claim these algorithms as new. Our contribution is the end-to-end scale-up characterisation: an external reproduction gate, matched 4B/8B capability analysis, cross-corpus perplexity, effective-bit accounting, lossless lattice-aware packing, and direct packed execution. The 8B model reaches a three-corpus perplexity ratio of 1.361x, with WikiText-2, C4, and PTB ratios of 1.318x, 1.393x, and 1.371x. On eight zero-shot tasks at n = 500, mean accuracy is 64.6% versus 72.4% for FP16, corresponding to 78.5% chance-corrected retention and a 7.8-point absolute cost. The matched 4B run retains 69.6%, yielding an 8.9-point 8B advantage. The packed checkpoint is 8.24 GiB and preserves the recorded perplexity to measurement precision. Direct packed execution reaches 15.52 tokens/s in 7.35 GiB, while a preliminary packed GEMV remains slower than FP16 cuBLAS. The result is a validated scale-up baseline: model size improves robustness to aggressive post-training discretisation, actual serialisation is solved for the measured artefact, and direct execution is feasible, while broader seeds, calibration distributions, and kernel optimisation remain open.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Anirudh Malik, M Sparsh Mehra, Poojith Devan
- 发布：2026-09-08；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
