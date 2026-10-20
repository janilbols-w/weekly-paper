---
title: "Koi: Evidence-Guided, Self-Calibrating Planning for Multi-Cloud, Heterogeneous LLM Inference Fleets"
description: "Deploying a large language model (LLM) requires choosing the right accelerator, parallelization strategy, engine configuration, and replica count amongst ~140 other variables across clouds, regions, and markets."
---

**评分：51/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.24355) · [PDF](https://arxiv.org/pdf/2610.24355)

## 一句话摘要

Deploying a large language model (LLM) requires choosing the right accelerator, parallelization strategy, engine configuration, and replica count amongst ~140 other variables across clouds, regions, and markets.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deploying a large language model (LLM) requires choosing the right accelerator, parallelization strategy, engine configuration, and replica count amongst ~140 other variables across clouds, regions, and markets. These decisions are intertwined, and the best cluster-wide plan continually changes as jobs contend for shared capacity on shifting workloads. We present Koi, a self-calibrating cluster planner for heterogeneous, multi-cloud fleets. Koi uses a Recursive Language Model (RLM) hierarchy to propose hypotheses and reason over deployment while deterministic components predict serving behavior, score candidates, and control placement. It represents inference behavior as a fixed causal graph linking decisions (e.g., accelerator, parallelism), runtime mediators (e.g., KV-cache pressure, communication overhead), and outcomes (e.g., latency, throughput). Each deployment strengthens or weakens scoped causal relationships, building a comprehensive playbook for inference that the planner employs to guide future decisions. Job-wise configurations are composed into cluster-wide plans and evaluated against serving objectives, resource constraints, SLO risks, and cost. Across benchmarks, Koi achieves 1.18x greater goodput than the strongest baseline while reducing $/token by 20% in a real heterogeneous cluster. Ablations isolate the contribution of Koi's architecture: a pure language model attains a composite score of 35.3, the same model equipped with Koi's deterministic tools reaches 51.6, and the full Koi planner reaches 70.8.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 15 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Mankeerat Sidhu, Gangmuk Lim, Hetarth Chopra, Maximillian Eisenberg, Quan Hao Ng, Aryan Gosaliya, Shu Liu, Luka Govedi\v{c}, Jiaxin Shan, Hongkuan Zhou, Vikram Sharma Mailthody, P. Brighten Godfrey, Ion Stoica
- 发布：2026-10-20；更新：2026-10-20
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
