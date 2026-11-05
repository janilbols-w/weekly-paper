---
title: "Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework"
description: "Autonomous agents challenge conventional LLM serving with long-lived, cross-component execution and evolving system state."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2607.29069) · [PDF](https://arxiv.org/pdf/2607.29069)

## 一句话摘要

Autonomous agents challenge conventional LLM serving with long-lived, cross-component execution and evolving system state.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autonomous agents challenge conventional LLM serving with long-lived, cross-component execution and evolving system state. These characteristics complicate controlled systems experimentation and attribution of end-to-end behavior across the serving stack. We present Aries, a full-stack experimentation framework that separates task specifications from execution configurations, reconstructs cross-component agent trajectories with correlated system telemetry, and exposes stateful tool execution through a consistent interface across heterogeneous sandbox substrates. We use Aries to conduct reproducible experiments on open agent harnesses and benchmarks. We complement these experiments with production traces from a commercial platform, grounding low-level systems research in observed production behavior. Our results show that (1) token-centric metrics miss non-inference bottlenecks, (2) retaining additional context yields diminishing accuracy benefits while reducing serving capacity, and (3) tool sandboxes alternate between long idle periods and short resource bursts, while current snapshot-based state management makes aggressive suspension costly. We then discuss the vision for agent-native serving systems designed around trajectory-level metrics, adaptive context management, and elastic sandbox resource management.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jooyoung Park, Leonid Kondrashov, Boxi Zhou, Hongrui Liu, Zonghao Liu, Chengzhi Lu, Riccardo Mancini, Esha Choukse, Haris Javaid, German Sviridov, Tao Peng, Chen Zhao, Anastasia Avdeeva, Aleksei Gusev, Marios Kogias, Luo Mai, Dmitrii Ustiugov
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
