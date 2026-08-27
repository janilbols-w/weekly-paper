---
title: "Scorpio: Serving Right Requests at the Right Time for Heterogeneous SLOs in LLM Inference"
description: "Large Language Model (LLM) serving increasingly underpins online Web services such as conversational agents, Web search, and programming assistants, where requests carry heterogeneous Service Level Objectives (SLOs) such as Time to First Token (TTFT) and Time Per Output Token (TPOT)."
---

**评分：45/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2505.23022) · [PDF](https://arxiv.org/pdf/2505.23022)

## 一句话摘要

Large Language Model (LLM) serving increasingly underpins online Web services such as conversational agents, Web search, and programming assistants, where requests carry heterogeneous Service Level Objectives (SLOs) such as Time to First Token (TTFT) and Time Per Output Token (TPOT).

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Model (LLM) serving increasingly underpins online Web services such as conversational agents, Web search, and programming assistants, where requests carry heterogeneous Service Level Objectives (SLOs) such as Time to First Token (TTFT) and Time Per Output Token (TPOT). Existing LLM serving systems prioritize maximum throughput and treat all requests uniformly, which leads to suboptimal SLO attainment. This paper introduces Scorpio, an SLO-oriented LLM serving system designed to maximize system goodput and SLO attainment for workloads with heterogeneous SLOs. Our core insight is to exploit SLO heterogeneity for adaptive scheduling across admission control, queue management, and batch selection. Scorpio features a TTFT Guard, which employs least-deadline-first reordering and rejects unattainable requests, and a TPOT Guard, which utilizes a VBS-based admission control and a novel credit-based batching mechanism. Both guards are supported by a predictive module. Evaluations demonstrate that Scorpio improves system goodput by up to 14.4x and SLO adherence by up to 46.5% under high load compared to state-of-the-art baselines.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 11 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yinghao Tang, Tingfeng Lan, Bo Pan, Xiuqi Huang, Hui Lu, Wei Chen
- 发布：2026-08-27；更新：2026-08-27
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
