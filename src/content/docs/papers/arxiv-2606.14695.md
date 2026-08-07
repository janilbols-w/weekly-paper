---
title: "Persona-Pruner: Sculpting Lightweight Models for Role-Playing"
description: "Language Models (LMs) have shown remarkable potential as role-playing chatbots, delivering consistent, stylized interactions when given a specification of a character or user persona."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.14695) · [PDF](https://arxiv.org/pdf/2606.14695)

## 一句话摘要

Language Models (LMs) have shown remarkable potential as role-playing chatbots, delivering consistent, stylized interactions when given a specification of a character or user persona.

## 为什么值得关注

待编辑增强。

## 摘要原文

Language Models (LMs) have shown remarkable potential as role-playing chatbots, delivering consistent, stylized interactions when given a specification of a character or user persona. However, applying these capabilities to real-world applications (e.g., ecosystems with numerous NPCs interacting simultaneously) exposes a critical inefficiency due to the excessive computational cost. In this paper, we question the necessity of dedicating a full, generalist model to a single persona, hypothesizing that a specific character identity relies on only a fraction of the model's total capacity. We observe that naively pruning LMs often severely degrades the role-playing performance for a specific persona; it does not distinguish between redundant knowledge and essential character traits. We propose Persona-Pruner, a framework that sculpts a lightweight role-playing model by isolating persona-specific sub-networks from a single description. Our experiments consistently show that Persona-Pruner preserves role-playing performance substantially more effectively than existing state-of-the-art LLM pruning techniques, reducing the performance drop from the dense model by up to 93.8% over the strongest baseline on RoleBench in LLM-as-a-judge score, while still maintaining general LLM capabilities. Code is available at https://github.com/jsu-kim/Persona-Pruner.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Jinsu Kim, Jihoon Tack, Noah Lee, Jongheon Jeong
- 发布：2026-08-07；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/jsu-kim/Persona-Pruner](https://github.com/jsu-kim/Persona-Pruner)
- 阅读深度：metadata
