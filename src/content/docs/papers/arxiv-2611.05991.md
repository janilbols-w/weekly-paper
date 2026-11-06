---
title: "A Controlled Experimental Evaluation of Configuration and Cache Architecture in LLM Serving Engines"
description: "Multi-agent LLM applications repeat most of their prompt tokens across requests, and serving engines reuse the cached state of shared prefixes."
---

**评分：53/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2611.05991) · [PDF](https://arxiv.org/pdf/2611.05991)

## 一句话摘要

Multi-agent LLM applications repeat most of their prompt tokens across requests, and serving engines reuse the cached state of shared prefixes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-agent LLM applications repeat most of their prompt tokens across requests, and serving engines reuse the cached state of shared prefixes. vLLM and SGLang reuse it at different granularities, and benchmarks of their default deployments report large performance gaps, usually credited to the cache. Such comparisons rarely control for other configuration differences. One of them, whether a long prompt is prefilled in chunks, is set by each engine's defaults from the hardware and the release, and it confounds the comparison. We built a reproducible testbed on Kubernetes and a seeded multi-agent workload generator, and compared the two engines under vendor defaults and with chunked prefill matched. SGLang's configuration is the same in both arms, which makes it an internal control across independently provisioned deployments. Under defaults, vLLM's median time to first token is up to 64x SGLang's. Matching one setting removes 78% of the capacity gap where that gap is largest and 30 to 67% of the latency gap. Near saturation the remaining latency gap reflects queue growth. A fluid queue model driven only by a 4.4% throughput shortfall reproduces it, and shows that such a gap scales with the length of the benchmark run. What survives matching is a tail-latency advantage of 2.4 to 6.4x at equal throughput, consistent with cache-aware ordering of waiting requests. We derive six recommendations for comparing serving engines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 12 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Muhammad Faizan Anwar, Sina Keshvadi
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
