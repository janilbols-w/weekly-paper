---
title: "Internalize the Temperature: On-Policy Self-Distillation as Policy Reheater for Reinforcement Learning"
description: "Reinforcement learning from verifiable rewards improves the reasoning ability of large language models, but often suffers from entropy collapse, in which increasingly concentrated policies reduce rollout diversity and useful learning signals."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2606.00755) · [PDF](https://arxiv.org/pdf/2606.00755)

## 一句话摘要

Reinforcement learning from verifiable rewards improves the reasoning ability of large language models, but often suffers from entropy collapse, in which increasingly concentrated policies reduce rollout diversity and useful learning signals.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning from verifiable rewards improves the reasoning ability of large language models, but often suffers from entropy collapse, in which increasingly concentrated policies reduce rollout diversity and useful learning signals. Existing remedies either constrain the RL objective (e.g., entropy regularization) or adjust sampling temperature during rollout collection, but these interventions remain external to the model parameters. We propose Temperature-Scaled On-Policy Self-Distillation (TS-OPSD), a lightweight policy reheating method that internalizes the exploratory effect of temperature into model parameters. Starting from an entropy-collapsed RL checkpoint, TS-OPSD constructs a self-teacher by applying high-temperature scaling to the model's own logits, then distills the resulting smoother distribution back into the student. This policy reheating requires no external teacher, privileged data, or additional inference cost. Experiments on Qwen3-4B-Base and Qwen3-8B-Base show that policy reheating yields a stronger initialization for continued RL than both standard continued RL and rollout-level temperature reheating. Further analyses show that TS-OPSD mainly reduces output sharpness while preserving intermediate representations, top candidate sets, and reasoning capability. These results suggest that entropy restoration can serve as a simple post-collapse intervention for extending reasoning-oriented RL.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Xuewei Yang, Jiachen Yu, Jie Wu, Shaoning Sun, Junjie Wang, Yujiu Yang
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
