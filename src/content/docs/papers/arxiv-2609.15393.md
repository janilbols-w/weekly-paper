---
title: "CodeTS: Verifiable Text-to-Time Series Generation via Executable Code"
description: "Text-to-Time Series Generation (Text-to-TS) provides a promising paradigm for synthesizing time series from natural language, enabling scenario-specific generation when real observations are scarce or costly to acquire."
---

**评分：44/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.15393) · [PDF](https://arxiv.org/pdf/2609.15393)

## 一句话摘要

Text-to-Time Series Generation (Text-to-TS) provides a promising paradigm for synthesizing time series from natural language, enabling scenario-specific generation when real observations are scarce or costly to acquire.

## 为什么值得关注

待编辑增强。

## 摘要原文

Text-to-Time Series Generation (Text-to-TS) provides a promising paradigm for synthesizing time series from natural language, enabling scenario-specific generation when real observations are scarce or costly to acquire. However, existing methods typically lack an explicit mechanism for deriving generation logic from textual descriptions to guide time series synthesis. In this paper, we propose CodeTS, a verifiable framework that uses code as an intermediate generation interface, reformulating Text-to-TS generation as a Text-to-Code-to-TS process. CodeTS first maps textual temporal descriptions into an explicit code space, where executable code specifies how textual requirements shape target temporal patterns, and then obtains the time series through code execution. To learn this code generation process reliably without real code annotations, CodeTS constructs aligned Text-Code-TS triplets from structured temporal attributes for supervised initialization. More importantly, we further design multi-stage execution-based rewards that verify format validity, code executability, and time series quality, enabling real Text-TS pairs to provide training signals for Reinforcement Learning with Verifiable Rewards (RLVR). Extensive experiments on eight benchmarks across short, medium, and long generation lengths demonstrate that CodeTS provides a strong zero-shot solution for Text-to-TS generation, outperforming LLM-based baselines and achieving better averaged results than supervised generative baselines trained on the target datasets.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xudong Yuan, Shunyu Liu, Tongya Zheng, Huiping Zhuang, Mingli Song, Kaixuan Chen
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
