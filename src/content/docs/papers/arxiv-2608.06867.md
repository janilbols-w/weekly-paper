---
title: "LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers"
description: "No single large language model (LLM) is optimal across all queries and budget constraints, making model routing essential for cost-effective deployment."
---

**评分：40/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2608.06867) · [PDF](https://arxiv.org/pdf/2608.06867)

## 一句话摘要

No single large language model (LLM) is optimal across all queries and budget constraints, making model routing essential for cost-effective deployment.

## 为什么值得关注

待编辑增强。

## 摘要原文

No single large language model (LLM) is optimal across all queries and budget constraints, making model routing essential for cost-effective deployment. Existing routers adopt diverse formulations and implementations, making fair comparison and extension difficult. We present a unified formulation of LLM routing as a sequential decision process characterized by five components: context encoders, model encoders, scoring functions, decision rules, and learning signals, covering single-turn, multi-turn, and personalized routing. Based on this formulation, we develop an automated pipeline for constructing routing supervision and evaluating routers jointly on response quality and inference cost. The resulting benchmark, xRouteBench, spans generic LLM, memory-augmented, vision, time-series, and personalized routing tasks. We further introduce LLMRouter, an open-source modular infrastructure with more than 16 representative routers. Our empirical study shows that learned routers outperform the strongest fixed-model baseline by 14.6% relatively, lightweight routers become more competitive under tight cost constraints, and user-conditioned routing consistently improves personalization.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model routing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tao Feng, Fangxu Yu, Haozhen Zhang, Zhongjie Dai, Liangqi Yuan, Zijie Lei, Weizhi Zhang, Kunlun Zhu, Haodong Yue, Keyang Xuan, Ge Liu, Jiaxuan You
- 发布：2026-08-10；更新：2026-08-10
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
