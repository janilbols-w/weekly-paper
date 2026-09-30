---
title: "Equal Ranking Quality, Different Decisions: Measuring and Reducing Order Dependence in LLM Scorers"
description: "In passage reranking, response ranking and multi-document question answering, LLMs can score several candidate documents or responses together in one prompt, each still receiving its own score."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.26762) · [PDF](https://arxiv.org/pdf/2608.26762)

## 一句话摘要

In passage reranking, response ranking and multi-document question answering, LLMs can score several candidate documents or responses together in one prompt, each still receiving its own score.

## 为什么值得关注

待编辑增强。

## 摘要原文

In passage reranking, response ranking and multi-document question answering, LLMs can score several candidate documents or responses together in one prompt, each still receiving its own score. Such scorers are selected on ranking quality, but their scores determine a decision: what a score threshold retains, a reader answers, or which chosen/rejected pair enters preference training. Because the candidates share that prompt, reordering them changes their scores. The same query over the same candidates should still yield the same decision. However, equal ranking quality does not imply equal decisions: on passage reranking, five trained scorers within 0.010 nDCG@10 retain sets that overlap by only 0.66-0.84 when reordered. No prompt-time change we test resolves that dependence: the only one that improves ranking quality does not measurably improve decision stability. We introduce order-consistency SFT (OC-SFT), which attenuates it in the weights by penalizing disagreement between a candidate's scores across orderings. It holds ranking quality and leads every decision-stability measure among trained scorers on all three tasks. It is also more stable on 12 base models than order-averaged distillation, which trains on labels averaged across permutations. One OC-SFT permutation retains sets that overlap more than ten averaged off-the-shelf permutations. A comparison of such scorers should therefore report what a threshold retains and a reader answers, not ranking quality alone. Code is available at https://github.com/thomsonreuters/presentation-dependence.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Markus Frohmann, Mahdiyar Ali Akbar Alavi, Elizabeth Lingg, Navid Rekabsaz
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/thomsonreuters/presentation-dependence](https://github.com/thomsonreuters/presentation-dependence)
- 阅读深度：metadata
