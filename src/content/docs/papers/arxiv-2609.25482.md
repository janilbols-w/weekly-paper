---
title: "Terminal Shrinkage Averaging Reveals a Schedule-Estimator Interaction in LLM Pretraining"
description: "Large language model (LLM) pretraining conventionally returns the raw final iterate."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.25482) · [PDF](https://arxiv.org/pdf/2609.25482)

## 一句话摘要

Large language model (LLM) pretraining conventionally returns the raw final iterate.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) pretraining conventionally returns the raw final iterate. This couples two design choices: the learning-rate schedule that generates the parameter trajectory and the estimator that constructs the deployed model (e.g. the raw final iterate or a checkpoint average). A schedule that promotes optimization progress may differ from one that minimizes variation in the raw final iterate. Separating these choices creates an opportunity to maintain progress late in training while reducing variation in the returned model. To this end, we propose \emph{Terminal Shrinkage Averaging (TSA)}, which interpolates between the raw final iterate and the average of recent checkpoints to balance recent progress against terminal variation. We analyze how TSA changes the preferred terminal learning-rate schedule under a local quadratic approximation and test this interaction through a sequence of controlled NanoChat experiments. Finally, we demonstrate that the resulting gains transfer to depth-22 NanoChat, where the combined schedule and estimator improve validation quality. A qualifying time-to-GPT-2 run also finishes faster than the public baseline used in our experiments, providing preliminary evidence of benchmark acceleration.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Adam Ousherovitch, Yixin Wang
- 发布：2026-09-21；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
