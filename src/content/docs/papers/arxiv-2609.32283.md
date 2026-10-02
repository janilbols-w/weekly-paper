---
title: "AgentReplay: Token-Wise Trace Replay Is Essential for Fair Serving System Performance Benchmarking"
description: "LLM-based agents execute multi-turn workflows with interleaved model inference and tool calls, making efficient serving increasingly important."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](http://arxiv.org/abs/2609.32283v1) · [PDF](https://arxiv.org/pdf/2609.32283v1)

## 一句话摘要

LLM-based agents execute multi-turn workflows with interleaved model inference and tool calls, making efficient serving increasingly important.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based agents execute multi-turn workflows with interleaved model inference and tool calls, making efficient serving increasingly important. However, evaluating serving optimizations is challenging because identical tasks can produce different execution trajectories. Changes in generated tokens can alter subsequent prompts, tool calls, and reasoning turns, making it difficult to distinguish system improvements from workload variation. Greedy decoding does not guarantee identical outputs, while replaying only sequence lengths loses token information that affects prefix caching and mixture-of-experts (MoE) routing. To address these problems, we propose AgentReplay, a configurable trace record-and-replay framework for agent serving. AgentReplay records input/output tokens, expert selections, request dependencies, and tool durations. During replay, it forces the recorded output tokens while performing normal autoregressive computation, with optional controls for MoE expert selection and tool delays. This allows different systems to execute the same recorded workload while retaining their own batching, scheduling, and parallelization decisions. We further separate trajectory generation from performance evaluation, enabling compatible smaller models to replay long-horizon traces collected with more capable models. Our experiments show that token-wise replay in AgentReplay effectively eliminates workload variation that greedy decoding and length-wise replay cannot avoid, enabling fairer performance comparisons across serving configurations.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: prefix caching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zaifeng Pan, Michael Wang, Chris Wu, Zhengding Hu, Xinwei Qiang, Zhongkai Yu, Yufei Ding
- 发布：2026-09-26；更新：2026-09-26
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
