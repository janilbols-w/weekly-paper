---
title: "Written as a Record, Read as an Address: What a Forward Pass Leaves in an Operation's KV Cache"
description: "When a language model reads an operation such as \"Swap the contents of Box F and Box B\", its forward pass writes keys and values for those tokens into the KV cache."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.24635) · [PDF](https://arxiv.org/pdf/2609.24635)

## 一句话摘要

When a language model reads an operation such as "Swap the contents of Box F and Box B", its forward pass writes keys and values for those tokens into the KV cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

When a language model reads an operation such as "Swap the contents of Box F and Box B", its forward pass writes keys and values for those tokens into the KV cache. Prior work on entity tracking establishes what models use: bindings are resolved at query time rather than stored as explicit latent state. We ask what they write at the operation span and how it is accessed. We split a forward pass into a frozen writer and a reader: the writer's cache is recomputed without gradients, while the reader sees only the instruction and operation tokens, with all state descriptions hidden, and is trained in isolation. Anything the reader recovers was therefore already present in the unmodified cache. On a synthetic boxes task, a base reader recovers $\leq 0.06$ of queried bindings against $0.75$--$1.00$ after training, and recoverability tracks the operation's read/write footprint. We find two modes of access. Across Llama-3.1-8B and Mistral-7B, operation-span transplants causally redirect which visible state is read even when the two worlds hold identical values, revealing a routing record. Isolation training preserves routing and adds direct access to the payload, the value the operation read, from the single operand-name token in a narrow mid-depth band (layers 12--15 of 32 in Llama-3.1-8B, 14--17 in Mistral-7B) --- the same site that holds the routing record. The same recipe extends to further operations, ToMi and GSM8K, but is bounded by training coverage and costs open-book accuracy. Operation tokens thus leave localized, causally recoverable records that support both routing and direct payload access, though the model that writes them reads mainly the address they carry and not the value.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lingfeng Wu, Behzad Shomali
- 发布：2026-09-22；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
