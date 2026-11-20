---
title: "One Checkpoint, Many Runs: Recipe Cards for Fine-Tuned Models"
description: "Fine-tuned language models are shared with model cards that describe the training setup in detail, often down to the default random seed, but report the score of a single released checkpoint."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2610.16825) · [PDF](https://arxiv.org/pdf/2610.16825)

## 一句话摘要

Fine-tuned language models are shared with model cards that describe the training setup in detail, often down to the default random seed, but report the score of a single released checkpoint.

## 为什么值得关注

待编辑增强。

## 摘要原文

Fine-tuned language models are shared with model cards that describe the training setup in detail, often down to the default random seed, but report the score of a single released checkpoint. Such setups are retrained routinely, by fine-tuning services for each customer, by organizations at each update, and by users on their own data, so the model that is deployed comes from a new run of the setup. Some runs fail, and a failed run can go unnoticed and reach the people the model serves. We call such a setup a model recipe and argue that its documentation should state how often a run of the recipe misses a required performance bar. In a survey of the model cards of 300 fine-tuned language models on Hugging Face, none reports this failure probability, and only three report results from more than one training run. Across 2,124 fine-tuning runs, we find that reading the mean, the median, or a bootstrap interval as an approval often approves recipes whose failure rate exceeds a stated failure tolerance, because these summaries do not measure how often a run fails. Model cards do not report how often the runs of a recipe fail, although whoever runs the training is best placed to count them, while those who rely on a retrained model bear the cost of a failed run. To report this failure probability directly, we propose recipe cards, an addendum to model cards that documents the model recipe behind a checkpoint. A recipe card states the bar and the tolerance and who chose them, reports how many runs are made and how many of them miss the bar, gives an upper bound on the failure probability, and warns when this bound exceeds the tolerance. Recipe cards record who set and who accepted this risk, and let deployers and regulators state acceptance criteria for retrained models.

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

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jaewon Choi, Jihye Kang, Namhyuk Ahn
- 发布：2026-11-19；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
