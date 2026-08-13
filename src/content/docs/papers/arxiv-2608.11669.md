---
title: "Rubric Dropout: A Simple Way to Mitigate Reward Hacking in Rubric-as-Reward RL"
description: "Reinforcement learning against rubrics, lists of criteria graded by an LLM judge, has become a standard way to post-train language models on tasks with no deterministic answer."
---

**评分：39/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2608.11669) · [PDF](https://arxiv.org/pdf/2608.11669)

## 一句话摘要

Reinforcement learning against rubrics, lists of criteria graded by an LLM judge, has become a standard way to post-train language models on tasks with no deterministic answer.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning against rubrics, lists of criteria graded by an LLM judge, has become a standard way to post-train language models on tasks with no deterministic answer. The rubric, however, is a fixed proxy for quality, never a complete description of it, and a policy trained against it long enough will learn to exploit the difference. We measure this directly. Training Qwen3-8B with Group Relative Policy Optimization (GRPO) on medical and science rubrics and grading out-of-distribution (OOD) benchmarks with both the training judge and a stronger gold judge, we find that the two scores diverge during training. The training judge's score keeps climbing while the gold judge's score peaks and then falls, by 3 points on HealthBench-Hard and by 22 points on ResearchQA. A judge with a fixed bias would shift the gold curve by a constant, not send it down while the training score rises, so the divergence is reward hacking, not judge noise. We propose Rubric Dropout, a one-line fix borrowed from neuron dropout. At every step, we randomly drop a subset of the rubric's criteria before computing the reward, so the policy never optimizes the same rubric twice. The dropped subset is shared across each rollout group, so GRPO's group-relative advantages stay comparable, and evaluation always uses the full rubric. Comparing no dropout against dropout at 30% and 50% on both benchmark pairs, dropout raises the OOD gold score at every matched checkpoint (+1 to +2 points on HealthBench-Hard, +6 to +7 points on ResearchQA), lowers the two hacking measures we track, and costs nothing in domain. Sweeping the dropout fraction shows a broad 30-50% sweet spot, while the natural alternative, reweighting criteria by how useful they are to training, performs worse than no intervention at all in our setting.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minglai Yang, Xinyu Guo, Utkarsh Tyagi, Mian Zhang, Razvan Dumitru, Sunjie Hou, Yunzhong He, Daniel Yue Zhang, Ying Liu
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
