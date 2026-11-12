---
title: "ForeSpark: Joint Draft and Verification Budget Scheduling for Parallel Speculative Decoding"
description: "Parallel drafters accelerate LLM decoding by proposing a whole block of draft tokens in a single forward pass, making them attractive for LLM serving."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.13442) · [PDF](https://arxiv.org/pdf/2611.13442)

## 一句话摘要

Parallel drafters accelerate LLM decoding by proposing a whole block of draft tokens in a single forward pass, making them attractive for LLM serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

Parallel drafters accelerate LLM decoding by proposing a whole block of draft tokens in a single forward pass, making them attractive for LLM serving. Recent systems optimize goodput (i.e., accepted tokens per second) because rejected drafts steal compute from other requests. However, these systems control only how many tokens are verified, so every request still drafts a full block. At high serving load, we find that drafting consumes up to 40% of step time, of which a majority is discarded because it is never verified. Yet, draft-length control from autoregressive drafters does not carry over, because a parallel drafter commits to its length before its single pass. Moreover, draft and verification lengths are coupled across the batch, so they must be selected jointly for every request while keeping the decision computationally cheap at every step. In this paper, we propose work-conserving speculation (WCS), a design that jointly allocates draft and verification budgets per request in LLM serving, and present ForeSpark as its prototype. ForeSpark realizes WCS with (i) a context-aware pre-draft estimator that predicts acceptance for every candidate length from the target model's context features, (ii) a lightweight joint draft-verify scheduler that selects both lengths through a global sort, and (iii) a post-draft budget distribution that spends verification on the most promising tokens. Implemented on vLLM, ForeSpark improves throughput by up to 1.77x over the state-of-the-art DSpark and by 2.49x over autoregressive decoding at a matched per-request generation rate, without changing the output distribution. It also tolerates higher load, sustaining up to 1.51x the request rate of DSpark under latency service level objectives (SLOs).

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jaeyong Song, Daniel Wang, Pratyush Patel, Jonny Kong, Preyas Shah, Shobhit Kanaujia
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
