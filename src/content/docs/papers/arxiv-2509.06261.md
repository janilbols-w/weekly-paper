---
title: "JigSLO: Solving the Resource Puzzle for Efficient Multi-LLM Serving"
description: "GPU spatial sharing co-locates instances with complementary demands, such as compute-bound prefill and memory-bound decode, promising cost-efficient multi-LLM serving."
---

**评分：51/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2509.06261) · [PDF](https://arxiv.org/pdf/2509.06261)

## 一句话摘要

GPU spatial sharing co-locates instances with complementary demands, such as compute-bound prefill and memory-bound decode, promising cost-efficient multi-LLM serving.

## 为什么值得关注

待编辑增强。

## 摘要原文

GPU spatial sharing co-locates instances with complementary demands, such as compute-bound prefill and memory-bound decode, promising cost-efficient multi-LLM serving. Prior systems partition compute and coordinate shared memory capacity, but do not model bandwidth contention among co-located instances of heterogeneous LLMs. This contention makes each instance's latency depend on the memory-access patterns of its co-runners, even when its own resource allocation remains unchanged. Drawing on extensive measurements, we find that the latency impact of bandwidth contention can be captured by a time-shared memory-access model with contended and uncontended periods, so the overall latency can be analytically estimated as a time-weighted average of the latency estimates for these periods. We propose JigSLO, a contention-aware multi-LLM serving system that manages memory resources and schedules each model's prefill and decode phases as separate instances, treating their co-location as a placement decision. Its contention-aware predictor estimates per-instance latency under any co-location from standalone profiles alone. Guided by these predictions, its placement algorithm jointly selects each instance's tensor parallelism, compute share, and batch configuration, pairing complementary memory-access patterns to maximize throughput within each model's latency targets. JigSLO's shared resource manager complements this on the capacity side, sharing weights, pooling KV cache, and transferring it between prefill and decode instances. Across three datasets covering chat, code generation, and long-context summarization, JigSLO outperforms state-of-the-art baselines by $2.3\times$ in SLO attainment and $1.2\times$ in throughput on average, matching their best attainment with half the GPUs on long-context workloads.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kyungmin Bin, Seungbeom Choi, Jimyoung Son, Jieun Choi, Daseul Bae, Daehyeon Baek, Kihyo Moon, Minsung Jang, Hyojung Lee
- 发布：2026-11-18；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
