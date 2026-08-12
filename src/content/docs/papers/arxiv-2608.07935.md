---
title: "Adaptive Supervised Anchoring for On-Policy Self-Distillation"
description: "On-policy self-distillation (OPSD) adapts a language model by distilling guidance from a frozen teacher on trajectories sampled from the student."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.07935) · [PDF](https://arxiv.org/pdf/2608.07935)

## 一句话摘要

On-policy self-distillation (OPSD) adapts a language model by distilling guidance from a frozen teacher on trajectories sampled from the student.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-policy self-distillation (OPSD) adapts a language model by distilling guidance from a frozen teacher on trajectories sampled from the student. Its effectiveness, however, depends critically on the quality of those trajectories. We show that when student rollouts drift from target trajectories, conditioning the teacher on off-target prefixes substantially weakens its task-relevant supervision. Controlled prefix-corruption experiments expose this failure mode, which we term rollout-conditioned signal degradation. To address this problem, we propose a unified training framework that separates two complementary supervision pathways. The first retains rollout-conditioned distribution matching, providing guidance on states the student actually visits. The second applies supervised cross-entropy on canonical ground-truth contexts, avoiding the incompatibility of imposing target tokens on erroneous rollout prefixes. Token-level rollout-target alignment is used to adapt the strength of the canonical-context anchor, emphasizing it during cold start and relaxing it as rollout quality improves. Experiments across multiple model scales, two task families, and general-reasoning benchmarks show that the proposed approach improves task acquisition over OPSD while preserving general capabilities, resulting in a more favorable empirical plasticity-stability trade-off. These findings identify context quality as a central bottleneck in on-policy self-distillation and demonstrate the value of separating rollout-conditioned guidance from canonical supervision.

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

- 作者：Meilin Yang (Renmin University of China, Beijing, China), Zixuan Ding (Renmin University of China, Beijing, China), Jianhao Nie (Renmin University of China, Beijing, China), Weite Zhang (Renmin University of China, Beijing, China), Yuxin Zhang (Renmin University of China, Beijing, China), Zhiming Shao (Renmin University of China, Beijing, China), Li Yu (Renmin University of China, Beijing, China), Zhe Fu (Renmin University of China, Beijing, China)
- 发布：2026-08-11；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
