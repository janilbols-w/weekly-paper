---
title: "Taming Speculative Search for Test-Time Scaling in LLM Serving"
description: "Test-time scaling has recently emerged as a powerful approach for improving LLM reasoning by allocating additional computation during inference, substantially enhancing accuracy on challenging tasks such as mathematics and coding."
---

**评分：45/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.39334) · [PDF](https://arxiv.org/pdf/2609.39334)

## 一句话摘要

Test-time scaling has recently emerged as a powerful approach for improving LLM reasoning by allocating additional computation during inference, substantially enhancing accuracy on challenging tasks such as mathematics and coding.

## 为什么值得关注

待编辑增强。

## 摘要原文

Test-time scaling has recently emerged as a powerful approach for improving LLM reasoning by allocating additional computation during inference, substantially enhancing accuracy on challenging tasks such as mathematics and coding. To accelerate the exploration of reasoning paths, recent studies proposed speculative execution. However, we show that supporting speculative execution poses two unique challenges for LLM serving systems: (1) an explosion in the search space of candidate paths and (2) frequent, fine-grained verification tasks for candidates. To address these challenges, this paper proposes SpecScale, a serving system for efficient speculative execution. We introduce three techniques to reconcile the trade-off between latency and computational overhead: (1) early pruning of low-quality candidate paths, (2) deduplicating computation across redundant candidate paths, and (3) deferring fine-grained verification tasks. We evaluate SpecScale on challenging reasoning benchmarks, including MATH and Olympiad. Our results show that SpecScale significantly outperforms both non-speculative and recent speculative approaches, delivering substantial improvements in throughput and latency while preserving answer quality.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jinwoo Jeong (Korea University), Woohyung Choi (Korea University), Myeongjae Jeon (POSTECH), Jeongseob Ahn (Korea University)
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
