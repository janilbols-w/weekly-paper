---
title: "REAL Loss: Optimizing Real Expected Acceptance Length for Speculative Decoding"
description: "Speculative decoding accelerates LLM inference by having a draft model propose multiple tokens for the target model to verify in one pass."
---

**评分：49/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.14399) · [PDF](https://arxiv.org/pdf/2611.14399)

## 一句话摘要

Speculative decoding accelerates LLM inference by having a draft model propose multiple tokens for the target model to verify in one pass.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates LLM inference by having a draft model propose multiple tokens for the target model to verify in one pass. The speedup is governed by the expected acceptance length (EAL), yet standard training objectives such as cross-entropy, KL divergence, and total variation focus only on distribution matching or single-step overlap. Recent studies instead propose block-level training objectives, aiming to optimize EAL directly. However, these objectives remain surrogates rather than exact formulations of EAL. For example, some average later acceptance over target-distributed continuations rather than the verification branches selected by accepted tokens, introducing a covariance gap that can reverse the gradient direction. We analyze this gap and derive REAL, a real EAL training loss that uses path weights for unbiased estimation and Rao-Blackwellization for variance reduction. In a controlled loss-level comparison with a Qwen3.6-35B-A3B target and a Domino drafter, REAL outperforms WTV, VSD, DBLast, and the static LK baseline on probabilistic serving acceptance length across 9 task subsets and 5 evaluation seeds. These gains require only a change to the training loss, with no modification to the drafter architecture or inference procedure, demonstrating the practicality of real EAL training. A reference implementation of the REAL loss is available at https://github.com/King-ty/speculators/tree/real-loss.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Yu Tian
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/King-ty/speculators/tree/real-loss](https://github.com/King-ty/speculators/tree/real-loss)
- 阅读深度：metadata
