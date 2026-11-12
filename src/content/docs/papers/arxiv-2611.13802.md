---
title: "Scaling Shapley Energy Attribution to Large LLM Batches"
description: "LLM services have become essential infrastructure for applications such as chat assistants and coding agents."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2611.13802) · [PDF](https://arxiv.org/pdf/2611.13802)

## 一句话摘要

LLM services have become essential infrastructure for applications such as chat assistants and coding agents.

## 为什么值得关注

待编辑增强。

## 摘要原文

LLM services have become essential infrastructure for applications such as chat assistants and coding agents. Service providers need to attribute resource consumption to individual requests for purposes such as billing. Among these resources, energy is a key metric for assessing the cost of serving each request. However, serving engines batch requests together, and GPUs report only aggregate energy consumption. Providers typically estimate each request's share in proportion to its token consumption, but this approach can produce substantially unfair estimates. The Shapley value provides a principled solution to fair energy allocation, but computing it directly requires $2^N-1$ GPU runs for $N$ requests, which is infeasible for large batches. To address this problem, we propose StepSplit. Across GPU generations, we observe that the energy consumed by each inference step, a forward pass over a batch, consists of a shared energy, largely due to reading model weights, and a request-specific energy. We derive a closed-form Shapley value: each request is charged its own energy plus an equal part of the shared energy of every step in which it participates. A microbenchmark of 2.5-17.8 minutes calibrates both parts of the step energy once per model and GPU configuration. Under static batching, StepSplit uses this closed form in a single pass over the scheduler log. Under continuous batching, removing a request can change how the remaining requests are batched, so StepSplit adds a correction to the closed form, computed by replaying the scheduler on a CPU. We evaluate StepSplit against Shapley values measured using 529,513 GPU runs. Under static batching with batch sizes of 8-256, StepSplit achieves an $L_1$ error of 0.4-4.3%, compared with 13.4-61.3% for token-proportional allocation. Under continuous batching with 8-128 requests, the corresponding errors are 0.5-6.4% and 20.6-71.7%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: continuous batching
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qi Luo, Ziwen Wang, Kunlin Li, Changxi Liu, Yun Chen
- 发布：2026-11-11；更新：2026-11-11
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
