---
title: "From Alert Floods to Precedence Forests: Zero-Prior-Knowledge Incident Triage with LOGOS"
description: "Commercial observability platforms rely on domain artifacts like distributed traces, topology maps, and baseline metrics."
---

**评分：40/100** · AI 基础设施 > 服务平台 > 可观测性与 Benchmark

[论文原文](https://arxiv.org/abs/2610.02297) · [PDF](https://arxiv.org/pdf/2610.02297)

## 一句话摘要

Commercial observability platforms rely on domain artifacts like distributed traces, topology maps, and baseline metrics.

## 为什么值得关注

待编辑增强。

## 摘要原文

Commercial observability platforms rely on domain artifacts like distributed traces, topology maps, and baseline metrics. However, when troubleshooting proprietary software, enterprise operators are left with only raw, unannotated text logs. We explore the extreme boundary of log-only diagnosis: To what extent can we isolate failure propagation using strictly raw text logs? We present LOGOS, an unsupervised system that exploits entity-event co-occurrence and temporal precedence to collapse millions of raw log lines into a compact precedence forest. Evaluated across 25 production enterprise outages and 12 open-source issues, LOGOS operates with zero prior knowledge---requiring no seed queries, observed symptoms, or pre-defined incident boundaries. In a median wall-time of 4.5 minutes, LOGOS eliminates a median 99.8% of background noise, achieves 0.76 mean recall, and detects failure cascades with a 16-hour median diagnosis-verified lead time---consolidating alert floods 124x to enable 80% enterprise (100% open-source) zero-shot LLM root-cause accuracy.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 8 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: observability
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Radhika Niranjan Mysore
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
