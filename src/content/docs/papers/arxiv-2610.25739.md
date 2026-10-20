---
title: "How Much Does One Wrong Answer Cost? Error Propagation in Constraint Pruning with Noisy LLM Oracles"
description: "Constraint pruning saves queries to a large language model (LLM) or another noisy oracle by skipping each yes/no question implied by answers accepted earlier, for example through transitivity."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.25739) · [PDF](https://arxiv.org/pdf/2610.25739)

## 一句话摘要

Constraint pruning saves queries to a large language model (LLM) or another noisy oracle by skipping each yes/no question implied by answers accepted earlier, for example through transitivity.

## 为什么值得关注

待编辑增强。

## 摘要原文

Constraint pruning saves queries to a large language model (LLM) or another noisy oracle by skipping each yes/no question implied by answers accepted earlier, for example through transitivity. Entity-resolution systems and LLM-based rankers use this idea. However, their analyses typically assume a correct oracle. We argue that pruning should be judged by its risk when the oracle errs, since an accepted wrong answer spreads to every question it implies. When each answer is wrong independently with small probability $\varepsilon$, the first-order risk is set by how many facts one wrong answer corrupts on average. We consider two kinds of constraints. For implication rules, as in taxonomies, pruning in a random order adds no first-order risk: a wrong answer that would change $k$ facts is accepted with probability $1/k$, so it costs one fact on average. Rules with $s$ premises break this balance: a wrong answer at a premise shared by $r$ rules can cost order $r^{1-1/s}$ facts. For entity resolution with $m$ records of one entity, the first-order risk equals $\varepsilon$ times the Wiener index (the total pairwise distance) of the spanning tree built by the query order. Pivot orders, which first compare one record with all others, amplify errors by less than 2 and are optimal; random orders by order $m^{1/3}$; the common most-similar-first order is the worst in one dimension and, for large $m$, worse than random in two. With several entities, the cost of wrongly merging two does not depend on how many others exist. Simulations agree with every predicted constant within sampling error.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zhengtao Gui (University of California, Irvine), Weining Shen (University of California, Irvine)
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
