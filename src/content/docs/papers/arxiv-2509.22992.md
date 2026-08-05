---
title: "T-TAMER: Provably Taming Trade-offs in ML Serving"
description: "As machine learning models continue to grow in size and complexity, efficient serving faces increasingly broad trade-offs spanning accuracy, latency, resource usage, and other objectives."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2509.22992) · [PDF](https://arxiv.org/pdf/2509.22992)

## 一句话摘要

As machine learning models continue to grow in size and complexity, efficient serving faces increasingly broad trade-offs spanning accuracy, latency, resource usage, and other objectives.

## 为什么值得关注

待编辑增强。

## 摘要原文

As machine learning models continue to grow in size and complexity, efficient serving faces increasingly broad trade-offs spanning accuracy, latency, resource usage, and other objectives. Multi-model serving further complicates these trade-offs; for example, in cascaded models, each early-exit decision balances latency reduction against potential accuracy loss. Despite the pervasiveness and importance of such trade-offs, current strategies remain largely heuristic and case-specific, limiting both their theoretical guarantees and general applicability. We present a general framework, T-Tamer, which formalizes this setting as a multi-stage decision process, where the objective is to determine both when to exit and which model to consult. Our main result shows that recall (i.e., the ability to revisit earlier models) is both necessary and sufficient for achieving provable performance guarantees. In particular, we prove that strategies without recall cannot obtain any constant-factor approximation to the optimal trade-off, whereas recall-based strategies provably attain the optimal trade-off in polynomial time. We validate our analysis through experiments on synthetic datasets and early-exit workloads for vision and NLP benchmarks. The results show that recall-based strategies consistently yield efficient accuracy-latency trade-offs. We hope this work provides a principled foundation for bridging heuristic practice with theoretical guarantees in the design of early-exit and cascaded models.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 13 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuanyuan Yang, Ruimin Zhang, Jamie Morgenstern, Haifeng Xu
- 发布：2026-08-04；更新：2026-08-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
