---
title: "KL for a KL: On-Policy Distillation with Control Variate Baseline"
description: "On-Policy Distillation (OPD) has emerged as a dominant post-training paradigm for Large Language Models, especially in reasoning domains."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2605.07865) · [PDF](https://arxiv.org/pdf/2605.07865)

## 一句话摘要

On-Policy Distillation (OPD) has emerged as a dominant post-training paradigm for Large Language Models, especially in reasoning domains.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-Policy Distillation (OPD) has emerged as a dominant post-training paradigm for Large Language Models, especially in reasoning domains. However, OPD remains unstable in practice due to the high gradient variance of its single-sample Monte Carlo estimator, and recipes for stable training are still immature. We propose vOPD (On-Policy Distillation with a control variate baseline), which casts OPD as policy-gradient RL and stabilizes it by introducing a control variate baseline---canonically a value function---from the RL literature. We show that the OPD value function admits a closed form: the per-token negative reverse KL divergence between student and teacher, available directly from the existing forward pass with no additional critic or inference. Existing stabilization methods either compute the full token-level reverse KL over the entire vocabulary, adding significant overhead, or restrict it to a top-k support, biasing the objective. vOPD instead preserves the lightweight single-sample estimator and subtracts the value function as a detached baseline to keep the gradient unbiased while reducing variance. Moreover, we show that a top-k approximation of the baseline further lowers cost without compromising performance. Across mathematics, science, and instruction-following benchmarks, vOPD consistently outperforms base OPD and matches the most expensive full-vocabulary method, offering an efficient stabilization of OPD through principled RL variance reduction.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Minjae Oh, Sangjun Song, Gyubin Choi, Yunho Choi, Yohan Jo
- 发布：2026-11-05；更新：2026-11-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
