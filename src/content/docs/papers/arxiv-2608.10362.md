---
title: "MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices"
description: "Speculative decoding accelerates autoregressive large language model (LLM) inference by using a lightweight draft model to speculate multiple tokens, reducing expensive target model decoding steps."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.10362) · [PDF](https://arxiv.org/pdf/2608.10362)

## 一句话摘要

Speculative decoding accelerates autoregressive large language model (LLM) inference by using a lightweight draft model to speculate multiple tokens, reducing expensive target model decoding steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates autoregressive large language model (LLM) inference by using a lightweight draft model to speculate multiple tokens, reducing expensive target model decoding steps. Its effectiveness depends heavily on draft selection, motivating adaptive methods that exploit variation across inputs and generation stages. On memory-constrained edge devices, however, these methods often fail to improve end-to-end throughput due to the overhead of switching between draft models. We identify a key limitation in this setting: the mismatch between draft selection and draft availability under tight memory budgets. To address this challenge, we present MemSpec, a prediction-guided, memory-aware runtime for adaptive speculative decoding on edge devices. MemSpec decouples draft selection from execution through proactive resident working-set management. A lightweight predictor estimates draft effectiveness from prompt and generation context, while a memory-aware scheduler reduces reactive model loading overhead. Experiments on a Jetson Orin Nano show that MemSpec improves steady-state generation throughput by 40.7% on average over state-of-the-art bandit-based adaptive methods while closely approaching the oracle upper bound.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Eunjeong Kim, Yeong Jun Jeon, Myeonggyun Han
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
