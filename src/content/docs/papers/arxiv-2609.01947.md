---
title: "On-Policy Distillation Meets Off-Policy GRPO: Training Compact Instruction-Following Rerankers"
description: "Compact instruction-following rerankers are attractive for deployment, but conventional distillation pipelines typically train students by offline imitation of teacher outputs on a fixed set of examples, constraining supervision to the teacher's observed ranking space."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.01947) · [PDF](https://arxiv.org/pdf/2609.01947)

## 一句话摘要

Compact instruction-following rerankers are attractive for deployment, but conventional distillation pipelines typically train students by offline imitation of teacher outputs on a fixed set of examples, constraining supervision to the teacher's observed ranking space.

## 为什么值得关注

待编辑增强。

## 摘要原文

Compact instruction-following rerankers are attractive for deployment, but conventional distillation pipelines typically train students by offline imitation of teacher outputs on a fixed set of examples, constraining supervision to the teacher's observed ranking space. We revisit reranker distillation through the lens of reinforcement learning. We propose a two-stage framework combining off-policy teacher optimization with on-policy student distillation. In Stage 1, a 4B teacher reranker is strengthened with off-policy GRPO using LLM-judge feedback on 88K instruction-following examples. In Stage 2, a compact 1B student samples rankings from its own policy and receives soft teacher-derived rewards on those rankings, coupling student exploration with knowledge transfer. Our strongest gains appear under distribution shift. On MAIR-11, the original 11-subset, 869-query evaluation, the proposed student reaches 0.7670 nDCG@6, outperforming offline listwise KD by +4.6 points. Controlled comparisons against offline pairwise RankNet KD and on-policy GKD show that neither changing the offline distillation objective nor moving teacher-distribution matching on-policy reproduces the performance of reward-based on-policy distillation over student-sampled rankings. The advantage persists on MAIR-Full: across all 126 tasks and 9,356 queries, the proposed method obtains the highest task-macro point estimates among the evaluated distillation variants, reaching 0.6808 nDCG@6 and 0.7865 MRR@6. It also exceeds two released 7B RL-trained rerankers on the comparable MAIR-11 evaluation, while the same Stage 2 training procedure consistently improves three architecturally distinct alternative student backbones. On the 9,861-query validation benchmark, the resulting 1B reranker achieves 0.7624 nDCG@6 while providing a favorable quality-efficiency tradeoff relative to larger alternatives.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Vignesh Prabhakar, Jialing Pan, Anil Babu Ankisettipalli
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
