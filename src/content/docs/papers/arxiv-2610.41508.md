---
title: "HiState: Hierarchical Prefix Cache Management for Hybrid LLM Serving in Agentic Workloads"
description: "Hybrid large language models combine full-attention and recurrent linear layers to reduce inference costs."
---

**评分：54/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.41508) · [PDF](https://arxiv.org/pdf/2610.41508)

## 一句话摘要

Hybrid large language models combine full-attention and recurrent linear layers to reduce inference costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid large language models combine full-attention and recurrent linear layers to reduce inference costs. Prefix caching can further reduce redundant computation across requests, but a recurrent checkpoint cannot recover an earlier state corresponding to a shorter prefix. Existing hybrid prefix caching systems retain checkpoints at selected boundaries to support common reuse patterns in conventional conversations. However, agent workloads modify and revisit earlier contexts, exposing reusable prefixes whose checkpoints were never saved or have already been evicted. A straightforward approach is to retain more checkpoints to reduce recomputation, but their cumulative footprint can displace reusable prefixes from other sessions and cause additional cache misses. To address these problems, we present HiState, a prefix cache management system for hybrid models serving agent workloads. Our key observation is that prefix reuse accesses all matching key-value (KV) entries but only one recurrent checkpoint, regardless of how many checkpoints are retained. This asymmetry allows HiState to retain historical checkpoints on SSD while prioritizing fast memory for KV entries: each hit retrieves only one checkpoint whose size is independent of context length. Within this hierarchy, we propose adaptive interval control to balance checkpoint storage against recomputation, and unified eviction to coordinate checkpoint sparsification with reclamation of stale trajectories. We implement HiState on top of vLLM and evaluate it on two public coding-agent trace datasets and controlled microbenchmarks. On real agent traces, HiState achieves up to 5.73x and 5.44x speedups in p99 TTFT over vLLM-Marconi and SGLang-HiCache, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zaifeng Pan, Lucas Wang, Xinwei Qiang, Yanbo Zhou, Chang Chen, Zhengding Hu, Yue Guan, Yufei Ding
- 发布：2026-11-02；更新：2026-11-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
