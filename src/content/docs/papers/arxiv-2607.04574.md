---
title: "A Few Teacher Steps Go a Long Way: Efficient SFT Data Collection for LLM Agents"
description: "DAgger-style supervised finetuning (SFT) combines full teacher demonstrations with teacher continuations of partial student rollouts, providing supervision on contexts the student encounters."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2607.04574) · [PDF](https://arxiv.org/pdf/2607.04574)

## 一句话摘要

DAgger-style supervised finetuning (SFT) combines full teacher demonstrations with teacher continuations of partial student rollouts, providing supervision on contexts the student encounters.

## 为什么值得关注

待编辑增强。

## 摘要原文

DAgger-style supervised finetuning (SFT) combines full teacher demonstrations with teacher continuations of partial student rollouts, providing supervision on contexts the student encounters. We study how to allocate the teacher-inference budget on these on-policy (OP) continuations after initial behavior cloning (BC). One existing collection recipe runs the teacher to termination and retains only successful continuations (OP-Success). Since rejected outputs still incur teacher-inference costs, we compare this recipe with shorter continuations without outcome filtering (OP-Short), and with continuing only failed learner rollouts while retaining successful continuations (OP-Critical). We evaluate these choices against acquiring additional full demonstrations, tracking total teacher-inference cost separately from retained training tokens. Across HotpotQA, ALFWorld, and OpenThoughts-TB-Dev, teacher continuations improve the accuracy-cost tradeoff over scaling full demonstrations. On HotpotQA and OpenThoughts-TB-Dev, OP-Short surpasses the strongest tested BC baseline while reducing estimated teacher-inference cost by 20% and 83%, respectively, and on ALFWorld five-step continuations cut teacher tokens by 22% relative to full continuations with little accuracy loss. Controlled HotpotQA ablations show that by focusing on failed student rollouts, OP-Critical achieves comparable accuracy to OP-Success with 30% lower estimated teacher-inference cost and 36% fewer retained training tokens. Compute-matched comparisons with reinforcement learning and on-policy distillation further support brief teacher continuations as an efficient and lightweight post-training recipe.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junze Ye, Jiayi Cheng, Miao Lu, Michal Mankowski, Jose Blanchet, Mohsen Bayati
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
