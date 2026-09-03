---
title: "WhiFlash: Accelerating Speculative Decoding with Token-Level Cross-Paradigm Routing"
description: "The autoregressive nature of large language models (LLMs) remains a significant bottleneck for inference, particularly in complex agentic workloads."
---

**评分：45/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2606.07710) · [PDF](https://arxiv.org/pdf/2606.07710)

## 一句话摘要

The autoregressive nature of large language models (LLMs) remains a significant bottleneck for inference, particularly in complex agentic workloads.

## 为什么值得关注

待编辑增强。

## 摘要原文

The autoregressive nature of large language models (LLMs) remains a significant bottleneck for inference, particularly in complex agentic workloads. While speculative decoding (SD) accelerates inference, current approaches rely on static drafting paradigms, utilising either autoregressive drafting models for reasoning or diffusion-based parallel drafting models for structured outputs. We empirically find that drafting accuracy fluctuates dramatically within a single sequence, leaving significant performance unrealised by static paradigms and coarse-grained routing. To address this volatility, we introduce WhiFlash, the first cross-paradigm SD method that unifies autoregressive and diffusion-based parallel drafting under a single token-level controller. WhiFlash adopts a fine-grained routing mechanism that employs either a lightweight entropy-based or a learned neural policy, both parametrised to provide a tunable balance between expected token gain and latency. To make high-frequency switching computationally viable, we introduce novel cache-management optimisations, Lazy Catch-up and KV-only Prefill, reducing switching overhead to below 7% of per-round latency. By capitalising on the complementary strengths of fundamentally distinct drafting architectures, WhiFlash achieves significantly higher acceptance lengths, yielding category-specific throughput gains of up to 69.6% over the state-of-the-art autoregressive EAGLE-3 and 37.3% over the diffusion-based DFlash.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 8 |
| rigor | 7 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Young D. Kwon, Miles Williams, Rui Li, Alexandros Kouris, Stylianos I. Venieris
- 发布：2026-09-03；更新：2026-09-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
