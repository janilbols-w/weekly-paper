---
title: "CACHEFORGE: LLM-Guided End-to-End Generative Cache Replacement Policy for Performance and Hardware Efficiency"
description: "Modern cache replacement designs saturate because they operate within fixed representational structures, hand-crafted and heuristic based feature-engineered predictors, or offline imitation models that cannot generate new decision logic on their own."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2610.07668) · [PDF](https://arxiv.org/pdf/2610.07668)

## 一句话摘要

Modern cache replacement designs saturate because they operate within fixed representational structures, hand-crafted and heuristic based feature-engineered predictors, or offline imitation models that cannot generate new decision logic on their own.

## 为什么值得关注

待编辑增强。

## 摘要原文

Modern cache replacement designs saturate because they operate within fixed representational structures, hand-crafted and heuristic based feature-engineered predictors, or offline imitation models that cannot generate new decision logic on their own. At the same time, replacement is shaped by the causal interaction of prefetching, thrashing, spatial locality, and access-type behavior, producing an enormous design space that is difficult to traverse manually. Prior approaches typically rely on heuristics, parameter tuning, or imitation of an offline optimal policy, capturing correlations rather than synthesizing new mechanisms. As a result, their performance gains often plateau and they overfit under dynamic workload conditions. CACHEFORGE is the first framework to evolve cache-replacement policies end-to-end by embedding a large language model inside a governed hardware-aware loop. In each iteration, the LLM proposes new C++ replacement logic, the policy is evaluated under a trace-based CRC-2 ChampSim simulator, and the framework enforces feasibility through reward shaping, structural checks, dynamic mutation, temperature scheduling, and cross-policy crossover. This closed-loop generation-evolution loop specifically designed for cache replacement policy enables the discovery of compact policies that satisfy hardware constraints while exploring algorithmic transformations beyond fixed predictor structures. Across SPEC CPU2006, CACHEFORGE outperforms all CRC-2 baselines. It improves the total hit rate by 27.36%, 19.69%, 13.72%, 13.15%, 11.83%, and 5.73% over MPPPB, ReD, Hawk-eye, SHiP++, LIME, and LRU, respectively. On memory-intensive workloads, it increases IPC by 10.15%, 7.89%, 6.34%, 3.64%, 3.12%, and 2.71% over LRU, MPPPB, LIME, ReD, SHiP++, and Hawkeye.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kaushal Mhapsekar, Bita Aslrousta, Brijesh Kumar Bhayana, Paula Contreras, Azam Ghanbari, Ethan Goodman, Anna Andriiko, Samira Mirbagher Ajorpaz
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
