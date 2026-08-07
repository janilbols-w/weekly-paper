---
title: "AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation"
description: "Attention--Feed-Forward Network (FFN) Disaggregation (AFD) is emerging as a promising architecture for serving Mixture-of-Experts (MoE) language models."
---

**评分：38/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2608.04502) · [PDF](https://arxiv.org/pdf/2608.04502)

## 一句话摘要

Attention--Feed-Forward Network (FFN) Disaggregation (AFD) is emerging as a promising architecture for serving Mixture-of-Experts (MoE) language models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Attention--Feed-Forward Network (FFN) Disaggregation (AFD) is emerging as a promising architecture for serving Mixture-of-Experts (MoE) language models. While existing AFD systems improve the efficiency of disaggregated execution, they leave a deployment question unanswered: under the same model, workload, time-per-output-token (TPOT) service-level objective (SLO), hardware budget, hardware catalog, and runtime capabilities, does AFD provide higher throughput than the best collocated deployment? Answering this question requires jointly optimizing hardware assignment and deployment organization for both architectures, making exhaustive provisioning prohibitively expensive. We present AFD-Ledger, an offline analytical provisioning system that independently provisions AFD and collocated deployments using an analytical execution model and an evaluation-bounded hardware search. Across deployment spaces where exhaustive provisioning is feasible, AFD-Ledger reduces complete deployment evaluations by 68.8%--83.5% while still recovering the globally optimal deployment. On three physical LongCat 2.0 deployments, it preserves the correct architecture decision while predicting AFD-to-collocated throughput within 6.6%--9.6% of measurement. Using this validated framework, we show that homogeneous AFD improves fixed-budget throughput in only a minority of the studied settings, heterogeneous AFD requires deployment-level hardware complementarity rather than heuristic device selection, and role-specific hardware improvements matter primarily when they enable better deployment organizations by crossing deployment capability--price boundaries.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chengyu Qiu, Xiao Fu, Fengcun Li, Yulei Qian, Yuchen Xie, Xunliang Cai, Yingdi Shan, Yongwei Wu, Mingxing Zhang
- 发布：2026-08-05；更新：2026-08-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
