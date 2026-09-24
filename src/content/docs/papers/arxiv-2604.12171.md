---
title: "PipeLive: Efficient Live In-place Pipeline Parallelism Reconfiguration for Dynamic LLM Serving"
description: "Pipeline parallelism (PP) is widely used to partition layers of large language models (LLMs) across GPUs, enabling scalable inference for large models."
---

**评分：42/100** · AI 基础设施 > 服务平台 > Serving Engine 与 Runtime

[论文原文](https://arxiv.org/abs/2604.12171) · [PDF](https://arxiv.org/pdf/2604.12171)

## 一句话摘要

Pipeline parallelism (PP) is widely used to partition layers of large language models (LLMs) across GPUs, enabling scalable inference for large models.

## 为什么值得关注

待编辑增强。

## 摘要原文

Pipeline parallelism (PP) is widely used to partition layers of large language models (LLMs) across GPUs, enabling scalable inference for large models. However, existing systems rely on static PP configurations that fail to adapt to dynamic settings, such as serverless platforms and heterogeneous GPU environments. Reconfiguring PP by stopping and redeploying service incurs prohibitive downtime, so reconfiguration must instead proceed live and in place, without interrupting inference. However, live in-place PP reconfiguration is fundamentally challenging. GPUs are already saturated with model weights and KV cache, leaving little room for new layer placements and necessitating KV cache resizing, at odds with systems like vLLM that preallocate for throughput. Moreover, maintaining KV consistency during execution is difficult: stop-and-copy introduces large pauses, while background synchronization risks inconsistency as states evolve. We present PipeLive, which enables live in-place PP reconfiguration with minimal disruption. PipeLive introduces a redesigned KV cache layout together with a co-designed extension to PageAttention, forming a unified mechanism for live KV resizing. It further adopts an incremental KV patching mechanism, inspired by live virtual machine migration, to synchronize KV states between source and target configurations and identify a safe switch point. PipeLive achieves a 2.5X reduction in time-to-first-token (TTFT) without KV cache overflow compared to disabling KV resizing. Furthermore, compared to a variant without KV patching, it reduces reconfiguration overhead from seconds to under 10ms, and improves TTFT and time-per-output-token (TPOT) by up to 54.7% and 14.7%, respectively.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: llm serving
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Xu Bai, Muhammed Tawfiqul Islam, Chen Wang, Adel N. Toosi
- 发布：2026-09-24；更新：2026-09-24
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
