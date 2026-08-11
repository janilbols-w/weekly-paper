---
title: "The Replay Gap: Static Evaluation of Model Switching in LLM Agents Scores the Wrong World"
description: "LLM routers promise efficiency by matching each request to the cheapest adequate model, and are increasingly applied per step inside multi-step agents."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.08239) · [PDF](https://arxiv.org/pdf/2608.08239)

## 一句话摘要

LLM routers promise efficiency by matching each request to the cheapest adequate model, and are increasingly applied per step inside multi-step agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM routers promise efficiency by matching each request to the cheapest adequate model, and are increasingly applied per step inside multi-step agents. Yet agentic routers are evaluated like single-turn routers: by replaying logged trajectories and substituting another model's recorded outputs, assuming the rest of the trajectory is unaffected. We test this assumption with branching rollouts: we fork live SWE-bench agent trajectories at controlled points, rebuild the environment, continue each fork with a different model, and compare against same-model control forks that isolate sampling and replay noise. Across six paired runs (~900 rollouts), swaps exceed their matched control floors by +0.25 to +0.66 normalized edit distance (multiplicity-corrected CIs exclude zero), rewriting 61-94% of post-fork actions; 74-77% of early swaps diverge at the first post-fork action, versus 6-35% of controls, leaving only 3% of replayed states valid. Divergence decreases with fork depth in both directions. All five outcome flips we observe occur in swap arms, upgrades rescuing unsolved instances and a downgrade losing the sole solve, and zero occur across 359 control forks. Scoring these same swaps with a log-stitching replay evaluator, replay mispredicts every success-relevant outcome call and predicts patches with 0.00-0.11 similarity to reality. Auditing the noise floor, temperature-0 "determinism" is configuration-dependent: FP8-served controls diverge on over 90% of forks while AWQ-served ones remain near-identical; and under tight budgets the stronger model more often exhausts its steps without submitting. Replay-based benchmarks score the wrong world for agentic routing; we release our harness and all trajectories.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: fp8
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Ashritha Gonuguntla
- 发布：2026-08-11；更新：2026-08-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
