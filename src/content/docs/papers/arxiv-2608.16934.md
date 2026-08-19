---
title: "SeqFeed: Improving Agentic RTL Code Generation with Sequential Behavior Feedback"
description: "RTL code generation is a critical stage in hardware design, and the emergence of agentic systems offers new opportunities to automate this process."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2608.16934) · [PDF](https://arxiv.org/pdf/2608.16934)

## 一句话摘要

RTL code generation is a critical stage in hardware design, and the emergence of agentic systems offers new opportunities to automate this process.

## 为什么值得关注

待编辑增强。

## 摘要原文

RTL code generation is a critical stage in hardware design, and the emergence of agentic systems offers new opportunities to automate this process. To generate correct RTL code, agents must understand sequential behavior, including how signals evolve and propagate over multiple clock cycles. However, effectively conveying such temporal information to agents remains a significant challenge. RTL code does not expose cycle-level signal behavior for a specific execution, whereas full simulation waveforms are too voluminous and noisy for effective LLM analysis. To address these limitations, we study how human engineers reason about sequential behavior and identify three requirements for effective feedback: it should be event-addressable, dependency-traceable, and iteratively-queryable. Guided by these requirements, we propose \textit{SeqFeed}, which comprises two complementary mechanisms: (1) \textit{SeQuery}, an SQL-like waveform query language that enables agents to anchor queries to semantic events and sample signal values at relative time points; and (2) \textit{SeGraph}, a dependency graph that tracks signal propagation across clock cycles. Experimental results across multiple LLMs demonstrate the effectiveness of SeqFeed in improving pass rates. SeQuery and SeGraph are each effective independently and provide complementary benefits when used together.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuxin Du, Juxin Niu, Tao Hu, Xi Wang, Zhe Jiang, Nan Guan
- 发布：2026-08-19；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
