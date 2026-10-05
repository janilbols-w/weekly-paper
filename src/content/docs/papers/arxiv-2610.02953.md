---
title: "SlimKV: Joint Token-Feature KV Cache Compression with Reconstruction-Free Beacon Attention"
description: "Long-context LLM serving is increasingly bottlenecked by KV-cache memory, especially in resource-constrained scenarios."
---

**评分：52/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.02953) · [PDF](https://arxiv.org/pdf/2610.02953)

## 一句话摘要

Long-context LLM serving is increasingly bottlenecked by KV-cache memory, especially in resource-constrained scenarios.

## 为什么值得关注

待编辑增强。

## 摘要原文

Long-context LLM serving is increasingly bottlenecked by KV-cache memory, especially in resource-constrained scenarios. Among existing KV-cache compression strategies, token-wise methods reduce cached states but risk information loss through eviction or condensation, while feature-wise methods reduce per-token KV dimensions but can require full-dimensional reconstruction to apply positional embedding, limiting decoding speedups. We introduce SlimKV, a question-agnostic joint token-feature KV-cache compression method. SlimKV uses low-rank-aware training to compress long contexts into beacon memory states with latent KV representations, together with layer-adaptive rank allocation. We further uncover a positional asymmetry: removing key-side RoPE affects beacon and raw tokens differently, with much smaller degradation for beacon tokens. Exploiting this asymmetry, SlimKV trains beacon KV projections under a K-RoPE-free constraint and enables latent-space attention during decoding, mitigating reconstruction latency. On LongBench, SlimKV outperforms baselines at 16x/32x compression and remains leading at 4x/8x, where it retains over 96% of the uncompressed model's score. Needle-in-a-Haystack confirms robustness across evidence positions, and efficiency evaluation shows up to 7.34x attention speedup and 3.38x end-to-end decoding speedup over the uncompressed model at 128K length.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache, kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Zihan Teng, Jiayu Zhao, Wentao Ren, Minhao Fan, Tianrui Ma, Song Chen, Weichen Liu
- 发布：2026-10-05；更新：2026-10-05
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
