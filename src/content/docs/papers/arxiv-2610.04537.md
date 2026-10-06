---
title: "PhaseGate: Phase-Aware CPU Retrieval Scheduling for On-Device LLMs on Unified Memory"
description: "On-device assistants run GPU-based LLM inference alongside CPU retrieval on unified-memory systems."
---

**评分：49/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.04537) · [PDF](https://arxiv.org/pdf/2610.04537)

## 一句话摘要

On-device assistants run GPU-based LLM inference alongside CPU retrieval on unified-memory systems.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-device assistants run GPU-based LLM inference alongside CPU retrieval on unified-memory systems. Under a saturated local-retrieval workload, four concurrent retrieval workers raise 95th-percentile (p95) decode latency by 60-61% on two M4 systems, whereas prefill latency rises by only 5.7-6.9%. We study LLM phase as an admission signal for independent CPU retrieval under controlled LLM workloads. PHASEGATE calibrates separate concurrency limits for prefill and decode, selecting four and one on our base-M4 configuration. Under a backlogged queue, it achieves 2.0 times the aggregate retrieval throughput of the best tested feasible fixed policy, with both p95 LLM latency metrics within 1.25 times their no-retrieval baselines in all seven held-out runs. A phase-blind control, TimeGate, uses the same two limits on a calibration-derived schedule without observing LLM phase. It achieves similar retrieval throughput but violates the output-token latency limit in every run. M2 and M2 Pro Mac minis reproduce the policy ordering, while output-length sweeps show that the advantage narrows as decode occupies more of each request.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: unified memory
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Seoyoon Yum, Sehoon Kim
- 发布：2026-10-06；更新：2026-10-06
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
