---
title: "Online Inference for Quantile Distributional Reinforcement Learning"
description: "In this paper, we study online statistical inference for quantile-based distributional policy evaluation, which aims to characterize the distribution of discounted cumulative rewards under a given policy."
---

**评分：39/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2608.12973) · [PDF](https://arxiv.org/pdf/2608.12973)

## 一句话摘要

In this paper, we study online statistical inference for quantile-based distributional policy evaluation, which aims to characterize the distribution of discounted cumulative rewards under a given policy.

## 为什么值得关注

待编辑增强。

## 摘要原文

In this paper, we study online statistical inference for quantile-based distributional policy evaluation, which aims to characterize the distribution of discounted cumulative rewards under a given policy. To obtain a finite-dimensional representation of the return distribution, we consider the fixed point $\bm\eta_m$ of the quantile-projected distributional Bellman equation, parameterized by the quantile vector $\bm\theta_m$. We develop two online inference procedures for $\bm\theta_m$, covering synchronous and asynchronous sampling from a generative model as well as Markovian data. The first method uses the trajectory of quantile temporal-difference learning (QTD). We establish functional central limit theorems for the partial sums of QTD iterates and construct a recursively computable random-scaling statistic. The resulting confidence intervals have asymptotically exact coverage at deterministic horizons, with length of order $T^{-1/2}$ in probability. The second method constructs anytime-valid confidence intervals directly from samples. Exploiting the monotonicity of the quantile Bellman map, we develop a computationally explicit coordinate-shaving algorithm with finite-sample simultaneous coverage. Under positive limiting state-visit frequencies, the resulting confidence intervals have lengths of order $\sqrt{\log\log T/T}$, which we establish as classwise optimal through a matching lower bound. Together, these results provide complementary guarantees for online inference in quantile distributional reinforcement learning, combining asymptotically exact fixed-horizon inference with finite-sample anytime validity.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: online inference
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zijie Cheng, Yang Peng, Zhihua Zhang
- 发布：2026-08-14；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
