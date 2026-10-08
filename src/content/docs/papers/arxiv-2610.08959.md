---
title: "GraphOPD: Graph-Augmented On-Policy Distillation for LLM Agents"
description: "On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the reinforcement-learning reward is sparse and arrives only once per trajectory."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.08959) · [PDF](https://arxiv.org/pdf/2610.08959)

## 一句话摘要

On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the reinforcement-learning reward is sparse and arrives only once per trajectory.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy distillation post-trains large language model agents by supplying dense, step-level guidance from a teacher policy when the reinforcement-learning reward is sparse and arrives only once per trajectory. Existing instantiations allocate this guidance by the size of the teacher-student divergence at each step, on the single-turn intuition that a large disagreement marks a mistake worth correcting. Once decisions chain over many turns, that rule misfires, since an early drift enters every later context both policies condition on, leaving the teacher consistent with the drifted trajectory instead of flagging its cause, while interchangeable steps register large but outcome-irrelevant divergences. We demonstrate this on an agentic benchmark, where distilling the highest-divergence steps brings no consistent benefit over random selection. To this end, we introduce GraphOPD, the first method to bring graph-based structural augmentation into on-policy distillation for agent capabilities. It reads which steps enabled which later ones from the environment's own record of state changes, immune to the drift that corrupts the teacher-student gap, organizes them into a dependency graph, scores each step by a random-walk stationary distribution over it, and fuses that structural credit with the divergence signal into a trajectory-relative mask concentrating supervision on each rollout's highest-aptitude steps. Across three model scales and eleven baselines on ALFWorld, WebShop, and SearchQA, GraphOPD shows competitive performance throughout, improving over the strongest baseline by up to +5.8 pp. An executed-replay audit further shows that this structural credit score tracks true causal impact far above chance, that both fused signals are independently necessary, and that the same signal transfers to out-of-domain tool-integrated reasoning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 9 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Bohan Lin, Liyi Chen, Zhuoning Guo, Muyang Li, Qimeng Wang, Yan Gao, Yao Hu, Yudong Zhang
- 发布：2026-10-08；更新：2026-10-08
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
