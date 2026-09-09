---
title: "DISEIL: Demonstration Distillation for Sample-Efficient Imitation Learning"
description: "A robot that can be taught a new task from a handful of demonstrations has to work out for itself what it still cannot do, and then ask for exactly that."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.08123) · [PDF](https://arxiv.org/pdf/2609.08123)

## 一句话摘要

A robot that can be taught a new task from a handful of demonstrations has to work out for itself what it still cannot do, and then ask for exactly that.

## 为什么值得关注

待编辑增强。

## 摘要原文

A robot that can be taught a new task from a handful of demonstrations has to work out for itself what it still cannot do, and then ask for exactly that. Interactive imitation learning takes a step in that direction by letting a policy practice on its own and calling an expert when it goes wrong. Existing methods decide when to interrupt the learner. A further 2 decisions are left to whichever episode happened to trigger the interruption: which failure to correct, and where the demonstration should start. This paper is a first attempt at making both of them deliberately. DISEIL (Demonstration dIstillation for Sample-Efficient Imitation Learning) marks each failed episode at the step where the policy first becomes unreliable, represents that moment with a geometric descriptor, and groups the failures into recurring failure modes. A vision-language model and a language model read the selected mode and write a request for the next demonstration, and a store of task constraints checks that the request can be carried out before any expert time is spent. No model produces a robot action. Across 5 simulated tasks under state and image observations, changing only what the expert is asked for gives the highest mean held-out success rate in all 10 settings, with a tie in 1, and the margin is widest at the smallest budget we tested. The scope is narrow: a single round of practice at a time, in simulation, with experts that are mostly scripted. The longer-term aim is a learner that also tracks what its demonstration set already covers, and that asks a human teacher for the missing behavior in proportion to the effort each request costs them.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Suyog Khanal, Arun Kumar A V, Santu Rana
- 发布：2026-09-09；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
