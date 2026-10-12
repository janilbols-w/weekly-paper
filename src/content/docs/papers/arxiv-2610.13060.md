---
title: "KV-Repurpose: A Testbed for Evaluating Non-Prefix KV-Cache Reuse"
description: "KV-cache reuse in large language model serving is commonly limited to exact prompt prefixes, preventing reuse when the same retrieved document appears after different system prompts, conversation histories, or dynamic metadata."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.13060) · [PDF](https://arxiv.org/pdf/2610.13060)

## 一句话摘要

KV-cache reuse in large language model serving is commonly limited to exact prompt prefixes, preventing reuse when the same retrieved document appears after different system prompts, conversation histories, or dynamic metadata.

## 为什么值得关注

待编辑增强。

## 摘要原文

KV-cache reuse in large language model serving is commonly limited to exact prompt prefixes, preventing reuse when the same retrieved document appears after different system prompts, conversation histories, or dynamic metadata. We present KV-Repurpose, an open-source, vLLM-based system for developing and evaluating segment-wise KV-cache reuse beyond exact prefixes. The system combines cache-aware segment scheduling, prompt construction, capacity management, workload generation, and runtime monitoring. Experiments on long-context benchmarks show that naive segment reuse largely preserves output quality for single-document question answering and summarization, while exposing clear limitations in cross-document reasoning. Under a Zipfian RAG-style workload in which 20% of requests share a fixed prefix, KV-Repurpose achieves a substantially higher token-level cache hit rate than prefix caching at the same 30 GB cache capacity, 63.9% versus 3.3%, resulting in lower TTFT. Even with 1 TB of cache capacity, prefix caching reaches only a 17.9% hit rate in this workload. Source code is available under the Apache-2.0 license at https://github.com/taiga333/eval-kv-repurpose.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache, prefix caching
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Taiga Ikeda, Daisuke Miyashita, Jun Deguchi
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/taiga333/eval-kv-repurpose](https://github.com/taiga333/eval-kv-repurpose)
- 阅读深度：metadata
