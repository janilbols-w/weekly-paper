---
title: "TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding"
description: "Speculative decoding accelerates large language model inference through a draft-then-verify paradigm."
---

**评分：44/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.26112) · [PDF](https://arxiv.org/pdf/2608.26112)

## 一句话摘要

Speculative decoding accelerates large language model inference through a draft-then-verify paradigm.

## 为什么值得关注

待编辑增强。

## 摘要原文

Speculative decoding accelerates large language model inference through a draft-then-verify paradigm. Building on this, tree-structured methods improve inference by organizing proposals into multiple candidate paths, increasing the accepted length. However, existing tree-structured methods use a single drafter for all drafting steps, creating a dilemma: a smaller drafter is fast but yields lower-quality trees, whereas a larger drafter improves tree quality but suffers from high latency. To address this, we propose TreeGraft, a multi-drafter framework in which drafters of different costs jointly construct a shared draft tree. TreeGraft uses the stronger drafter to rescore candidates by updating scores assigned by the weaker drafter, reselect grafting positions, and recover promising paths left unexplored. It also integrates stronger drafter expansions non-destructively, preserving existing branches that may still be accepted by the target model. Together, these designs improve the quality of the shared draft tree. To control the drafting cost, TreeGraft introduces a lightweight scheduler distilled from an offline value system to decide when to call the stronger drafter. Across 10 model pairs and 6 benchmarks, TreeGraft outperforms the better of the two fixed single-drafter endpoint strategies by 15.1% on average, reaching a maximum gain of 26.6%. Our code is available at https://anonymous.4open.science/r/TreeGraft-E983.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jiaming Fan, Daming Cao, Canchen Huang, Jiale Fu, Jin Zhang, Junjie Gao, Kai Yang, Xiangzhong Luo, Xu Yang
- 发布：2026-08-28；更新：2026-08-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
