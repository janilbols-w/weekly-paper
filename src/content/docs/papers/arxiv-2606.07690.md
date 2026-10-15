---
title: "HARP: Efficient Data Selection for Finetuning Large Language Models"
description: "Finetuning data selection requires balancing two competing goals: selecting examples that improve the downstream objective, and doing so without repeatedly finetuning models."
---

**评分：48/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.07690) · [PDF](https://arxiv.org/pdf/2606.07690)

## 一句话摘要

Finetuning data selection requires balancing two competing goals: selecting examples that improve the downstream objective, and doing so without repeatedly finetuning models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Finetuning data selection requires balancing two competing goals: selecting examples that improve the downstream objective, and doing so without repeatedly finetuning models. Train-free selectors are scalable but rely on proxies such as embedding similarity or clustering, which may not match the target objective. Train-based selectors better reflect downstream utility through gradient signals, subset evaluation, or Shapley attribution, but require many costly train-evaluate iterations. We propose Hierarchical Active Region Pruning (HARP), an efficient train-based selector that preserves downstream alignment while reducing selection cost. HARP organizes the training pool into a node-leaf hierarchy, evaluates only representative leaves, and infers unmeasured utilities with empirical Bayes posteriors. It then selects data using two complementary envelopes: HARP-C, which conservatively controls redundancy, and HARP-E, which additively rewards complementary regions. We theoretically show that, under local smoothness and bounded estimation error, HARP controls selection error while reducing train-evaluate cost. Across 3 base models, 3 finetuning datasets, and 4 reasoning benchmarks (36 settings), HARP variants achieve the highest accuracy among ranked methods in 23 settings and obtain 36-setting mean accuracies of 64.2 and 63.5, respectively, compared with 59.3 for the strongest baseline, NICE. HARP-C trains on roughly 9x fewer examples than the budgeted baselines and 75x fewer than full finetuning, combining higher mean accuracy with a smaller mean training-set size than every ranked baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 15 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: pruning
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Ning Wang, Zhengxin Zhang, Maosen Tang, Yitang Gao, Claire Cardie, Sainyam Galhotra
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
