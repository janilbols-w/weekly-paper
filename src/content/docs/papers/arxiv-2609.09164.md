---
title: "HELIOS: Guardrailed LLM-Driven Evolution of Autonomous Resource Orchestration Policies for Multi-Cloud Distributed Systems"
description: "Operating latency-sensitive services across multiple public clouds creates an optimization surface no single provider autoscaler can see: on-demand vCPU prices differ by provider, spot discounts and interruption risks vary by provider and instance type, egress fees penalize state movement, and provider-level failures can take down single-cloud deployments."
---

**评分：43/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2609.09164) · [PDF](https://arxiv.org/pdf/2609.09164)

## 一句话摘要

Operating latency-sensitive services across multiple public clouds creates an optimization surface no single provider autoscaler can see: on-demand vCPU prices differ by provider, spot discounts and interruption risks vary by provider and instance type, egress fees penalize state movement, and provider-level failures can take down single-cloud deployments.

## 为什么值得关注

待编辑增强。

## 摘要原文

Operating latency-sensitive services across multiple public clouds creates an optimization surface no single provider autoscaler can see: on-demand vCPU prices differ by provider, spot discounts and interruption risks vary by provider and instance type, egress fees penalize state movement, and provider-level failures can take down single-cloud deployments. Large language models (LLMs) are appealing orchestrators because they can synthesize non-trivial decision logic from a natural-language environment description. However, placing an LLM on the critical path of every scheduling decision is impractical: for a 200-service fleet, per-decision inference would cost more than the cloud capacity it manages and add multi-second latency to a millisecond-scale control loop. HELIOS moves the LLM off the critical path. The LLM evolves executable orchestration policies, small Python programs over a fixed feature interface, against a trace-driven multi-cloud simulator. Only the champion program runs in production, wrapped in guardrails that enforce capacity feasibility, SLO-class placement rules, and churn budgets regardless of evolved code's proposal. On real workload traces (PlanetLab, Bitbrains, Azure) combined with 2026 price and interruption-frequency data from AWS, Azure, and GCP, the evolved policy reduces penalized operating cost by 45% versus a single-cloud best-fit baseline and by 9-19% versus calibrated multi-cloud heuristics. It matches an oracle-informed MILP planner's premium-SLO performance at 40% lower cost and outperforms a DQN meta-controller trained with 2.6x more environment interactions. Guardrails are essential: without them, the same policy family degrades to 97-98% premium-tier downtime under a 10x spot-hazard stress test, versus 0.17% when guarded. We release the simulator, policies, LLM prompt/response archive, and per-generation fitness logs for full reproducibility.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Guanyu Ding, Ying Wang
- 发布：2026-09-10；更新：2026-09-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
