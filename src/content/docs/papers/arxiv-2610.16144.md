---
title: "Hashrope: A Persistent Data Structure for Mechanisms of LLM Context Management"
description: "Serving stacks for large language models manage context through four recurring mechanisms: incremental edits to a growing context, branching and snapshotting for tree search, identification of reusable prefixes for KV-cache reuse, and encoding of repeated segments."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2610.16144v1) · [PDF](https://arxiv.org/pdf/2610.16144v1)

## 一句话摘要

Serving stacks for large language models manage context through four recurring mechanisms: incremental edits to a growing context, branching and snapshotting for tree search, identification of reusable prefixes for KV-cache reuse, and encoding of repeated segments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Serving stacks for large language models manage context through four recurring mechanisms: incremental edits to a growing context, branching and snapshotting for tree search, identification of reusable prefixes for KV-cache reuse, and encoding of repeated segments. Each mechanism is served today by a different specialist structure. We show that all four reduce to a single persistent weight-balanced rope whose every node carries a polynomial hash of its subtree over a Mersenne prime, so that the structure supports logarithmic edits and logarithmic verified content-identity queries at the same time. We validate each mechanism with pre-registered, replicated experiments, then compare against a deployed specialist per mechanism: the Ropey editing library, a faithful PagedAttention copy-on-write block table, and the vendored SGLang radix matcher. On workloads that interleave edits with identity queries, Hashrope is net-superior to Ropey by a factor that grows without bound (369.7x at one million characters). Against the radix matcher on a live vLLM stack serving Qwen2.5-7B-Instruct-1M on four A100 GPUs, Hashrope identifies a one-million-token shared prefix exactly and 1.20x faster, at a context length the dense engine cannot even prefill.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Muntaser Syed, Ameerah Alsulami, Marius Silaghi
- 发布：2026-10-12；更新：2026-10-12
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
