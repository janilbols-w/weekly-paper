---
title: "TokenStack: A Heterogeneous HBM-PIM Architecture and Runtime for Efficient LLM Inference"
description: "Large language model (LLM) serving is now limited by the key-value (KV) cache."
---

**评分：44/100** · AI 基础设施 > 服务平台 > 多租户、SLO 与可靠性

[论文原文](https://arxiv.org/abs/2605.05639) · [PDF](https://arxiv.org/pdf/2605.05639)

## 一句话摘要

Large language model (LLM) serving is now limited by the key-value (KV) cache.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving is now limited by the key-value (KV) cache. During decode, each new token rereads prior KV state, so attention becomes a bandwidth- and capacity-heavy memory task. HBM-PIM helps by moving attention closer to memory, but current stack organizations still waste resources. In practice, only hot KV blocks benefit from near-memory compute. Weights, activations, and cold KV mainly need dense storage and GPU-visible bandwidth. A uniform HBM-PIM stack makes all layers pay for PIM logic, while a dedicated-PIM design such as AttAcc recovers capacity but shrinks the HBM bandwidth left for GPU-side work. We propose TokenStack, a vertically heterogeneous HBM-PIM architecture for KV-centric LLM serving that leverages HBM4's logic-die substrate. TokenStack separates each stack into dense capacity layers and PIM-enabled compute layers, then uses the logic base die as a stack-local control point that manages cross-layer movement without host-side overhead. The base-die controller handles cross-layer DMA, layered address translation, attention-side gather/broadcast coordination, and inline quantization during migration. On top of this hardware, TokenStack uses topology-aware KV placement, workload-aware eviction, and bounded replication to keep hot KV near PIM compute while moving colder state to dense layers. Using production-derived traces across four models, completed multi-QPS runs show that TokenStack increases geometric-mean token throughput by 1.62x and SLO-compliant serving capacity by 1.70x over AttAcc, and reduces per-token energy by 30-47%.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: slo
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zhuoran Li, Zhuohang Bian, Zihao Huang, Yibo Zhao, Xueqi Li, Guangyu Sun, Youwei Zhuo
- 发布：2026-08-13；更新：2026-08-13
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
