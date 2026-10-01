---
title: "Disentangling Self-Distillation: Measuring and Modeling Acquisition and Retention"
description: "Self-distillation with privileged context adapts a language model from demonstrations by letting the model, once conditioned on a reference response, teach its context-free copy token by token."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.39494) · [PDF](https://arxiv.org/pdf/2609.39494)

## 一句话摘要

Self-distillation with privileged context adapts a language model from demonstrations by letting the model, once conditioned on a reference response, teach its context-free copy token by token.

## 为什么值得关注

待编辑增强。

## 摘要原文

Self-distillation with privileged context adapts a language model from demonstrations by letting the model, once conditioned on a reference response, teach its context-free copy token by token. Our taxonomy reveals existing methods differ along three entangled axes: (i) the rollout source (student or teacher), (ii) the teacher coupling (frozen, or an exponential moving average of the student at some coupling rate) and (iii) the KL direction (reverse or forward), yet these axes are usually studied in fixed combinations and have led to conflicting conclusions. We formalize a unifying framework to encompass all self-distillation methods vs classic supervised fine-tuning: we train every combination of the three axes, on Qwen2.5-7B and Ministral-3-3B across ordinary and contradictory tasks, totaling 1,200 adaptation runs, to systematically investigate the impact of the above axes. We propose a controlled model of the same objective to explain the resulting acquisition-retention trade-offs. We find that (i) the rollout source matters mostly where the task contradicts the pretrained behavior: there teacher rollouts raise acquisition well above what student rollouts achieve, with almost no change in retention; (ii) the teacher coupling changes acquisition most, on every task: acquisition rises with the coupling rate, then falls past a task-specific rate; (iii) switching the KL direction costs retention in one model but not the other so which axis to tune first depends on the model. The controlled model reproduces the three trends.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Luis Zuin, Alexis Huet, Dario Rossi, Zied Ben Houidi
- 发布：2026-10-01；更新：2026-10-01
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
