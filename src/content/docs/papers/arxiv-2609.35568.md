---
title: "From Experience to Expertise: Adoption-Aware Memory Learning for Data-Scarce NPU Kernel Synthesis"
description: "High-performance kernels underpin efficient accelerator execution but require expert tuning and lengthy manual optimization cycles."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.35568) · [PDF](https://arxiv.org/pdf/2609.35568)

## 一句话摘要

High-performance kernels underpin efficient accelerator execution but require expert tuning and lengthy manual optimization cycles.

## 为什么值得关注

待编辑增强。

## 摘要原文

High-performance kernels underpin efficient accelerator execution but require expert tuning and lengthy manual optimization cycles. LLM coding agents promise automation, yet their CUDA knowledge transfers poorly to data-scarce domain-specific architectures (DSAs) such as NPUs, whose execution models and memory hierarchies differ substantially from those of GPUs. To address this transfer gap, post-training methods adapt LLMs to NPU programming but depend on scarce expert data and substantial training compute. Memory-learning agents instead adapt through external memory, but their uniform credit assignment gives adopted and unused experiences the same reward target, potentially biasing subsequent retrieval rankings. Moreover, when learned values guide only retrieval, high-value experiences that generalize across operators must be retrieved repeatedly rather than retained in context, thereby increasing retrieval overhead and weakening cross-task guidance. We therefore present SAGE, a persistent self-improving agent for NPU kernel synthesis. Adoption-Traced Utility estimation (ATU) combines explicit adoption records with kernel evaluation outcomes for adoption-aware credit assignment. Utility-Gated Consolidation (UGC) uses positive utility and repeated adoption across operators to select and abstract reusable rules into a bounded resident context. On NPUKernelBench, SAGE achieves a 95.5% execution rate versus 84.1% for the strongest controlled baseline, with 86.9% of solved operators outperforming torch_npu. With GLM-5.3, SAGE achieves a 43.99x speedup over the torch_npu reference on sparse flash attention. These results show that adoption-aware credit assignment and selective consolidation enable agents to accumulate and reuse hardware-specific knowledge across tasks.

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

- taxonomy keywords: flash attention
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Longxiao Fan, Tao Zhang, Han Yan, Jiajun Li, Mingcong Song, Guoping Long, Hongjie Si, Weiwei Sun
- 发布：2026-09-28；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
