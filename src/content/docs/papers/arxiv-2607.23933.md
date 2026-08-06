---
title: "SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving"
description: "As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency."
---

**评分：47/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2607.23933) · [PDF](https://arxiv.org/pdf/2607.23933)

## 一句话摘要

As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency.

## 为什么值得关注

待编辑增强。

## 摘要原文

As LLM agents increasingly rely on the Model Context Protocol (MCP) to invoke isolated external sandboxes, disaggregated sandbox deployment introduces a fundamental tension between resource utilization and interactive tail latency. Persistent long-lived sandbox reservations incur excessive memory overhead at scale, while lazy on-demand instantiation generates severe cold-start penalties that degrade response performance under multi-tenant, multi-turn agent workloads. To resolve this dilemma, we present SpecBox, a runtime built around speculative sandbox preallocation tailored for dynamic LLM agent execution pipelines. At its core, SpecBox implements keyword matching and streaming semantic embedding to enable intent-driven sandbox prewarming, which identifies pending tool execution demands mid-LLM token generation and fully overlaps sandbox bootstrapping with model inference. To extend prewarming windows across sequential agent steps, the framework leverages context-aware stochastic prefetching atop a sandbox dependency graph to probabilistically forecast future sandbox switches ahead of execution. We complement these speculative mechanisms with two orthogonal optimizations: a semantic result cache that prunes redundant repeated sandbox invocations, and a dedicated out-of-band shared-memory transport plane that bypasses conventional network serialization to deliver zero-copy artifact transfers. Evaluated on high-concurrency multi-turn agent traces, our prototype demonstrates that SpecBox cuts P99 end-to-end latency by up to $2.9\times$ relative to the on-demand sandbox baseline, while slashing peak memory consumption by $45.9\%$ compared to permanently reserved sandbox deployments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: multi-tenant, tail latency
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yihui Zhang (Beihang University), Tianyu Wo (Beihang University), Jinghao Wang (Beihang University), Xiaoyang Sun (University of Leeds), Menghao Zhang (Beihang University), Cangzhou Yuan (Beihang University), Li Li (Beihang University), Chunming Hu (Beihang University), Albert Y. Zomaya (The University of Sydney), Renyu Yang (Beihang University)
- 发布：2026-08-06；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
