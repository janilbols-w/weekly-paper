---
title: "ATMA: Long-Context Language Modeling via Polar Attention and Gated-Delta Compression Memory"
description: "Length extrapolation in language models involves competing objectives: retrieval fidelity, long-document likelihood, short-context quality, and inference cost."
---

**评分：48/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2606.25156) · [PDF](https://arxiv.org/pdf/2606.25156)

## 一句话摘要

Length extrapolation in language models involves competing objectives: retrieval fidelity, long-document likelihood, short-context quality, and inference cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

Length extrapolation in language models involves competing objectives: retrieval fidelity, long-document likelihood, short-context quality, and inference cost. We present ATMA, a 378M-parameter hybrid recipe that combines Polar Attention with gated-delta recurrent memory, and study these objectives as a Pareto problem rather than claiming general architectural dominance. Polar Attention separates a normalized direction channel from a bounded participation-ratio magnitude channel. We select the recipe with a complete 120-cell, 1B-token factorial sweep, then train matched NoPE, RoPE, and Polar variants for 9.816B tokens at length 2K and evaluate them through 256K. Across the factorial, memory improves Polar's 64K retrieval score in all 20 matched cells (mean +47.8 points), whereas its effect on NoPE is small and inconsistent. At 256K, Polar retains 34.4% teacher-forced target-token accuracy and 9.0% exact five-token accuracy; exact retrieval is 18.0% on synthetic contexts but 0.0% on FinePDFs contexts. Polar also limits mean fixed-target bits-per-byte degradation to 1.26 times, at a 1.9-point mean cost on eight short-context tasks. Raven baselines lead BABILong and have length-independent decode state, illustrating a different point on the frontier. Finally, a post-hoc checkpoint audit shows that nearly identical 2K validation curves can conceal a 6.70-nat difference at 256K. Because those runs were neither seed-paired nor randomized across devices, we interpret this as checkpoint variability associated with an infrastructure transition, not a causal hardware effect. Code: https://github.com/kreasof-ai/atma

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Habibullah Akbar
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/kreasof-ai/atma](https://github.com/kreasof-ai/atma)
- 阅读深度：metadata
