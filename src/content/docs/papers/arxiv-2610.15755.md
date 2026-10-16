---
title: "Native Dual Pools or Shared Paging? Memory Organization for Concurrent Hybrid LLM Serving"
description: "Hybrid attention-SSM serving combines growing attention KV with fixed-size recurrent and convolution state whose allocation units, reuse boundaries, and lifetimes differ."
---

**评分：50/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2610.15755) · [PDF](https://arxiv.org/pdf/2610.15755)

## 一句话摘要

Hybrid attention-SSM serving combines growing attention KV with fixed-size recurrent and convolution state whose allocation units, reuse boundaries, and lifetimes differ.

## 为什么值得关注

待编辑增强。

## 摘要原文

Hybrid attention-SSM serving combines growing attention KV with fixed-size recurrent and convolution state whose allocation units, reuse boundaries, and lifetimes differ. We implement four memory organizations in a modified vLLM runtime: a coarse shared-page baseline (S0), checkpoint-internal recurrent paging (S1), paging with convolution-slot packing (S2), and native dual pools (D0). Nine evaluation questions cover storage costs and serving behavior. The cumulative S0-S1-S2 refinement improves completed-output throughput and tail completion time at the main operating point. D0-S2 performance varies with memory budget, offered load, and admission headroom. Shared-prefix workloads yield larger stepwise gains; gains also persist in a no-sharing control with equal recorded input-work totals. State traces identify recurrent-checkpoint availability as the limit on joint reuse in the tested S2 runs. Extending producer-side checkpoint lifetime increases reusable depth at a fixed page budget. A fresh-seed SHARE/ISOLATE comparison estimates a positive retention interaction, with a primary confidence interval that includes zero. Retained-state continuation correctness remains unresolved. These findings motivate evaluating physical state representation together with request admission and checkpoint lifetime when designing memory management for concurrent hybrid-model serving.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving, model serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Dongwook Kang
- 发布：2026-10-11；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
