---
title: "Rethinking the Evaluation of Efficiency Methods for Multi-Agent Systems"
description: "Efficiency is increasingly important for Large Language Model (LLM)-based multi-agent systems (MAS), as larger models and more agents introduce substantial execution costs."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.05933) · [PDF](https://arxiv.org/pdf/2609.05933)

## 一句话摘要

Efficiency is increasingly important for Large Language Model (LLM)-based multi-agent systems (MAS), as larger models and more agents introduce substantial execution costs.

## 为什么值得关注

待编辑增强。

## 摘要原文

Efficiency is increasingly important for Large Language Model (LLM)-based multi-agent systems (MAS), as larger models and more agents introduce substantial execution costs. Recent methods aim to make MAS cheaper by pruning agents, removing communication edges, or searching for compact structures. However, we argue that existing evaluations may overestimate their true ability to improve MAS efficiency. Reported gains are often measured under method-specific prompts and starting topologies, making them difficult to attribute to the proposed structural changes. Moreover, many reported successes appear in non-MAS-demanding settings, where a single agent or a randomly pruned system can already preserve strong performance. To study these issues, we introduce a controlled and MAS-demanding diagnostic benchmark for representative MAS efficiency methods. We evaluate methods under a shared backbone model, agent registry, and runtime, across controlled variations in topology, scale, depth, and tool use. Our analysis shows that many reported gains are setup-dependent and may arise from structural collapse, disabled tool pathways, or starting systems where random pruning already preserves accuracy, rather than robust improvements in MAS efficiency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiamu Zhang, Lingxi Zhang, Pengjun Lu, Qiyue Zhang, Yu-Neng Chuang, Zhengchen Li, Shuai Xu, Vipin Chaudhary, Hanjie Chen
- 发布：2026-09-05；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
