---
title: "Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It"
description: "We study training-inference mismatch in reinforcement learning with verifiable rewards (RLVR) for large language models, where rollouts are sampled by an inference engine while gradients are computed by a training engine, and the two engines assign different probabilities to the same tokens."
---

**评分：43/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.32444) · [PDF](https://arxiv.org/pdf/2609.32444)

## 一句话摘要

We study training-inference mismatch in reinforcement learning with verifiable rewards (RLVR) for large language models, where rollouts are sampled by an inference engine while gradients are computed by a training engine, and the two engines assign different probabilities to the same tokens.

## 为什么值得关注

待编辑增强。

## 摘要原文

We study training-inference mismatch in reinforcement learning with verifiable rewards (RLVR) for large language models, where rollouts are sampled by an inference engine while gradients are computed by a training engine, and the two engines assign different probabilities to the same tokens. To account for this discrepancy in policy updates, we introduce calibrated importance sampling (CIS). CIS is motivated by an empirically supported logit-displacement characterization that expresses the mismatch as an additive displacement $\varepsilon_t$ in log-odds, determined by the per-logit perturbation before the softmax, whose distribution is approximately invariant to token confidence. This characterization motivates a confidence-aware truncation: large positive displacements are truncated at a single constant threshold, which maps back to an importance-ratio cap that tightens as token confidence increases. Theoretically, we show that CIS replaces the unbounded second moment that governs the error of exact importance sampling with a term bounded by a constant, at the cost of a bias controlled by the truncated excess. In evaluation across three mixture-of-experts models and five mathematical reasoning benchmarks, CIS achieves the highest five-benchmark average on all three models among the evaluated baselines. Diagnostic analyses show that CIS places less truncation bias on low-confidence tokens than truncated importance sampling, while upward clipping of small importance weights reduces held-out accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: inference engine
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianrun Yu, Kaixiang Zhao, Shangzhe Li, Yuxiao Yang, Porter Jenkins, Weitong Zhang, Taylor W. Killian
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
