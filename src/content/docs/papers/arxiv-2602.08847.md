---
title: "Dr. MAS: Stable Reinforcement Learning for Multi-Agent LLM Systems"
description: "Multi-agent LLM systems enable advanced reasoning and tool use via role specialization, yet reliable reinforcement learning (RL) post-training for such systems remains difficult."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2602.08847) · [PDF](https://arxiv.org/pdf/2602.08847)

## 一句话摘要

Multi-agent LLM systems enable advanced reasoning and tool use via role specialization, yet reliable reinforcement learning (RL) post-training for such systems remains difficult.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-agent LLM systems enable advanced reasoning and tool use via role specialization, yet reliable reinforcement learning (RL) post-training for such systems remains difficult. In this work, we theoretically pinpoint a key reason for training instability when extending group-based RL to multi-agent LLM systems. We show that under GRPO-style optimization, a global normalization baseline may deviate from diverse agents' reward distributions, which ultimately leads to gradient-norm instability. Based on this finding, we propose Dr. MAS, a simple and stable RL training recipe for multi-agent LLM systems. Dr. MAS uses an agent-wise remedy: normalizing advantages per agent using each agent's own reward statistics, which calibrates gradient scales and dramatically stabilizes training, both theoretically and empirically. Beyond the algorithm, Dr. MAS provides an end-to-end RL training framework for multi-agent LLM systems, supporting scalable orchestration, flexible per-agent LLM serving and optimization configs, and shared resource scheduling of LLM actor backends. We evaluate Dr. MAS on multi-agent math reasoning and multi-turn search benchmarks using Qwen2.5 and Qwen3 series models. Dr. MAS achieves clear gains over vanilla GRPO (e.g., +5.6\% avg@16 and +4.6\% pass@16 on math, and +15.2\% avg@16 and +13.1\% pass@16 on search) while largely eliminating gradient spikes. Moreover, it remains highly effective under heterogeneous agent-model assignments while improving efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Lang Feng, Longtao Zheng, Shuo He, Fuxiang Zhang, Bo An
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
