---
title: "Zephon: Elastic Determinism for Online, Stateful Foundation Model Data Loading Pipelines"
description: "Deterministic data loading is important for foundation model development: model researchers need confidence that differences they observe across costly ablations are caused by the parameter they changed rather than non-determinism in the training data sequence."
---

**评分：46/100** · AI 基础设施 > 集群与资源系统 > 存储与数据平面

[论文原文](https://arxiv.org/abs/2610.03087) · [PDF](https://arxiv.org/pdf/2610.03087)

## 一句话摘要

Deterministic data loading is important for foundation model development: model researchers need confidence that differences they observe across costly ablations are caused by the parameter they changed rather than non-determinism in the training data sequence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Deterministic data loading is important for foundation model development: model researchers need confidence that differences they observe across costly ablations are caused by the parameter they changed rather than non-determinism in the training data sequence. The data loader must provide elastic determinism, i.e., a deterministic sequence of global training data batches despite changes to the GPU topology across runs (e.g., due to GPU scarcity), frequent checkpoint-resume cycles, and different data processing execution backends. Achieving this is difficult because modern foundation model data pipelines tokenize, pack, and mix samples online, introducing stateful n-to-m transformations that break sample indexing. Existing data loaders largely assume indexable 1-to-1 pipelines, and the common workaround of offline materialization is expensive and, for some modalities such as video, infeasible. We present Zephon, a data loader for foundation models that supports online, stateful pipelines while providing elastic determinism and efficient resumption from checkpoints. It partitions the global stream into topology-independent lanes, serializes ordering decisions while parallelizing stateless work on interchangeable backends, and checkpoints only bounded in-flight state so recovery cost does not grow with training progress. We evaluate Zephon on text and vision-language workloads and show that it achieves competitive throughput while providing a combination of guarantees that no existing loader offers for online, stateful pipelines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: data loading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Maximilian B\"other, Josh Wills, Ties Robroek, Sonnet Xu, Paul Burstein, Daniel Zayas, Cody Blakeney, Siddharth Joshi, Haoli Yin, Rishabh Adiga, Haakon Mongstad, Luke Merrick, Pratyush Maini, Ari Morcos, Matthew Leavitt, Ana Klimovic, Bogdan Gaza
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
