---
title: "Agentic Coding in the Wild: Characterizing GitHub Copilot Traces at Production Scale"
description: "AI coding agents (e.g., GitHub Copilot, Claude Code, Codex) interleave multi-step LLM inference with tool execution, creating a workload different from chatbots."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2608.00101) · [PDF](https://arxiv.org/pdf/2608.00101)

## 一句话摘要

AI coding agents (e.g., GitHub Copilot, Claude Code, Codex) interleave multi-step LLM inference with tool execution, creating a workload different from chatbots.

## 为什么值得关注

待编辑增强。

## 摘要原文

AI coding agents (e.g., GitHub Copilot, Claude Code, Codex) interleave multi-step LLM inference with tool execution, creating a workload different from chatbots. We present the first production-scale characterization of coding agents using sampled GitHub Copilot traces from June-July 2026, comprising 7.4M users, 819M conversations, 5.7B LLM calls, and 946T tokens. Our analysis reveals distinctive workload properties with unique systems implications: e.g., sparse user-initiated turns unfold into autonomous agent loops with nearly 1:1 coupling between LLM calls and tool execution; parallel LLM calls are rare but exist in turns that trigger subagents; KV cache hit rates average 90% within a turn, but fall to 52% across turn boundaries and to 6% after model switches; workflows and user behaviors exhibit diverse, long-tailed resource footprints. We further distinguish short agentic turnaround times from minutes-long user idle periods between turns, and develop a lightweight idle-time predictor that captures 87-89% of total idle time. We demonstrate two use cases: (1) a harness-side LLM API keep-alive policy that preserves provider-side context KV cache, reducing token costs by 14.9% on turn boundaries; and (2) a serving-side KV cache residency policy that uses predicted idle time to guide DRAM offloading, reducing time to first token (TTFT) by 3-33% compared with LRU during a one-week evaluation with GitHub Copilot traces.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Banruo Liu, Haoran Qiu, \'I\~nigo Goiri, Rodrigo Fonseca, Ricardo Bianchini, Esha Choukse
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
