---
title: "Learning When to Ask: Advisor-Aware Post-Training for SLM Agents"
description: "Small language models (SLMs) are increasingly attractive for cheap, high-throughput agentic deployment, but they remain weak at multi-step reasoning and tool use that long-horizon tasks demand."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > 编译器与计算图优化

[论文原文](https://arxiv.org/abs/2611.27443) · [PDF](https://arxiv.org/pdf/2611.27443)

## 一句话摘要

Small language models (SLMs) are increasingly attractive for cheap, high-throughput agentic deployment, but they remain weak at multi-step reasoning and tool use that long-horizon tasks demand.

## 为什么值得关注

待编辑增强。

## 摘要原文

Small language models (SLMs) are increasingly attractive for cheap, high-throughput agentic deployment, but they remain weak at multi-step reasoning and tool use that long-horizon tasks demand. We study how to post-train an SLM to seek advice from a stronger model and act on that advice itself, following an advisor-executor pattern. Out of the box, this pattern fails across open- and closed-source small-model families: wiring an SLM to an advisor is a harness-design matter that is not enough on its own. A post-training recipe is needed to teach the model when to ask, in a cost-aware fashion, and how to follow advice across steps. Our method, ADAPT (ADvisor-Aware Post-Training), is a multi-stage recipe that instills this behavior, learning entirely from the policy's own rollouts supervised by the environment's outcome, with no learned reward model or human annotation. Across three domains, compared to an untrained harness baseline, ADAPT improves success rate in embodied text reasoning (TextWorld) from 24.5% to 77.3%, code generation (LiveCodeBench) from 21.8% to 56.0%, and deep web search (GAIA) from 17.5% to 49.3%, while querying the advisor sparingly (~1.0-2.1 calls per task). On the two long-horizon domains it closes 70-85% of the gap to an oracle that perfectly times when to ask for advice, and on code generation it exceeds that oracle. The gains persist when the advisor is replaced by one unseen in training, showing that the learned help-seeking policy is robust to a changing advisor rather than tied to the one it was trained with.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: code generation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Aasheesh Singh, Vishal Vaddina
- 发布：2026-11-23；更新：2026-11-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
