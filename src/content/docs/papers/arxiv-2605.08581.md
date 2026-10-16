---
title: "HAServe: Horizon-Aware Scheduling and Memory Co-Design for Efficient LLM Serving"
description: "Online large language model (LLM) services process requests that share context but differ in prefix structure and arrival timing."
---

**评分：53/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2605.08581) · [PDF](https://arxiv.org/pdf/2605.08581)

## 一句话摘要

Online large language model (LLM) services process requests that share context but differ in prefix structure and arrival timing.

## 为什么值得关注

待编辑增强。

## 摘要原文

Online large language model (LLM) services process requests that share context but differ in prefix structure and arrival timing. Finite capacity couples request admission and key-value (KV) retention. This paper addresses one online serving problem: using a unified view of visible demand to choose the feasible joint admission and KV-retention candidate with the lowest predicted latency cost as prefix structures and arrival rates vary. To model this problem, we introduce HorizonSchema, a workload abstraction that connects exact prefix paths, permitted serializations, and released consumers as shared inputs to both decisions. Our analysis shows that useful reuse depends on demand and prefix survival, while service order changes latency even at equal computation. Furthermore, we present HAServe, which turns this abstraction into a scheduling--memory co-design method of systematic optimization for online LLM serving. We implement HAServe on SGLang and evaluate Qwen3-4B-Instruct-2507 and Llama2-13B on five workloads using eight H100 GPUs. Across the evaluated workloads, HAServe achieves up to $1.14$--$5.90\times$ P99 TTFT speedups and up to $1.08$--$1.44\times$ the throughput, with KV-cache hit rate up to 20.59 percentage points higher than the strongest baseline for each metric and setting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 15 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xingyu Qu, Tianhao Lin, Yiqi Li, Zhiyu Chen, Sheng Wang
- 发布：2026-10-16；更新：2026-10-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
