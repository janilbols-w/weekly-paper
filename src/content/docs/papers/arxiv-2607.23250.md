---
title: "Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool"
description: "Long-context LLM training suffers from a load-balancing problem that sequence packing does not solve."
---

**评分：44/100** · AI 基础设施 > 服务平台 > Gateway、路由与弹性

[论文原文](https://arxiv.org/abs/2607.23250) · [PDF](https://arxiv.org/pdf/2607.23250)

## 一句话摘要

Long-context LLM training suffers from a load-balancing problem that sequence packing does not solve.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM training suffers from a load-balancing problem that sequence packing does not solve. Packing samples into fixed-token sequences balances memory and linear-cost operators, but the dominant attention cost scales with the sum of squared sequence lengths. Thus, equally sized packed sequences drawn from a long-tailed corpus can carry substantially different attention workloads, creating data-parallel stragglers and pipeline bubbles. Existing approaches either balance at the granularity of sequences or microbatches, where an outlier can dominate an assignment, or disaggregate attention over a global worker pool whose communication domain grows with the data-parallel (DP) degree. We present Libra, which operationalizes the law of large numbers (LLN) as a scaling principle for load balancing: the attention-balancing pool need not grow with the DP degree. Libra groups packed sequences and their CP groups into fixed-size sequence pools. As DP scales out, Libra adds pools rather than enlarging each one, bounding every attention exchange. Variance-Reduced Sequence Placement makes this effective for finite, long-tailed workloads by co-locating sequences with complementary attention workloads to reduce residual inter-pool skew. Within each pool, Tiled Attention Pooling dispatches sequence-head SH-Tiles across GPUs, while a pipelined runtime overlaps tile exchange with attention. Libra exposes a drop-in context-parallel attention operator and a pluggable data sampler, requiring no changes to model layers, optimizers, or pipeline schedules. On three production Qwen3 models (8B, 30B, 235B) and 256K- and 1M-token production workloads, Libra improves end-to-end training throughput over the strongest evaluated baseline (WLB-LLM) by 44% on average and up to 68% at 256 GPUs. Libra has run for hundreds of thousands of GPU-hours in production on jobs spanning 32K to 1M tokens.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: load balancing
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yan Wang, Xiulong Yuan, Kaiming Yang, Jiaxuan Peng, Pengju Lu, Mingzhen Li, Zhipeng Zhang, Chang Si, Zhixiang Ruan, Hongqing Chen, Linlang Jiang, Siyu Wang, Langshi Chen, Rui Men, Man Yuan, Guangming Tan, Yong Li, Weile Jia, Jingren Zhou
- 发布：2026-09-18；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
