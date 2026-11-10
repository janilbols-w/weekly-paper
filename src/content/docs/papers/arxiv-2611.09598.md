---
title: "Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression"
description: "Private, personalised language models must run on local consumer devices, where large, frontier models cannot fit, and retaining long contexts is non-trivial."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.09598) · [PDF](https://arxiv.org/pdf/2611.09598)

## 一句话摘要

Private, personalised language models must run on local consumer devices, where large, frontier models cannot fit, and retaining long contexts is non-trivial.

## 为什么值得关注

待编辑增强。

## 摘要原文

Private, personalised language models must run on local consumer devices, where large, frontier models cannot fit, and retaining long contexts is non-trivial. Sequential memory---the key-value (KV) cache---grows linearly with context length, quickly dwarfing the model itself: for Qwen3-1.7B-Base, 200,000 retained entries require 21 GiB, 6.6 times more than the model weights. Yet the KV-cache compression methods we measured fail beyond moderate compression ratios. We introduce Transformer-FSQ, addressing extreme KV-cache compression by replacing standard key and value projections with a finite scalar quantisation bottleneck. Our cache stores a packed vector of discrete integer codes per token, with no per-token quantisation metadata. Converting a pretrained transformer trains only these projections on 0.25 tokens per original parameter. We evaluate Transformer-FSQ against five baseline families on models from 0.6B to 8B parameters. On long-context retrieval (RULER), from 12$\times$ to 97.5$\times$ Transformer-FSQ is the most accurate method we evaluate, across scales. A fused Triton kernel decodes directly from the integer codes; with baselines given their authors' kernels where available, it decodes at $1.01\times$ (95% interval $0.98$--$1.05$) the throughput of native SDPA attention on the uncompressed Qwen3-8B-Base at $32\times$ and $1.54\times$ at $97.5\times$. Extreme KV-cache compression is therefore a practical way to extend how much context a fixed device can hold.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Andras Szecsenyi, Thomas L. Lee, Vaisakh Shaj, Elliot J. Crowley, Amos Storkey
- 发布：2026-11-09；更新：2026-11-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
