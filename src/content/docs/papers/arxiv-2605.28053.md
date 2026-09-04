---
title: "RW-TTT: Batched Serving for Request-Owned Test-Time Training State"
description: "Test-time training (TTT) adapts an LLM during generation by reading and updating request-owned state, such as fast weights, low-rank deltas, or streaming learner state."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2605.28053) · [PDF](https://arxiv.org/pdf/2605.28053)

## 一句话摘要

Test-time training (TTT) adapts an LLM during generation by reading and updating request-owned state, such as fast weights, low-rank deltas, or streaming learner state.

## 为什么值得关注

待编辑增强。

## 摘要原文

Test-time training (TTT) adapts an LLM during generation by reading and updating request-owned state, such as fast weights, low-rank deltas, or streaming learner state. This breaks batched LLM serving, which assumes shared static weights: serial execution is correct but slow, while naive batching can corrupt request state. We formulate this problem as read-write TTT serving and present RW-TTT , which tags each decode step with its owner, version, and READ/WRITE effect, batches only compatible phases, and commits updates only to the owner. On one GPU with eight fast-weight InPlace-TTT streams, RW-TTT reaches 274.61 aggregate tok/s, 9.31x over sequential serving and 3.44x over per-stream replicas under the same memory budget. It preserves behavior on RULER, a long-context benchmark, and passes owner/version checks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Jian Yang, Zhizhuo Kou, Yao Tian, Hao Zhang, Han Chen, Sirui Han, Yike Guo
- 发布：2026-09-04；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
