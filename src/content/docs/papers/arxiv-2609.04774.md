---
title: "Adaptive Context Parallelism for Production LLM Serving"
description: "As LLM context windows expand and input sequences grow longer, serving systems face increasing computational and memory demands."
---

**评分：48/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.04774) · [PDF](https://arxiv.org/pdf/2609.04774)

## 一句话摘要

As LLM context windows expand and input sequences grow longer, serving systems face increasing computational and memory demands.

## 为什么值得关注

待编辑增强。

## 摘要原文

As LLM context windows expand and input sequences grow longer, serving systems face increasing computational and memory demands. Context parallelism (CP), which partitions the input sequence across multiple ranks to parallelize the computation, has therefore become increasingly important for efficient LLM serving. However, existing CP-enabled systems either rely on static CP configurations or adjust the CP degree only for active requests or batches. In this paper, we present Vertumnus, an adaptive CP serving system designed for heterogeneous and evolving workloads. At the request level, Vertumnus routes requests among workers with different CP degrees using a placement cost that combines predicted queuing delay, cache-aware prefill time, and GPU-time cost. At the cluster level, Vertumnus adapts the worker composition through seconds-scale split and merge operations as workload demand changes. Vertumnus further introduces a global prefix-cache management policy that coordinates cache placement and replication among workers with the same or different CP degrees, preserving cache locality as request assignments and worker composition change. Experiments on a 64-GPU cluster with public and production workloads show that, under the highest evaluated loads, Vertumnus reduces mean TTFT by up to 28.1% and improves token-weighted SLO attainment by up to 13.3 percentage points over the strongest baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiarui Guo, Rongle Wang, Peijun Huang, Zongwei Lv, Ziqing Wang, Kan Liu, Tao Lan, Lin Qu, Xiaolin Wang, Tong Yang
- 发布：2026-09-07；更新：2026-09-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
