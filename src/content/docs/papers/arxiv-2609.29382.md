---
title: "Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs"
description: "Flow-matching Vision-Language-Action (VLA) models have emerged as a potential solution for generalist robot control, designed by combining a pretrained Vision-Language Model (VLM) backbone with an action expert that generates continuous robot actions."
---

**评分：38/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.29382) · [PDF](https://arxiv.org/pdf/2609.29382)

## 一句话摘要

Flow-matching Vision-Language-Action (VLA) models have emerged as a potential solution for generalist robot control, designed by combining a pretrained Vision-Language Model (VLM) backbone with an action expert that generates continuous robot actions.

## 为什么值得关注

待编辑增强。

## 摘要原文

Flow-matching Vision-Language-Action (VLA) models have emerged as a potential solution for generalist robot control, designed by combining a pretrained Vision-Language Model (VLM) backbone with an action expert that generates continuous robot actions. While these models exhibit impressive capabilities, due to their very high number of parameters, their computational requirements are often prohibitive for robotics control. To mitigate these inefficiencies, existing methods predominantly skip VLM backbone layers with early exits or reduce denoising steps, while leaving action expert depth untouched. We propose a framework that exposes backbone depth $V$, action expert depth $A$, and denoising steps $D$ as three jointly configurable compute axes in a VLA. Starting from a pretrained VLA, we attach lightweight Exit Transformers (ET) at intermediate depths in both the backbone and the action expert, trained to distil the last layer of the policy into each exit. Furthermore, we introduce a KV Cache synthesis mechanism that manages the missing keys and values of the skipped backbone layers, allowing the action expert to exit deeper than the backbone. Finally, we show that the optimal compute budget is task-dependent, with different tasks benefiting from different axes and depths. Notably, our method does not require training the original policy from scratch, and for each exit, it increases the number of parameters by only $2.1\%$ for SmolVLA and $4.1\%$ for $\pi_{0.5}$. We validate our approach across two flow-matching VLAs (SmolVLA, $\pi_{0.5}$) and two benchmarks (LIBERO, Meta-World), revealing complementary effects: $V$ and $A$ respectively reduce FLOPs and latency, while $D$ improves both. Our joint configurations $(V,A,D)$ reduce latency by $79.2\%$ and computation (FLOPs) by $31.8\%$, while improving mean success rate by $5.6\%$.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Riccardo Andrea Izzo, Rimvydas Rubavicius, Gianluca Bardaro, Subramanian Ramamoorthy, Matteo Matteucci, Alessandro Suglia
- 发布：2026-09-24；更新：2026-09-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
