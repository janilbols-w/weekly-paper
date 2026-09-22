---
title: "Per-Query Gating of LLM Rerankers for Multi-Hop Retrieval"
description: "LLM rerankers add of the order of \\$0.2-0.3 per 1,000 queries and about a second of tail latency on top of a graph-augmented dense pipeline such as HippoRAG2, and on three multi-hop benchmarks they improve final-hop top-K coverage on seven of nine (dataset, K) cells, by up to +34.8 pp."
---

**评分：40/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.22880) · [PDF](https://arxiv.org/pdf/2609.22880)

## 一句话摘要

LLM rerankers add of the order of \$0.2-0.3 per 1,000 queries and about a second of tail latency on top of a graph-augmented dense pipeline such as HippoRAG2, and on three multi-hop benchmarks they improve final-hop top-K coverage on seven of nine (dataset, K) cells, by up to +34.8 pp.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM rerankers add of the order of \$0.2-0.3 per 1,000 queries and about a second of tail latency on top of a graph-augmented dense pipeline such as HippoRAG2, and on three multi-hop benchmarks they improve final-hop top-K coverage on seven of nine (dataset, K) cells, by up to +34.8 pp. We ask whether a learned per-query gate can skip the reranker where it will not help, using only features available before the LLM call (27 score and lexical statistics of the two retrieval lists plus a PCA of a small query embedding) with an executable fallback. Every choice, including the fallback and the threshold, is made inside the training fold and applied once to held-out queries, and harmful skips (the rerank would have found the target, the fallback did not) are reported next to the aggregate coverage. Across nine cells on 2WikiMultiHopQA, MuSiQue and HotpotQA the gate skips 51% of calls at an average held-out LastHop@K cost of 1.2 pp; four cells meet a pre-registered 1 pp rule, harmful skips occur in eight (190 harmful against 136 beneficial), and a random gate at the same skip rate loses 2 to 11 pp on the high-lift cells. A second rule sets each cell's threshold from a pre-specified budget on the expected harmful-skip rate over Platt-calibrated harm probabilities (ECE 0.025 after calibration, 0.094 before): at a 1 pp budget the gate skips 42% at -0.8 pp with 66 harmful skips and six cells within 1 pp, but realised harm exceeds the promise in six cells (mean 1.45 vs 0.83 pp), a selection optimism we quantify; a 0.5 pp budget realises about 1 pp. The harm probabilities are calibrated but barely discriminative (AUC 0.16 to 0.70). An earlier version reported 73% "lossless" savings; that figure rested on an oracle fallback and a wrong MuSiQue target, and we document both.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: tail latency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Andre Bacellar
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
