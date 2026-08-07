---
title: "HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving"
description: "Omni models unify text, speech, image, and multimodal reasoning in a single serving backend, but this unified deployment exposes a new scheduling problem."
---

**评分：41/100** · LLM 高效推理 > Serving 与分布式推理 > Batching 与请求调度

[论文原文](https://arxiv.org/abs/2608.01785) · [PDF](https://arxiv.org/pdf/2608.01785)

## 一句话摘要

Omni models unify text, speech, image, and multimodal reasoning in a single serving backend, but this unified deployment exposes a new scheduling problem.

## 为什么值得关注

待编辑增强。

## 摘要原文

Omni models unify text, speech, image, and multimodal reasoning in a single serving backend, but this unified deployment exposes a new scheduling problem. Requests with different output modalities may share an initial multimodal backbone and then diverge into downstream generation stages, creating heterogeneous first-response metrics and service-level objective (SLO) targets on the same GPU. Existing large language model (LLM) and multimodal serving systems mainly optimize token progress or input-side processing, and they do not jointly control temporal sharing in the shared stage and spatial sharing among co-running stages. This paper presents HorizonServe, a single-GPU omni-model serving system that coordinates request admission and GPU allocation under heterogeneous SLOs. HorizonServe profiles per-class first-response latency, protects requests with limited slack, rotates shared-stage opportunities across execution paths, and throttles the shared-stage streaming multiprocessor (SM) allocation when downstream stages are active. Across three omni-model workloads and two GPU platforms, HorizonServe improves SLO attainment by up to 4.9$\times$ in arrival-rate sweeps and 7.0$\times$ under downstream-heavy traffic, and reduces per-class first-response latency by 38.4--63.7\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: request scheduling
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuning Zhang, Dong Yuan
- 发布：2026-08-03；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
