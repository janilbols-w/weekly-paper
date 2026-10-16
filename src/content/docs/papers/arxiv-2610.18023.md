---
title: "FRACTION: Fraud Explanation Generation via Agentic Graph Context Navigation"
description: "Graph fraud explanation generation emerges as an important task, which requires jointly leveraging graph structure and content information to produce human-readable explanations for a given risk label."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.18023v1) · [PDF](https://arxiv.org/pdf/2610.18023v1)

## 一句话摘要

Graph fraud explanation generation emerges as an important task, which requires jointly leveraging graph structure and content information to produce human-readable explanations for a given risk label.

## 为什么值得关注

待编辑增强。

## 摘要原文

Graph fraud explanation generation emerges as an important task, which requires jointly leveraging graph structure and content information to produce human-readable explanations for a given risk label. An intuitive approach is to adapt existing graph-enhanced large language models (LLMs), which inject graph structure into LLMs via graph-conditioned instruction tuning or structure-aware embeddings. However, existing methods face two key challenges in graph fraud explanation generation: a lack of evaluation protocols tailored to explanation quality, and a mismatch between the granularity of graph information they provide and what explanation generation requires. In this paper, we propose FRaud Explanation Generation via Agentic Graph Context NavigaTION (FRACTION), a framework for graph fraud explanation generation. To evaluate explanation quality, we introduce a task-specific rubric that assesses faithfulness, graph grounding, helpfulness, consistency, and conciseness, and validate it against human judgments. To focus on fine-grained details of relevant neighbors without reading the entire neighborhood, we equip a language model with graph tools that progressively disclose neighbor records. To train our graph agent, we propose a rubric-guided trajectory distillation strategy through which the agent learns both tool-use behavior and structured explanation generation. Experimental results on three fraud datasets demonstrate consistent improvements over state-of-the-art baselines under a human-aligned rubric.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 15 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Cecelia Soh, Jun Hu, Yuan Li, Cheng Chen, Hui Liu, Yanjia Zhu, Hao He, Bryan Hooi, Bingsheng He
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
