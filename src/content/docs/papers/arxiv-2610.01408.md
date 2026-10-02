---
title: "Smoother Flow Matching via Contrastive Trajectory Repulsion"
description: "Trajectory crossing remains a critical bottleneck in Flow Matching (FM), and previous works typically view these crossings from a theoretical optimization perspective causing velocity averaging."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2610.01408) · [PDF](https://arxiv.org/pdf/2610.01408)

## 一句话摘要

Trajectory crossing remains a critical bottleneck in Flow Matching (FM), and previous works typically view these crossings from a theoretical optimization perspective causing velocity averaging.

## 为什么值得关注

待编辑增强。

## 摘要原文

Trajectory crossing remains a critical bottleneck in Flow Matching (FM), and previous works typically view these crossings from a theoretical optimization perspective causing velocity averaging. They attempt to address it indirectly by post-hoc distillation or endpoint coupling, without explicitly regulating the intermediate trajectories. In this paper, we introduce a new network learning perspective: crossing points inherently induce large local Lipschitz constants in the target velocity field, leading to two drawbacks. First, high Lipschitz constants correspond to high-frequency signals in the velocity field that neural networks struggle to fit due to spectral bias. Second, they also imply drastic velocity variations, leading to severe numerical integration errors in few-step inference. To alleviate this, we propose CoFlow, a framework that introduces the contrastive learning paradigm into FM to explicitly repel trajectories during training, thereby lowering the local Lipschitz constants of the velocity field. Specifically, we formulate CoFlow from a Stochastic Differential Equation (SDE) perspective by injecting a repulsive drift term. This drift actively guides the forward process of positive samples away from negative trajectories, effectively reducing the local Lipschitz constant. Furthermore, we derive an equivalent stochastic interpolant formulation from this SDE, providing a simple and tractable design space to control the influence of negative samples. Extensive experiments on ImageNet 256x256 demonstrate that CoFlow significantly reduces FID compared to standard FM in few-step inference (e.g., 20 steps), with no added training overhead. The code can be accessed at: https://github.com/HKUST-LongGroup/CoFlow

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- code/artifact link detected

## 元数据

- 作者：Ziqi Jiang, Zhenqi He, Long Chen
- 发布：2026-10-02；更新：2026-10-02
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/HKUST-LongGroup/CoFlow](https://github.com/HKUST-LongGroup/CoFlow)
- 阅读深度：metadata
