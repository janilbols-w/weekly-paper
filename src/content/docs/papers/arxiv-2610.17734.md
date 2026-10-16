---
title: "Explore with Memory, Learn without It: In-Context Exploration and Self-Distillation for LLM Reasoning"
description: "Exploration bounds learning efficiency in reinforcement learning with verifiable rewards (RLVR)."
---

**评分：51/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](http://arxiv.org/abs/2610.17734v1) · [PDF](https://arxiv.org/pdf/2610.17734v1)

## 一句话摘要

Exploration bounds learning efficiency in reinforcement learning with verifiable rewards (RLVR).

## 为什么值得关注

待编辑增强。

## 摘要原文

Exploration bounds learning efficiency in reinforcement learning with verifiable rewards (RLVR). Current methods explore mostly through independent sampling, without fully using the information gathered along the way, such as known wrong answers and environment feedback. We propose LEAF, which injects a dynamic, problem-specific memory into the context before every rollout. The memory contains the most recent response, its reward, and other environment feedback. It is updated after every verifier call. We decouple policy updates from rollouts and update the policy through self-distillation. On four benchmarks and two open models, LEAF accelerates exploration by about 4x compared with a random sampling baseline. On unseen test sets, it improves accuracy over the strongest baseline by 1.59 and 1.83 percentage points on the two models, while using less compute than any RL baseline. These results highlight the potential of LEAF in improving both exploration and learning efficiency. Code is available at: https://github.com/on1262/LEAF

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 10 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Yutong Chen, Zhichao Xu, Rui Liu, Kunpeng Liu
- 发布：2026-10-13；更新：2026-10-13
- 来源：arXiv；Venue：未确认
- 代码：[https://github.com/on1262/LEAF](https://github.com/on1262/LEAF)
- 阅读深度：metadata
