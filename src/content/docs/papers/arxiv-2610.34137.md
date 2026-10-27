---
title: "Self-Evolution Reasoner: Continuous Optimization via Policy-Intrinsic Exploration and Exploitation"
description: "Reinforcement learning with verifiable rewards (RLVR) enables large language models (LLMs) to continuously self-improve their reasoning capabilities."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.34137) · [PDF](https://arxiv.org/pdf/2610.34137)

## 一句话摘要

Reinforcement learning with verifiable rewards (RLVR) enables large language models (LLMs) to continuously self-improve their reasoning capabilities.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reinforcement learning with verifiable rewards (RLVR) enables large language models (LLMs) to continuously self-improve their reasoning capabilities. Compared to RLVR's scalar rewards, recent self-supervised on-policy distillation methods leverage denser supervision signals. However, both paradigms suffer from exploration bottlenecks, struggling to escape local optima when the policy fails to sample valid solutions. Relying on external demonstrations can bypass this issue; however, the off-policy nature hinders genuine self-improvement and the mismatched-distribution reasoning can not be fully exploited. In this work, we propose Self-Evolution Policy Optimization (SEPO), a framework that drives continuous reasoning capability evolution via guided exploration and in-distribution exploitation. Specifically, SEPO utilizes labels to elicit correct reasoning from the policy, unlocking the exploration potential. By treating current policy conditioned on this in-distribution reasoning as a self-teacher, SEPO distills the newly discovered solution back into the policy. Through this iterative cycle of policy-intrinsic exploration and exploitation, SEPO achieves robust and continuous capability evolution. Across scientific, tool-use, and complex logical reasoning domains, SEPO consistently achieves the best performance under identical training time or steps, demonstrating superior efficiency and convergence ceilings. Notably, SEPO maintains stable improvements even in scenarios where baselines severely underperform or fail entirely, such as on complex tasks or with small-scale models. Our code is available at https://github.com/Eric8932/SEPO.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Wenhang Shi, Yiren Chen, Zhe Zhao, Jinhao Dong, Wei Lu, Xiaoyong Du
- 发布：2026-10-27；更新：2026-10-27
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/Eric8932/SEPO](https://github.com/Eric8932/SEPO)
- 阅读深度：metadata
