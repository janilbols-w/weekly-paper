---
title: "WiSDoM: Wireless Sparse Decision Transformer with Mixture-of-Experts for Multi-Task Mobile Network Optimization"
description: "Emerging 6G wireless networks are expected to operate across diverse deployment scenarios, where variations in network topology, user mobility, traffic demand, and radio conditions challenge the scalability of conventional radio resource management (RRM)."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > MoE 路由与专家优化

[论文原文](https://arxiv.org/abs/2609.00284) · [PDF](https://arxiv.org/pdf/2609.00284)

## 一句话摘要

Emerging 6G wireless networks are expected to operate across diverse deployment scenarios, where variations in network topology, user mobility, traffic demand, and radio conditions challenge the scalability of conventional radio resource management (RRM).

## 为什么值得关注

待编辑增强。

## 摘要原文

Emerging 6G wireless networks are expected to operate across diverse deployment scenarios, where variations in network topology, user mobility, traffic demand, and radio conditions challenge the scalability of conventional radio resource management (RRM). While offline reinforcement learning (RL) methods have demonstrated strong decision-making capabilities, learning a single policy that performs consistently across heterogeneous wireless environments remains difficult due to conflicting optimization objectives and limited model specialization. These challenges become particularly pronounced in coordinated multipoint (CoMP) transmission, where selecting the optimal serving-cell combination requires sequential decision-making under evolving network conditions. This paper presents the Wireless Sparse Decision Transformer with Mixture of Experts (WiSDoM), a sparse multi-task offline RL framework for adaptive multi-cell selection. WiSDoM combines Decision Transformers (DTs) with a Mixture-of-Experts (MoE) architecture that dynamically activates specialized experts according to task characteristics. This MoE mechanism improves model capacity without proportionally increasing inference cost, mitigates negative transfer, and enables expert specialization across tasks. WiSDoM is trained jointly on diverse network configurations spanning multiple base station and user equipment densities, mobility levels, and scheduler policies. Experimental results show that WiSDoM consistently outperforms heuristic methods, single-task models, and conventional multi-task DTs, improving quality of experience (QoE) by up to 55% while activating approximately one-third of the parameters of its dense counterpart during inference. Furthermore, WiSDoM exhibits strong task generalization and efficiently adapts to unseen wireless scenarios through few-shot prompting without retraining or fine-tuning.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: mixture of experts
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Fatih Temiz, Shavbo Salehi, Melike Erol-Kantarci
- 发布：2026-08-31；更新：2026-09-02
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
