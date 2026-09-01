---
title: "SALT: Salience-Aware Lexical Trie for Long-Context Compression"
description: "As large language models (LLMs) process increasingly longer prompts, computation and KV-cache memory costs have emerged as major bottlenecks in inference systems."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.17486) · [PDF](https://arxiv.org/pdf/2607.17486)

## 一句话摘要

As large language models (LLMs) process increasingly longer prompts, computation and KV-cache memory costs have emerged as major bottlenecks in inference systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

As large language models (LLMs) process increasingly longer prompts, computation and KV-cache memory costs have emerged as major bottlenecks in inference systems. Existing input-level prompt compression methods address this, but rank each sentence by a scalar relevance score, treating the document as an unstructured pool of words and sentences. Under tight budgets, this causes theme collapse, where the dominant theme(s) of a document consumes the budget, discarding less-frequent yet task-relevant themes. Preserving thematic coverage instead requires allocating the budget across recurring themes rather than scoring sentences in isolation. To this end, we propose SALT, a model-agnostic extractive framework that organizes per-sentence keywords into a trie ordered by sentence frequency (SF), a lightweight, reusable proxy for document thematic structure. This trie-based organization smooths memory allocation and prevents dominant themes from monopolizing the budget. Multi-anchor retrieval activates trie nodes labeled by query keywords at any depth, and the trie persists across dialogue turns, supporting multi-turn use without re-encoding the document. By preserving document themes, SALT reduces the prefill computation and memory cost of long-context prompts while remaining composable with KV-cache methods that target decoding-time latency and memory.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Oteo Mamo, Hyunjin Yi, Joydhriti Choudhury, Shangqian Gao, Weikuan Yu
- 发布：2026-09-01；更新：2026-09-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
