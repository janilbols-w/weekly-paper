---
title: "CascadeRec: Deployed Adaptive LLM Compute Allocation for Multi-Tenant Content Recommendation"
description: "Large language models (LLMs) are attractive rerankers for recommendation."
---

**评分：46/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2611.08566) · [PDF](https://arxiv.org/pdf/2611.08566)

## 一句话摘要

Large language models (LLMs) are attractive rerankers for recommendation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language models (LLMs) are attractive rerankers for recommendation. Running an expensive model on every request is costly, and for users with sparse interaction histories it often lowers quality. We present CascadeRec, a two-tier LLM reranking cascade deployed in production at a large financial planning and analysis (FP&A) SaaS provider. It serves content recommendations to enterprise tenants on AWS EKS and GKE. A lightweight Tier-1 model reranks every request. A router escalates only the requests where extra inference-time compute is likely to help, and sends them to a more expensive Tier-2 procedure (self-consistency sampling, multi-path reasoning, or a larger model). The system has run in a production A/B experiment for over a month. Compared with uniform use of the expensive tier, CascadeRec has reduced inference cost by about 10%, with minimal latency impact and no quality regression observed to date. Tenant data cannot be released, so we also evaluate the pipeline on public benchmarks (MovieLens-1M and Amazon-Electronics). Segment-level analysis with paired-bootstrap confidence intervals shows that uniform LLM reranking lowers NDCG@10 for sparse-history users by up to 30%, and its only statistically significant gain appears on the segment with the longest histories. Escalating cold users can make the loss larger instead of repairing it. Which segments benefit from escalation depends on the domain, and this motivates the segment-gated rollout we use in production. We describe the deployment architecture, the measured benefits, and lessons learned, including inter-tenant load imbalance as a driver for cascading and the handling of LLM output-parsing failures at the serving layer.

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

- taxonomy keywords: multi-tenant
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Kai Zhao, Guilin Zhang, Xiang Cheng, Xiquan Cui, Henry Heng, Xu Chu, Alet Blanken
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
