---
title: "FinEvolveBench: A Benchmark for Self-Evolving Agents on Low-Repetition Tasks with Implicit Rewards"
description: "Large language model (LLM) agents increasingly rely on external experience to continually adapt to changing environments without modifying their underlying models."
---

**评分：42/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2606.06960) · [PDF](https://arxiv.org/pdf/2606.06960)

## 一句话摘要

Large language model (LLM) agents increasingly rely on external experience to continually adapt to changing environments without modifying their underlying models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) agents increasingly rely on external experience to continually adapt to changing environments without modifying their underlying models. Recent experience mechanisms have demonstrated promising results across diverse tasks. However, their effectiveness is typically evaluated within individual benchmark settings, and how experience mechanisms generalize across different scenarios remains insufficiently explored. In this work, we present a scenario-oriented analysis of experience mechanisms for LLM agents. We characterize existing evaluation scenarios along four dimensions: outcome observability, credit assignment complexity, environmental dynamics, and experience reusability. Our analysis shows that existing benchmarks often evaluate experience mechanisms under scenarios where at least one dimension is comparatively favorable, leaving more challenging combinations of scenario properties underexplored. To address this gap, we introduce \textsc{FinEvolveBench}, a reproducible benchmark built on a chronological stream of rich financial news and market data that enables systematic evaluation of experience-based self-evolution under challenging experience regimes characterized by noisy feedback, ambiguous credit assignment, environmental non-stationarity, and limited experience reusability. Experiments show that existing approaches exhibit substantially reduced or inconsistent gains in this setting, highlighting the scenario-dependent nature of experience mechanisms and the challenge of maintaining valid experience under changing environments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 5 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yining Zhu, Zihao Deng, Leiming Wang, Jingfei Lu, Junbo Wang, Yuke Li, Jikun Shen, Chuncheng Ran
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
