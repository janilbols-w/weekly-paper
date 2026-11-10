---
title: "MemSkill: Learning and Evolving Memory Skills for Self-Evolving Agents"
description: "Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2602.02474) · [PDF](https://arxiv.org/pdf/2602.02474)

## 一句话摘要

Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Most Large Language Model (LLM) agent memory systems rely on a small set of static, hand-designed operations for extracting memory. These fixed procedures hard-code human priors about what to store and how to revise memory, making them rigid under diverse interaction patterns and inefficient on long histories. To this end, we present \textbf{MemSkill}, which reframes these operations as learnable and evolvable memory skills, structured and reusable routines for extracting, consolidating, and pruning information from interaction traces. Inspired by the design philosophy of agent skills, MemSkill employs a \emph{controller} that learns to select a small set of relevant skills, paired with an LLM-based \emph{executor} that produces skill-guided memories. Beyond learning skill selection, MemSkill introduces a \emph{designer} that periodically reviews hard cases where selected skills yield incorrect or incomplete memories, and evolves the skill set by proposing refinements and new skills. Together, MemSkill forms a closed-loop procedure that improves both the skill-selection policy and the skill set itself. Experiments on LoCoMo, LongMemEval, HotpotQA, and ALFWorld demonstrate that MemSkill improves task performance over strong baselines and generalizes well across settings. Further analyses shed light on how skills evolve, offering insights toward more adaptive, self-evolving memory management for LLM agents. Code is available at https://github.com/ViktorAxelsen/MemSkill

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: memory management
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Haozhen Zhang, Quanyu Long, Jianzhu Bao, Tao Feng, Weizhi Zhang, Haodong Yue, Wenya Wang
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ViktorAxelsen/MemSkill](https://github.com/ViktorAxelsen/MemSkill)
- 阅读深度：metadata
