---
title: "PEEK: Predictive Queue-Informed KV Cache Management for LLM Serving"
description: "We present PEEK, a lightweight scheduling and eviction framework for both online (streaming) and offline (batch) LLM serving; this paper focuses on the online regime."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2607.02525) · [PDF](https://arxiv.org/pdf/2607.02525)

## 一句话摘要

We present PEEK, a lightweight scheduling and eviction framework for both online (streaming) and offline (batch) LLM serving; this paper focuses on the online regime.

## 为什么值得关注

待编辑增强。

## 摘要原文

We present PEEK, a lightweight scheduling and eviction framework for both online (streaming) and offline (batch) LLM serving; this paper focuses on the online regime. PEEK maintains an incremental radix tree over the pending queue, exposing prefix-sharing clusters no existing engine surfaces. A low-overhead dual-walk matches the tree against the engine's prefix cache to yield longest-prefix-match for every waiting request; PEEK then admits cluster pioneers first so siblings inherit the freshly cached prefix, a co-designed eviction hook protects blocks ancestral to queued demand, and a multi-lane stride scheduler bounds starvation. On SGLang and vLLM across five workloads up to 4$\times$H100 (DP=2 over TP=2), PEEK delivers up to 3.0$\times$/2.6$\times$ cache hit, 7.9$\times$/7.1$\times$ TTFT, 6.7$\times$/5.5$\times$ E2E, and 3.6$\times$/4.5$\times$ throughput gains over each engine's strongest stock baseline (SGLang/vLLM), while matching baselines within noise on workloads with no exploitable prefix structure. Wins hold as KV-cache pressure and inference parallelism scale.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bing Xie, Zhipeng Wang, Masahiro Tanaka, Zhen Zheng
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
