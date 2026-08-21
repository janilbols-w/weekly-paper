---
title: "Phantom Gains: Auditing Self-Improvement Against a Measured Null"
description: "Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses."
---

**评分：46/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.20290) · [PDF](https://arxiv.org/pdf/2608.20290)

## 一句话摘要

Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses.

## 为什么值得关注

待编辑增强。

## 摘要原文

Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses. Tracking these transitions means differencing two noisy estimates, leaving them vulnerable to measurement artifacts. Auditing three rounds of rank-$32$ LoRA self-training on Qwen3-8B against a frozen control pushed through the identical pipeline, we identify seven measurement failures, each of which inverts a reported finding when its control is absent. Several are standard practice. A ledger built on a single greedy decode manufactures capability changes on an untrained model, largely an artifact of inference batching; the expansion statistic separating acquisition from sharpening assigns that same model a rate of $0.280$. The natural threshold repair does not survive replication: estimated across the frozen comparisons such a design already contains, its null stays non-zero. We replace it with a per-problem exact test against a pooled baseline under false-discovery-rate control, which detects nothing on any held-out replicate and is unchanged under the multiple-testing rule, error rate and pool size. Applied to a ladder of arms matched in stream, volume and evaluation, the audit finds that external distillation improves problems the base model rarely reaches while three forms of self-training do not; a regression rejects this asymmetry as a by-product of distillation's larger overall gain ($p < 10^{-8}$). On the far smaller set of problems the base model never reaches, the evidence is inconclusive, while self-training corrupts problems solved at baseline at rates well above the measured floor. Transition-level auditing therefore requires a separately measured null for every statistic it reports: nulls that cost no new experiments, built from baseline replicates a multi-arm study already owns, though not from as few as most possess.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 8 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Cheng Xu, Nan Yan, Liming Chen, M-Tahar Kechadi
- 发布：2026-08-20；更新：2026-08-21
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/chengxuphd/phantom-gains](https://github.com/chengxuphd/phantom-gains)
- 阅读深度：metadata
