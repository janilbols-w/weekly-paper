---
title: "Hot-Cold Tiering of HBM and High Bandwidth Flash for Agentic LLM Serving"
description: "Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context."
---

**评分：46/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2609.25782) · [PDF](https://arxiv.org/pdf/2609.25782)

## 一句话摘要

Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large language model (LLM) serving is increasingly agentic, with multi-turn sessions that idle between actions yet must retain their full context. Limited GPU memory capacity forces inactive KV states to be evicted, so resuming a session incurs either costly recomputation or slow interconnect transfers. To address this, high bandwidth flash (HBF)-an on-package 3D-NAND memory offering orders-of-magnitude greater capacity than high bandwidth memory (HBM) at comparable read bandwidth-has emerged as a strong candidate. However, its high read energy and limited write endurance make it impractical to serve all KV traffic. Fortunately, our analysis shows that agentic KV states exhibit distinct access patterns: a small hot set is read for every decoding step, while a large cold pool is read only when a paused session resumes. Exploiting this, we place the hot set in HBM and the cold pool in HBF, forming a hot-cold KV hierarchy within the GPU memory tier. On agentic workloads with Qwen3-Coder-30B-A3B, our design delivers 14 ms time-between-tokens (TBT) and adds only $\approx$0.1 ms of resume latency on top of prefill, while hosting $24\times$ more concurrent sessions per GPU. By confining HBM to the hot set, our design also cuts read power by 7.6 kW per 8-GPU node relative to serving all KV from flash-establishing HBF as a cold-tier complement to HBM rather than its replacement.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Jongjin Baek, Won Ji, Seungjae Yoo, Joo-Young Kim
- 发布：2026-09-23；更新：2026-09-23
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
