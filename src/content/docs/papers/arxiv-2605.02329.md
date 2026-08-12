---
title: "Taming Request Imbalance: SLO-Aware Scheduling for Disaggregated LLM Inference"
description: "In production environments, large language model (LLM) serving is required to meet stringent service-level objectives (SLOs) amid highly variable request patterns."
---

**评分：50/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2605.02329) · [PDF](https://arxiv.org/pdf/2605.02329)

## 一句话摘要

In production environments, large language model (LLM) serving is required to meet stringent service-level objectives (SLOs) amid highly variable request patterns.

## 为什么值得关注

待编辑增强。

## 摘要原文

In production environments, large language model (LLM) serving is required to meet stringent service-level objectives (SLOs) amid highly variable request patterns. In practice, request lengths follow a long-tail distribution, which gives rise to head-of-line blocking on the prefill side and underutilization caused by stragglers on the decode side in disaggregated serving architectures. Current systems, which adopt first-come-first-served (FCFS) scheduling for prefill and continuous batching for decode, lack the ability to adapt to this imbalance, resulting in compromised SLO attainment and reduced throughput. To address these challenges, we propose Kairos, an SLO-aware scheduling system equipped with two complementary mechanisms. On the prefill side, Kairos employs urgency-based priority scheduling: it predicts prefill completion times and dynamically selects requests to maximize the attainment of time-to-first-token (TTFT) SLOs. On the decode side, Kairos introduces slack-guided adaptive batching, which leverages the gap between per-step decode time and the time-per-output-token (TPOT) SLO to greedily pack short requests. This approach maximizes throughput while strictly adhering to SLO requirements. We implement Kairos and conduct evaluations using an online serving dataset and a state-of-the-art LLM. Experimental results demonstrate that, compared with state-of-the-art baselines, Kairos improves TTFT SLO attainment by up to 23.9\%, TPOT SLO attainment by up to 27.1\%, end-to-end SLO attainment by up to 33.8\%, and decode throughput by up to 19.3\%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 13 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Qipeng Wang
- 发布：2026-08-12；更新：2026-08-12
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
