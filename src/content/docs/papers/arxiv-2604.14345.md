---
title: "PAC-CF: Calibrating Irreversible Frontier Pruning in LLM-Guided Search"
description: "LLM-guided search explores multiple candidate trajectories, but at substantial test-time cost."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2604.14345) · [PDF](https://arxiv.org/pdf/2604.14345)

## 一句话摘要

LLM-guided search explores multiple candidate trajectories, but at substantial test-time cost.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM-guided search explores multiple candidate trajectories, but at substantial test-time cost. Pruning low-scoring frontier candidates can control this cost, yet it also turns potentially biased evaluator scores into irreversible decisions: systematic ranking errors can persist under repeated scoring and remove useful branches. We propose Probably Approximately Correct Conformal Filtering (PAC-CF). Its fixed-frontier analysis formulates elimination as an $(\varepsilon,\delta)$-PAC problem under bounded evaluator bias; its operational rule separately calibrates a score-gap threshold on held-out tasks by running the original controller without PAC-CF and using post-search verifier labels to measure the deficit of solution-preserving candidates relative to the frontier leader. Conditional on exchangeable native-controller tasks with nonempty protected exposure, conformal calibration gives finite-sample coverage for retaining at least one verifier-defined valid continuation at every protected frontier on the native trajectory. At deployment, PAC-CF removes only candidates whose gap from the highest frontier score exceeds the frozen threshold. We evaluate PAC-CF across three domains, five controllers, and four request budgets from B100 to B500. In the cross-domain/controller macro averages, the point estimates for all three workload measures are lower at every budget; the paired-bootstrap 95\% confidence interval for utility excludes zero at B100 and B200. For pruning-aware ToolTree, the full-test-set cross-domain utility difference is $+4.38$ points at each tested budget; on the natural-termination sensitivity cohort, physical requests decrease by $18.94$--$18.95\%$ and end-to-end token usage by $23.57$--$23.76\%$.

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

- taxonomy keywords: pruning
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tianhao Qian, Jiayu Chen, Lixu Wang
- 发布：2026-09-09；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
