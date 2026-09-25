---
title: "The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems"
description: "Prefix caching is critical for efficient large language model (LLM) serving, particularly for agentic workloads that repeatedly invoke the model with a growing conversation and tool-use history."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.27746) · [PDF](https://arxiv.org/pdf/2609.27746)

## 一句话摘要

Prefix caching is critical for efficient large language model (LLM) serving, particularly for agentic workloads that repeatedly invoke the model with a growing conversation and tool-use history.

## 为什么值得关注

待编辑增强。

## 摘要原文

Prefix caching is critical for efficient large language model (LLM) serving, particularly for agentic workloads that repeatedly invoke the model with a growing conversation and tool-use history. By reusing the key-value (KV) states of previously processed prefixes, prefix caching avoids redundant prefill computation. Its effectiveness, however, depends on retaining a sufficiently large set of KV cache states. Provisioning enough cache to preserve all historical KV states is prohibitively expensive and often unnecessary, whereas insufficient capacity can substantially degrade the cache hit rate. Determining the KV cache working set, defined as the minimum cache capacity required to achieve a target hit rate, is therefore essential for efficient cache provisioning and system design. We present KVSET, an online analyzer that estimates the KV cache working set of LLM serving workloads. KVSET uses the Mattson stack algorithm to efficiently estimate cache hit rates across a wide range of cache capacities. For each KV cache page, KVSET computes its LRU stack distance and compares it with the page number of each candidate capacity. This comparison determines whether the page would be a hit at each capacity without independently simulating every capacity configuration. KVSET therefore substantially reduces the computational and memory overhead of conventional capacity-by-capacity simulation and makes online working-set analysis practical. KVSET further determines the minimum cache capacity based on the maximum LRU depth among the prefix pages required to achieve the target hit rate. We validate KVSET using traces collected from production LLM workloads and show that its estimates closely match measurements from real cache deployments. The open-source implementation supports both online request processing and offline trace replay.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luchang Li, Shuaishuai Wang, Zhao Ruan, Dongfang Li, Bozhao Gong
- 发布：2026-09-23；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
