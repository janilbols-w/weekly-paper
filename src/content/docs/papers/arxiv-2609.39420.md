---
title: "QuantCode Model: Specializing Language Models for Executable Algorithmic Trading Code"
description: "Large language models are strong general-purpose code generators, but executable algorithmic trading remains a demanding specialization target: a model must translate a natural-language strategy specification into correct program logic for a specialized trading framework, execute on historical data, produce trades, and remain semantically faithful to the req"
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2609.39420) · [PDF](https://arxiv.org/pdf/2609.39420)

## 一句话摘要

Large language models are strong general-purpose code generators, but executable algorithmic trading remains a demanding specialization target: a model must translate a natural-language strategy specification into correct program logic for a specialized trading framework, execute on historical data, produce trades, and remain semantically faithful to the req

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models are strong general-purpose code generators, but executable algorithmic trading remains a demanding specialization target: a model must translate a natural-language strategy specification into correct program logic for a specialized trading framework, execute on historical data, produce trades, and remain semantically faithful to the request. We study two complementary mechanisms for specializing language models for this setting: continued pretraining on algorithmic-trading framework code and supervised fine-tuning (SFT) on agent-validated request-to-code pairs. Evaluation is centered on QuantCode-Bench, our 400-task benchmark for Backtrader strategy generation, together with a repository-level SWE-bench-like track. Continued pretraining improves single-turn Judge Pass from 41.5% to 47.5% for Qwen3.5-397B-A17B and from 27.8% to 33.0% for Qwen3.6-35B-A3B. SFT applied after continued pretraining yields a larger gain for Qwen3.6-35B-A3B, reaching 58.2% Judge Pass and 83.5% successful backtests; in agentic evaluation it raises first-turn success from 22.3% to 58.3% and final success after up to 10 turns from 47.5% to 79.5%. Continued pretraining alone improves first-turn agentic success but lowers final success after repair from 47.5% to 32.5%, consistent with degraded instruction following, whereas SFT improves both. We also identify a capability-retention failure: domain specialization degrades parser-conformant structured tool calling, and targeted recovery SFT restores tool-call formatting but not the base checkpoint's repository-level agent performance. The results show that framework-oriented pretraining, validated SFT, and explicit capability-retention evaluation address distinct failure modes in domain-specific executable code generation.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Alexey Chernysh, Orkhan Ekhtibarov, Dmitry Zmitrovich
- 发布：2026-09-30；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
