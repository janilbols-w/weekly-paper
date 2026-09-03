---
title: "MASkills: Continual Skills Optimization for Multi-Agent LLM Systems"
description: "LLM-based multi-agent systems have shown strong performance on complex tasks, yet continual improvement from interaction experience remains challenging."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.02094) · [PDF](https://arxiv.org/pdf/2609.02094)

## 一句话摘要

LLM-based multi-agent systems have shown strong performance on complex tasks, yet continual improvement from interaction experience remains challenging.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-based multi-agent systems have shown strong performance on complex tasks, yet continual improvement from interaction experience remains challenging. Existing self-reflection methods build experience memories, but memories are mostly hard to invoke, refine, or scale, while agent skills offer a more actionable unit: structured procedural knowledge that specifies when to act, how to act, and which resources or tools to use. We introduce MASkills, a continual learning framework that optimizes multi-agent LLM systems through agent skills. MASkills presents a new agent-optimization pipeline that integrates skill-conditioned credit assignment, hierarchical credit aggregation, and momentum-smoothed optimization, enabling agent skill libraries to evolve through refinement, induction, consolidation, and pruning. Experiments on HotpotQA, LoCoMo, and GAIA demonstrate the effectiveness of MASkills across multiple agentic tasks. Our code is available at https://github.com/DaRL-GenAI/MASkills

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Huaiyuan Yao, Xiaoou Liu, Charles Fleming, Tianlong Chen, Hua Wei
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/DaRL-GenAI/MASkills](https://github.com/DaRL-GenAI/MASkills)
- 阅读深度：metadata
