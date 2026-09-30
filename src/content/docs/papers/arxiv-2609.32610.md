---
title: "KV-Lingo: Learning KV-Cache Translators with Distillation"
description: "Large language models represent context with a key-value (KV) cache."
---

**评分：47/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.32610) · [PDF](https://arxiv.org/pdf/2609.32610)

## 一句话摘要

Large language models represent context with a key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models represent context with a key-value (KV) cache. Caches are model-specific: for the same text, models with different architectures or weights produce incompatible representations. This makes it costly to switch models over a shared context: although the context has already been processed by one model, the incoming model must process it again to build its own cache. We introduce KV-Lingo, a method for translating the KV cache of a source model into one that can be read by a target model. KV-Lingo consists of a collection of linear maps, typically one per layer of the target model, that are applied independently on all tokens' key and value representations. We train these maps using distillation, minimising the divergence between the target model's predictions from its native cache and those from the translated cache. We consider several model pairs spanning multiple sizes and architectures, training one translator per pair on a generic text corpus. The resulting translators preserve strong downstream performance in both small-to-large and large-to-small transfers. Since a switch then costs a linear map and a single decoding step instead of a prefill, replacing re-prefill with cache translation reduces the time to first token after a model switch by 9.6x already on a 64-token prompt for Qwen models on an Apple M3 Ultra, and by up to 29x at 32k context length on an H100. These gains make KV-Lingo particularly useful for dynamic model routing: a context can be processed by one model and handed off to another only when needed, without re-prefilling the shared prefix. We finally show that KV-Lingo can be used for seamless model switching, staying close to re-prefill across repeated switches in our multi-turn evaluations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Val\'erie Castin, Keitaro Sakamoto, Anastasiia Filippova, Jo\~ao Monteiro, Marco Cuturi, Pierre Ablin
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
