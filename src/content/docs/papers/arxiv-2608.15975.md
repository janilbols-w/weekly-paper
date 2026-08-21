---
title: "A Scalable Pipeline for LLM-Teacher Distillation Labeling: Work-Stealing Job Scheduling and Memory-Aware GPU Concurrency"
description: "Labeling large text corpora with LLM teachers has become a practical route to training data at scale."
---

**评分：61/100** · LLM 高效推理 > 模型与算法效率 > 压缩、稀疏与蒸馏

[论文原文](https://arxiv.org/abs/2608.15975) · [PDF](https://arxiv.org/pdf/2608.15975)

## 一句话摘要

Labeling large text corpora with LLM teachers has become a practical route to training data at scale.

## 为什么值得关注

待编辑增强。

## 摘要原文

Labeling large text corpora with LLM teachers has become a practical route to training data at scale. At millions of items, hand-labeling every batch is not feasible, and two questions dominate: what label quality a teacher buys per dollar, and how to keep a fleet of GPU workers busy under skewed, failure-prone workloads. We present a simple, reproducible pipeline that addresses both. First, a work-stealing ring pool: each worker owns a queue, drains it first, and then steals from ring successors, with exactly-once task claims via atomic conditional writes and crash tolerance via stale-claim sweeping. The claim protocol requires only a compare-and-set primitive from its storage layer; we implement it on a single SQLite file, which makes the reference implementation dependency-free and the experiments reproducible on one machine. Second, a memory-aware concurrency rule that sizes per-node parallelism by how many model copies fit on the GPU, so the same code runs safely across device sizes. Third, a relabeling benchmark methodology in which the teacher relabels a public dataset that already has gold labels, so quality reduces to an agreement measurement and cost follows from measured throughput. Under skewed load the pool sustains up to 3.4 times the throughput of static sharding while matching it at zero skew, loses 0 of 2,000 tasks when half the workers are killed mid-run (static sharding loses 953), and yields measured quality and cost points for an instruction-tuned teacher on irony and sentiment tasks. All experiments run on public data and commodity hardware; code, tests, and run logs are released.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 13 |
| practical impact | 14 |
| reproducibility | 9 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: distillation
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Ravi Satya Durga Prasad Yenugula
- 发布：2026-08-17；更新：2026-08-19
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/rsdpyenugula/hybrid-labeling-training](https://github.com/rsdpyenugula/hybrid-labeling-training)
- 阅读深度：metadata
