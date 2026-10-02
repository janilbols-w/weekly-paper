---
title: "Tool Waiting and Re-arrival in Compile-Time-Static LLM Serving: Cost Mechanisms and Configuration Selection"
description: "In agentic LLM services, a session calls an external tool, waits for it, and re-arrives to continue inference."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](http://arxiv.org/abs/2609.34663v1) · [PDF](https://arxiv.org/pdf/2609.34663v1)

## 一句话摘要

In agentic LLM services, a session calls an external tool, waits for it, and re-arrives to continue inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

In agentic LLM services, a session calls an external tool, waits for it, and re-arrives to continue inference. Statically compiled NPU serving can fix the batch bucket set, the maximum batch size, and the number of KV cache slots at compile time. We define such an environment as a compile-time-static serving substrate and analyze the execution-time cost that tool waiting and re-arrival incur in it. On a single LLM instance, we run synthetic workloads following a measured tool waiting time distribution and compare, on the same inputs, a baseline configuration with settings {1, 2, 4, 8}, 8, and 8 against configurations that change some of them. Because re-arrival times differ across configurations, we build a simulator that replays request processing in time order, select the candidate with the lowest predicted cost among 2,077 configurations, and validate it on new inputs. We identify three mechanisms: discrete batch alignment, KV cache survival, and prefill interference. At a concurrency of 6, absent from the bucket set, tool waiting lowered the padding ratio (0.235 to 0.120) yet increased decode execution time 1.51-fold, so padding alone did not indicate cost. On new inputs at a concurrency of 8, where the baseline reused KV in 9 of 24 re-arrivals, enlarging the maximum batch size alone cut execution cost by 8.25%, and the selected configuration, which also adjusted the bucket set, by 9.72%. Where 17 of 18 re-arrivals were already reused, the effect was 0.59%. Compile-time configurations should thus be selected by diagnosing KV reuse loss and the resulting change in execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dongkyeom Jang, In-Nea Wang, Junho Jeong
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
