---
title: "Match the Distribution, Not the Compute: Post-Training Multi-Token Prediction Heads"
description: "Multi-token prediction (MTP) improves the throughput of autoregressive generation by enabling the language model to draft multiple next tokens per forward pass, while a verification step over draft tokens ensures that token distribution of the backbone is preserved."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.00888) · [PDF](https://arxiv.org/pdf/2610.00888)

## 一句话摘要

Multi-token prediction (MTP) improves the throughput of autoregressive generation by enabling the language model to draft multiple next tokens per forward pass, while a verification step over draft tokens ensures that token distribution of the backbone is preserved.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-token prediction (MTP) improves the throughput of autoregressive generation by enabling the language model to draft multiple next tokens per forward pass, while a verification step over draft tokens ensures that token distribution of the backbone is preserved. Every open MTP-family release (MiMo-7B, DeepSeek-V3, Qwen3) trains its heads jointly with the backbone over the full pretraining run of tens of trillions of tokens, thus setting the drafter quality at pretraining time. We ask whether a lightweight post-training pass on target-generated chain-of-thought is enough to reach the same expected throughput speedup on a frozen reasoning model, and study how a serving-time system built on such a checkpoint can be optimized. We present three findings. 1) On a frozen Qwen3-8B with $K{=}3$ chained MTP heads, we show that a post-training recipe with plain cross-entropy on $\approx\!2.5$B tokens reaches or exceeds the expected speedup of jointly trained MiMo-7B on math, coding and knowledge benchmarks. Our post-training recipe utilizes $10^3$-$10^4\times$ less MTP-training tokens as compared with joint pre-training of MiMO-7B MTP baseline. 2) We propose a chain-aware relaxation of draft token verification rule that allows a bounded drift from backbone language model token distribution. We show that this relaxation lifts expected speedups by $+12$ to $+16\%$ per benchmark while preserving task accuracy. 3) We propose an adaptive controller that dynamically chooses the number of MTP heads to be engaged at inference time and demonstrate recovery of upto $11$--$14\%$ loss in speedup using fixed maximum MTP draft length.

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

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Prachi Badarayani, Aidan Jay, Chenghui Zhou, Dayquan Julienne, Yuan Gao, Tianwei Chen, George Zerveas, Ishmam Zabir, Xiren Zhou, Chris Quirk, Xia Song
- 发布：2026-10-01；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
