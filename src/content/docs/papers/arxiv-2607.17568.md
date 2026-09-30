---
title: "CoCurve: Cross-Module Co-Pruning Curvature for Structured LLM Pruning"
description: "Resource-constrained deployment requires sustaining large language model (LLM) capabilities as models scale under fixed memory and computation budgets."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.17568) · [PDF](https://arxiv.org/pdf/2607.17568)

## 一句话摘要

Resource-constrained deployment requires sustaining large language model (LLM) capabilities as models scale under fixed memory and computation budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Resource-constrained deployment requires sustaining large language model (LLM) capabilities as models scale under fixed memory and computation budgets. Structured pruning advances this deployment frontier with smaller dense checkpoints, yet deciding what to prune remains bottlenecked by interactions among joint removals. We introduce Cross-Module Co-Pruning Curvature (CoCurve), which formulates structured pruning as set-dependent predictive risk over a unified inventory of attention heads and feed-forward groups. A co-pruning graph built from single-unit forward ablations assigns individual risk to nodes and reinforcement or cancellation to interaction edges, conditioning each decision on the units already removed. We evaluate 6 LLMs (3B--70B) and 3 vision--language models (VLMs) across 3 perplexity corpora, 12 language tasks, and 7 multimodal benchmarks. Across the five-model 20--40% grid and the 70B 10--50% sweep, CoCurve ranks first in 53/60 corpus comparisons (15/15 at 70B); matched-quality interpolation permits 2.2--6.6 more pruning points in 9/10 cases, while CoCurve leads all 6 VLM Avg$_7$ blocks. After the same lightweight recovery, its retained structures remain strongest through 50% pruning, where the 8B checkpoint regains 10.8 Avg$_{12}$ points; physical slicing delivers $1.58\times$ dense prefill throughput with 41% lower peak memory. Mechanism analysis across 10 LLMs and 7 VLMs finds organized within- and cross-module edge structure; matched low-saliency, high-coupling removals degrade 19/20 capability groups by up to 23.7 points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhiren Gong, Zihao Zeng, Tiantong Wang, Yixin Wang, Honoka Anada, Zijie Wang, Ming Xiao, Chau Yuen, Wei Yang Bryan Lim
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
