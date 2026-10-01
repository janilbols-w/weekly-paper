---
title: "Working Around the Compute Ceiling: Byte-Exact Memory in Galahad Makes LLM Reading a One-Time Cost LLM Reading a One-Time Cost"
description: "A transformer language model performs a bounded amount of computation per token, and recent work by Vishal Sikka, former CEO of Infosys, argues that this bound limits which tasks a model can carry out or verify (arXiv:2507.07505)."
---

**评分：41/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.39358) · [PDF](https://arxiv.org/pdf/2609.39358)

## 一句话摘要

A transformer language model performs a bounded amount of computation per token, and recent work by Vishal Sikka, former CEO of Infosys, argues that this bound limits which tasks a model can carry out or verify (arXiv:2507.07505).

## 为什么值得关注

待编辑增强。

## 摘要原文

A transformer language model performs a bounded amount of computation per token, and recent work by Vishal Sikka, former CEO of Infosys, argues that this bound limits which tasks a model can carry out or verify (arXiv:2507.07505). We ask how much of the budget beneath that ceiling is spent on work the model has already done. Serving is stateless across requests: a model that answers a second question about a document recomputes the document's attention state from the first token. On seven real-world datasets, 98.7% of prompt tokens were text the model had already read. We present Galahad, a memory layer for vLLM, SGLang and llama.cpp that makes this reading a one-time cost. Taliesin saves the model's key-value (KV) state for a block of text and loads it on the next request that contains the same bytes, instead of recomputing it. Blaise keeps the documents themselves and passes the model only the section a question needs. On a recall test with 100 facts hidden in a 97,000-token corpus (Gemma 4 31B), Taliesin alone let the model attend to the whole corpus and answered 98 of 100 on llama.cpp at 3.0 s and 572 J per question, against 10 of 100, 9.3 s and 2,754 J for the same model without Galahad, which could hold only the last 12,000 tokens. With Blaise added, the model read about 668 tokens per question and answered 100 of 100 on all three runtimes at 0.59-0.64 s and 200-213 J; a tuned RAGFlow pipeline answered 77. Storing the corpus is a one-time cost of about 100 s and 28 kJ, whose energy is recovered after 13 questions. Restored state is bit-identical: all 262,144 output logits matched after restart, rehydration and hot-load. Galahad worked with all 30 models we tested under vLLM, and it fails closed: any load that does not pass its checks is recomputed. Together these results move LLM serving from stateless to stateful inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sietse Schelpe
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
