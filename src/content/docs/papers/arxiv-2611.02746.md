---
title: "Replay for LLM Continual Learning with Multi-Teacher On-Policy Distillation"
description: "Multi-teacher on-policy distillation (MOPD) distills domain experts into one student but needs every expert at once."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2611.02746) · [PDF](https://arxiv.org/pdf/2611.02746)

## 一句话摘要

Multi-teacher on-policy distillation (MOPD) distills domain experts into one student but needs every expert at once.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-teacher on-policy distillation (MOPD) distills domain experts into one student but needs every expert at once. When domains arrive one at a time and earlier experts are gone, the previous-stage student can teach replayed prompts of earlier domains inside every stage. Some pipelines instead store every stage snapshot for a final multi-teacher recovery stage. On five domains with a 1.5B student and five public experts, this paper compares both with joint MOPD. It varies the replay budget and the replay signal. The signal is token-level distillation alone or with alignment of hidden states, attention and value relations. Sequential distillation without replay or recovery is 6.2 points below 208-step joint MOPD on a 14-benchmark average and 3.5 points below on the 11 benchmarks outside safety. Without snapshots, replay toward the previous student closes 3.8 of the 6.2 points when the earlier domains share the replay budget of a stage. With a fixed share of seven replay steps per earlier domain and stage, it closes 5.8 over two training runs. This is level with the 5.9 of recovery from all snapshots, both at its default length and when given as many training steps as the fixed share. Alignment terms on replay steps change the average by about one point or less. If refusal and compliance count equally in safety, shared-budget replay ranks first among the trained configurations, and the fixed share stays at or above recovery. Against the shared budget, the fixed share lowers the score on the newest domain. Recovery lowers this score as well, in five of six cases. The replay steps of the fixed share grow quadratically with the number of stages.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yiqiao Qiu
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
