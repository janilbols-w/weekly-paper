---
title: "Multi-Turn LLM Conversations under the Least-Recently-Used Policy: Mean-Field Asymptotics and Hit Ratio Approximation"
description: "The major workloads in modern large language model (LLM) serving systems have shifted from single-shot LLM calls to multi-turn conversations, where new responses are generated based on the whole conversation history across all previous turns."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.02027) · [PDF](https://arxiv.org/pdf/2609.02027)

## 一句话摘要

The major workloads in modern large language model (LLM) serving systems have shifted from single-shot LLM calls to multi-turn conversations, where new responses are generated based on the whole conversation history across all previous turns.

## 为什么值得关注

待编辑增强。

## 摘要原文

The major workloads in modern large language model (LLM) serving systems have shifted from single-shot LLM calls to multi-turn conversations, where new responses are generated based on the whole conversation history across all previous turns. The hit ratio, i.e., the average fraction of KV caches accessed directly from existing caches stored in high-bandwidth memory (HBM), is hence a crucial metric that governs system performance. Estimating the hit ratio is a highly nontrivial task due to the complex system dynamics, where the KV cache prefixes grow with turns and some must be evicted due to finite memory capacity. We formulate the system as a multi-turn conversation model under the least-recently-used (LRU) policy. Through a mean-field asymptotic framework, we prove that as the conversation arrival rate and the memory capacity grow proportionally to infinity, the hit ratio converges to a closed-form limit. Based on the characterization of the limit, we further propose a practical hit ratio estimator, and validate its accuracy by real LLM serving experiments on the Qwen3-8B model implemented on Ascend NPUs. Our results provide a theoretical foundation for the analysis of multi-turn LLM serving systems and a practical guideline for memory capacity provisioning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Heyuan Yao, Chutong Gao, Yuan Lyu, Izzy Grosof, David Simchi-Levi
- 发布：2026-09-02；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
