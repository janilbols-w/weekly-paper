---
title: "Proxy OPD: On-Policy Distillation with Transferable Relative Proxy Update for Large Language Models"
description: "Reward-based reinforcement learning (RL) improves large language models but incurs substantial costs when repeated across targets."
---

**评分：41/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.11505) · [PDF](https://arxiv.org/pdf/2607.11505)

## 一句话摘要

Reward-based reinforcement learning (RL) improves large language models but incurs substantial costs when repeated across targets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reward-based reinforcement learning (RL) improves large language models but incurs substantial costs when repeated across targets. On-policy distillation (OPD) reuses experts by matching their distributions on target-generated trajectories, yet differing base policies can confound reward-induced updates with pre-existing policy differences, potentially distorting transferred update directions. We propose Proxy OPD (P-OPD), a post-training method that transfers reward-induced relative policy updates using the target's frozen base policy as a reference. A proxy undergoes reward-guided exploration, yielding token-level log-probability changes between its initial and optimized policies. These signals guide learning on target-generated trajectories, with calibration controlling signal absorption, enabling reuse of reward-induced improvements across targets. Experiments on Qwen3-family targets in mathematical reasoning, code generation, and instruction following show that P-OPD improves targets and outperforms conventional OPD in most settings. For 1.7B-to-8B transfer, average Math Mean@16 and Code Mean@8 scores exceed OPD by 8.3 and 3.4 points, respectively. Mechanism analyses show more faithful reward-induced supervision and controllable adaptation. Cross-scale and cross-generation experiments confirm signal transferability and reusability, while multi-domain distillation reveals synergistic gains and cross-domain interference. In the measured 4B-to-8B setting, target adaptation after proxy exploration takes approximately 15\% of direct target RL time; repeated signal reuse amortizes the one-time exploration cost across compatible models. These findings support relative policy updates as effective, transferable, and composable supervision for an ``explore once, transfer multiple times'' post-training paradigm.

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

- 作者：Daocheng Fu, Rong Wu, Yu Yang, Jianbiao Mei, Licheng Wen, Pinlong Cai, Xuemeng Yang, Yong Liu, Botian Shi, Yu Qiao
- 发布：2026-08-11；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
