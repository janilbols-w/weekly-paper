---
title: "VGFM: Expressive Robot Policies via Dense Value Guidance in Flow Matching"
description: "Recent robot learning paradigms increasingly rely on large offline datasets of robotic interactions to train control policies."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.14261) · [PDF](https://arxiv.org/pdf/2609.14261)

## 一句话摘要

Recent robot learning paradigms increasingly rely on large offline datasets of robotic interactions to train control policies.

## 为什么值得关注

待编辑增强。

## 摘要原文

Recent robot learning paradigms increasingly rely on large offline datasets of robotic interactions to train control policies. Expressive generative models enable rich and multimodal action representations, expanding the capability of this paradigm for complex robotic control. However, policy improvement with multi-step generative actors remains challenging. In offline reinforcement learning (RL), incorporating value-based objectives along generative trajectories often introduces substantial training complexity, including backpropagation through time (BPTT), auxiliary architectures, or distillation losses. We propose Value-Guided Flow Matching (VGFM), a scalable offline RL framework that enables dense value-guided shaping within a flow-based policy while avoiding BPTT and additional algorithmic overhead. VGFM parameterizes the policy as a conditional flow-matching model in action (x-prediction) space, ensuring that each intermediate flow step produces a valid robot action that can be directly evaluated by a standard offline RL critic. This design allows value guidance to be applied at randomly sampled flow times without differentiating through the entire generative trajectory, while preserving inference-time flexibility by varying the discretization of the underlying flow ODE without retraining. Evaluated on robotic locomotion and manipulation tasks in OGBench, VGFM achieves strong performance across a wide range of tasks under rigorous evaluation protocols. With minimal hyperparameter tuning, these results demonstrate that VGFM provides a simple, scalable, and effective approach for expressive policy learning in long-horizon, goal-oriented robotic control.

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

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Prajwal Koirala, Mark Campbell
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
