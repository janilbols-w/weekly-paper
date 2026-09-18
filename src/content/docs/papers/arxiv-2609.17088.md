---
title: "Interactive Memory Learning for Long-Term Conversations"
description: "Recent advancements in large language models have significantly enhanced the capabilities of agents in modeling long-term conversations."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2609.17088) · [PDF](https://arxiv.org/pdf/2609.17088)

## 一句话摘要

Recent advancements in large language models have significantly enhanced the capabilities of agents in modeling long-term conversations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent advancements in large language models have significantly enhanced the capabilities of agents in modeling long-term conversations. Despite these successes, existing approaches typically adopt a static heuristic paradigm, where information is passively archived without adaptive memory valuation. Consequently, these methods fail to self-evolve or align their memory management with evolving user needs. To address this, we propose ICML (InteraCtive Memory Learning), a multi-agent framework that transforms the memory mechanism from a passive archive into a learnable, interactive memory policy. Specifically, we first employ a session synthesis pipeline to generate expert data, facilitating rapid test-time adaptation in unseen scenarios. Building on this, ICML utilizes an online reinforcement learning mechanism where a Planner agent selectively encodes high-value information and a Trigger agent dynamically retrieves it to optimize response quality, whereby the two agents co-evolve through continuous interaction feedback. Crucially, both agents are synchronized through a delayed reward mechanism that propagates future feedback back to earlier storage decisions, ensuring memory policies are precisely aligned with user expectations. Experimental results demonstrate that ICML significantly outperforms strong baselines, exhibiting the unique capability to continuously improve response quality as interactions accumulate.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Cai Ke, Jiangyue Yan, Han Zhang, Xin Liu, Zike Yuan, Yue Yu, Hui Wang, Ruifeng Xu
- 发布：2026-09-15；更新：2026-09-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
