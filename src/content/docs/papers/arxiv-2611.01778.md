---
title: "MemRole: From Memories to Decisions for Long-Horizon Reasoning in Role-Playing Agents"
description: "LLM-based role-playing agents are fluent at imitating a character's style, yet struggle to make role-consistent decisions over long narrative horizons."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.01778) · [PDF](https://arxiv.org/pdf/2611.01778)

## 一句话摘要

LLM-based role-playing agents are fluent at imitating a character's style, yet struggle to make role-consistent decisions over long narrative horizons.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based role-playing agents are fluent at imitating a character's style, yet struggle to make role-consistent decisions over long narrative horizons. Such decisions are shaped by experiences spanning many prior scenes, which are often partial and may point in different directions. Existing methods inject cross-scene memories as context, but do not reason about how past events shape a character's current motivations and behavior. We propose MemRole, a framework that makes this memory-to-decision process explicit. It introduces Long-Horizon Memory Thinking (LHMT), a reasoning schema that decomposes hidden reasoning into context understanding, memory activation, and response strategy planning, trained on a novel-derived dataset whose character-grounded, timeline-constrained memory pools limit each character to what it could plausibly know at the current narrative point. Beyond supervised fine-tuning, we propose Self-Refining On-Policy Self-Distillation (SR-OPSD): the model critiques its own rollouts against the reference under a data-driven rubric, and a critique-conditioned teacher view of the same model distills token-level guidance back into the policy. MemRole-32B improves over its backbone by 15.2 points on memory-grounded role-playing, performs on par with frontier LLMs such as GPT-5.4, and achieves the best character-motivation recognition accuracy on CroSS-MR.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Mengting Li, Xilong Cheng, Zhihao Xiao, Zhenhua Xu, Jingyuan Zhou, Linfeng Li, Long Zhang, Borui Cai, Yunxiao Qin
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
