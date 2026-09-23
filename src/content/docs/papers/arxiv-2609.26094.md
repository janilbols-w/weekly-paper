---
title: "CoEvo: Oracle-Grounded Self-Evolution of a Single Model for Multi-Step Causal Reasoning"
description: "Multi-step causal reasoning requires chaining inferences where each step constrains the next."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2609.26094) · [PDF](https://arxiv.org/pdf/2609.26094)

## 一句话摘要

Multi-step causal reasoning requires chaining inferences where each step constrains the next.

## 为什么值得关注

待编辑增强。

## 摘要原文

Multi-step causal reasoning requires chaining inferences where each step constrains the next. An early error propagates silently, and a correct answer reached via flawed logic evades outcome-level detection. In specialized domains, teacher LLMs err on intermediate steps, safety constraints restrict cloud distillation, and shifting conditions demand adaptation, leaving self-evolution as the practical route. Naive self-evolution can collapse: outcome-only rewards let the model exploit distributional shortcuts, and weak self-evaluation reinforces spurious paths into stable failure patterns. We exploit a key asymmetry: generating a correct chain is hard, but verifying a single step is easy. Many high-stakes domains admit a deterministic, queryable oracle, a physics simulator or rule engine over codified constraints. It checks asserted steps without teacher-level ability and abstains beyond its rules; it can check what the model asserts, never replace it. This enables CoEvo, an oracle-grounded self-evolution framework where a single model alternates between Proposer and Solver. As Solver, the model generates competing chains; intra-group debate exposes disagreement steps, a proxy for the capability boundary, and the oracle adjudicates them into process-level supervision. As Proposer, the same model constructs progressively harder scenarios inside oracle constraints, steering the curriculum toward deep multi-hop chains. Both roles are updated jointly, so training pressure co-evolves with the model. On industrial, clinical, and legal multi-step causal reasoning benchmarks, CoEvo enables an 8B LLM to sustain self-evolution, surpassing distillation baselines and the strongest proprietary reference on path correctness (82.1% vs. 71.4%). The trained model generalizes to unseen categories and systems, preserving root-cause accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jian Zhang, Bingyi Wang, Yizhi Liu
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
