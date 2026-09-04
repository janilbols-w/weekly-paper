---
title: "APEx: Distillation of Agent Procedural Experience for Adaptive Deep Research Question Answering"
description: "Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.02253) · [PDF](https://arxiv.org/pdf/2609.02253)

## 一句话摘要

Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deep research agents augment large language models with external tools to answer complex, long-horizon questions through multi-turn reasoning. Learning from prior experience is crucial for continual improvement, yet existing methods either retrieve verbose task-specific traces that burden decision-making, or distill procedural skills that remain decoupled from downstream policy adaptation. We propose APEx, a hierarchical experience utilization framework that organizes interaction history into instance-level trajectory memories and category-level procedural skills, and couples them through a closed-loop architecture of Executor, Distiller, and Planner. The three modules are optimized via a three-stage alternating GRPO training paradigm, enabling reward-guided skill distillation rather than fixed-prompt generation. At test time, distilled skills serve as procedural priors for online Planner adaptation through skill-guided test-time reinforcement learning, allowing ground-truth-free self-improvement with skill-alignment regularization to prevent policy drift. Experiments on 7 benchmarks demonstrate that APEx achieves state-of-the-art performance, surpassing GPT-5.4 by 14.7 points and the strongest memory-augmented baseline by 3.0 points.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jie Ding, Rui Sun, Xinyuan Zhang, Zeyu Zhang, Xin Liu
- 发布：2026-09-02；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
