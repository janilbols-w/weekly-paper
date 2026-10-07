---
title: "ECO: Energy-Oriented Configuration Optimization for Attention FFN Disaggregated LLM Serving"
description: "Energy-efficient LLM serving requires minimizing serving GPU energy while meeting latency and throughput service-level objectives (SLOs)."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.08373) · [PDF](https://arxiv.org/pdf/2610.08373)

## 一句话摘要

Energy-efficient LLM serving requires minimizing serving GPU energy while meeting latency and throughput service-level objectives (SLOs).

## 为什么值得关注

待编辑增强。

## 摘要原文

Energy-efficient LLM serving requires minimizing serving GPU energy while meeting latency and throughput service-level objectives (SLOs). Attention--FFN disaggregation (AFD) enables separate resource allocation and operating controls for attention and expert computation, but their energy effects remain coupled through the execution pipeline. Realizing its energy-saving potential therefore requires navigating a hierarchical configuration space in which deployment structures constrain admissible controls and shape their end-to-end effects. Finding low-energy configurations that meet SLOs is challenging because physical evaluations are costly and only a small fraction of candidates can be measured. We present Energy-Oriented Configuration Optimization (ECO), which jointly searches deployment structures and their admissible operating controls under a limited measurement budget. ECO constructs a structure-aware energy prior from calibrated stage behavior and pipeline dependencies, then learns residual prediction errors with a Gaussian process. Its cost-aware constrained Bayesian optimization prioritizes measurements according to expected energy improvement while accounting for SLO feasibility, execution success, and evaluation cost, and returns the lowest-energy measured feasible configuration. Across all 16 scenarios on A6000 and A100 with Qwen and DeepSeek, ECO's frozen configurations, evaluated on disjoint requests, reduce serving energy by 40.5\% and increase output token rate by 20.7\% on average relative to baselines while meeting target SLOs. Across the 8 A6000 scenarios, its selected feasible energy averages 33.1\% below generic constrained Bayesian optimization and 25.8\% below genetic search.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Zou Qingyun, Bin Gao, Zhuobin Huang, Weng-Fai Wong, Tulika Mitra, Bingsheng He
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
