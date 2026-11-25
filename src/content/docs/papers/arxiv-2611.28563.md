---
title: "Selective ROM Weight Storage for Responsive LLM Control on Edge Robots"
description: "Edge robots increasingly use large language models (LLMs) for complex tasks, demanding efficient inference alongside timely control."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.28563) · [PDF](https://arxiv.org/pdf/2611.28563)

## 一句话摘要

Edge robots increasingly use large language models (LLMs) for complex tasks, demanding efficient inference alongside timely control.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge robots increasingly use large language models (LLMs) for complex tasks, demanding efficient inference alongside timely control. Limited memory capacity constrains model deployment, while repeated weight transfers during decoding compete with activations and KV cache for external bandwidth. Sequential generation of robot actions further delays decisions and periodic control on shared hardware. We present a hybrid memory architecture with heterogeneous scheduling to address these bottlenecks jointly. Banked ROM stores selected fixed weights and supplies a standard compute array through a dedicated datapath. LPDDR retains the remaining weights and mutable state, preserving model flexibility. Coordinated operand delivery and preemption at output slice boundaries accelerate inference while limiting interference with periodic control. A structured decision interface scores candidate phases in a single forward pass, avoiding sequential token generation for routine choices. Together, these mechanisms improve memory service, compute access, and decision execution for edge robotic workloads. Experiments with Qwen3-8B achieve a peak decode speedup of 1.56$\times$ and reduce P99 task response time by a factor of approximately 227.27$\times$, while completing 100.00\% of the tested grasping and transport tasks.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Boxiang Song, Zhihong Chen, Xiaoyu Hao, Jinhong Huang, Chengkai Zhu, Jiaqi Yang, Hongyang Pan, Changhao Yan, Keren Zhu
- 发布：2026-11-24；更新：2026-11-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
