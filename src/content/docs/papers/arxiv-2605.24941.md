---
title: "Memory-Induced Tool-Drift in LLM Agents"
description: "LLM agents increasingly combine long-term memory for personalization with tool calling for taking actions."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2605.24941) · [PDF](https://arxiv.org/pdf/2605.24941)

## 一句话摘要

LLM agents increasingly combine long-term memory for personalization with tool calling for taking actions.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM agents increasingly combine long-term memory for personalization with tool calling for taking actions. We study a failure of this combination: personality-driven preferences stored in memory (e.g., cost-consciousness, impatience, risk tolerance) silently shifting tool-call parameters in contexts where they do not apply. We call this memory-induced tool-drift and stress-test it with MEMDRIFT, an iteratively refined benchmark of 105 scenarios spanning five bias dimensions and seven professional domains. Measured as excess parameter degradation over a neutral-memory baseline, biased memories in MEMDRIFT induce drift in all eight models we evaluate, raising degradation rates to 0.38--0.83 versus 0.05--0.12 for neutral memories. The drift persists under three widely used memory frameworks. A vulnerability audit of 6,062 tools across 288 MCP servers demonstrates that real-world tools are also susceptible to this failure mode. Mechanistically, we find that biased memories act as implicit steering vectors along the same direction as explicit behavioral instructions and draw attention away from task-relevant context. Neither prompt-based defenses nor relevance filters offer a complete solution, motivating defenses at the intersection of memory management and tool calling.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mahavir Dabas, Jihyun Jeong, Ming Jin, Ruoxi Jia
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
