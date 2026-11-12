---
title: "KAIROS: Stateful, Context-Aware Power-Efficient Agentic Inference Serving"
description: "Power has become a central bottleneck for AI inference."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2604.16682) · [PDF](https://arxiv.org/pdf/2604.16682)

## 一句话摘要

Power has become a central bottleneck for AI inference.

## 为什么值得关注

待编辑增强。

## 摘要原文

Power has become a central bottleneck for AI inference. This problem is becoming more urgent as agentic AI emerges as a major workload class, yet prior power-management techniques focus almost entirely on single-turn LLM serving. Our analysis shows that agentic serving behaves fundamentally differently: each request carries long-lived context that evolves across tool-interleaved turns, and lowering GPU frequency can push the system into a thrashing regime where memory pressure sharply worsens both performance and power efficiency. These observations show that power optimization for agentic serving requires rethinking. We present KAIROS, a context-aware power optimization system for agentic AI serving. KAIROS uses agent context as a first-class control signal to jointly manage GPU frequency, per-instance concurrency, and multi-instance request placement. This enables KAIROS to save power when memory headroom exists while avoiding thrashing and preserving performance targets. At a high level, KAIROS tracks requests at agent granularity, adapts local control to context growth and agent progress, and routes agents across instances to jointly improve power efficiency and memory stability. Evaluated across diverse software and data engineering agentic tasks, KAIROS achieves an average of 27% (up to 39.8%) power reduction while meeting the performance targets.

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

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yichao Yuan, Mosharaf Chowdhury, Nishil Talati
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
