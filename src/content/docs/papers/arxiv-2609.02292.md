---
title: "SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology"
description: "The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level."
---

**评分：41/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.02292) · [PDF](https://arxiv.org/pdf/2609.02292)

## 一句话摘要

The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid proliferation of large language models (LLMs) and the growing diversity of their applications presents a unique optimization opportunity: selecting the right model for the task, while optimizing for speed, cost, and quality at a per-task level. However, inference endpoints can vary widely in quality, price, latency, context support, tool use, domain expertise, and reasoning behavior. This heterogeneity makes manual heuristics difficult to maintain and unlikely to achieve consistently favorable speed--cost--quality trade-offs on their own. We introduce \router{}, a lightweight GLiClass-based router that assigns a suitability score to each inference-time model label without autoregressive generation. The released 0.6B-parameter checkpoint combines a Qwen3 decoder with a shallow bidirectional scorer. Its decoder-KV execution path preserves a text-only key--value cache across a session, encodes only new dialogue turns, and evaluates transient candidate-label tokens without adding them to the persistent cache. The same checkpoint also predicts task type, difficulty, reasoning mode, and expected output length, and supports custom zero-shot labels. For task generation, we construct a task ontology with 23 families, 115 task types, 345 routable subtypes, 1,173 synthetic examples, and an orthogonal axis of 30 domains. Using this structure, we generate 150,000 verifier-scored tasks and 15,000 open-ended tasks. We then train the Qwen3 decoder on these tasks, while explicitly separating learned request prediction from per-task policies for attributes such as eligibility, cost, cache reuse, safety, and sovereignty. Across six LiveBench subsets, the router outperforms the mean candidate; on the selected 1,000-task subset, it achieves an aggregate top-1 score of 0.707 versus 0.696 for the strongest fixed model, with benchmark-dependent gains.

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

- 作者：Ihor Stepanov, Aleksandr Smechov, Mykhailo Shtopko, Dmytro Vodianytskyi, Oleksandr Lukashov
- 发布：2026-09-02；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
