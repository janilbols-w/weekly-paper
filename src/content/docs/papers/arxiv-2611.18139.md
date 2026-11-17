---
title: "PUMA-Former: Uncertainty-Aware Agentic Computation Offloading in MEO-LEO Satellite Networks With Incomplete Information"
description: "Satellite edge computing distributes mobile workloads across moving processors whose service capacity must be coordinated over time."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2611.18139) · [PDF](https://arxiv.org/pdf/2611.18139)

## 一句话摘要

Satellite edge computing distributes mobile workloads across moving processors whose service capacity must be coordinated over time.

## 为什么值得关注

待编辑增强。

## 摘要原文

Satellite edge computing distributes mobile workloads across moving processors whose service capacity must be coordinated over time. In medium Earth orbit (MEO)--low Earth orbit (LEO) networks, periodic reports leave CPU states stale or missing, making offloading sensitive to uncertain capacity and shared-destination congestion. We propose PUMA-Former, an uncertainty-aware agentic framework for cooperative offloading under incomplete information that balances completed work, service delay, and execution cost. A MEO coordinator maintains distinct-report memory and closes the loop between available evidence, capacity estimates, allocation commands, and execution feedback. Latent-delay attention weights plausible measurement-age hypotheses, and historical innovations refine CPU estimates around the latest received report. Queue-error-aware fusion incorporates auxiliary pressure while accounting for backlog uncertainty. The inferred resource moments condition a structured Transformer allocator for joint destination, partition, bandwidth, CPU, and power decisions. Bounded risk-aware calibration then adjusts workload splits to reflect uncertainty and shared destination load. In traffic-driven development evaluation, PUMA-Former increases admitted compute-work completion by 8.62%, reduces mean modeled service delay by 34.78%, and reduces mean episode-P95 delay by 71.08% relative to ATLA-adapt. It also improves completion and normalized energy over fixed-half round-robin offloading. Service gains over the learning baselines involve higher normalized energy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yi Jing, Chunxiao Jiang, Jiawei Wang, Jiachen Sun
- 发布：2026-11-16；更新：2026-11-16
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
