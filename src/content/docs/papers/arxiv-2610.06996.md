---
title: "Mask-Guided KV Cache Eviction in Block Diffusion Language Models"
description: "Block diffusion language models keep a large key-value (KV) cache throughout generation and attend to it at every denoising step, limiting both memory capacity and generation speed."
---

**评分：45/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2610.06996) · [PDF](https://arxiv.org/pdf/2610.06996)

## 一句话摘要

Block diffusion language models keep a large key-value (KV) cache throughout generation and attend to it at every denoising step, limiting both memory capacity and generation speed.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block diffusion language models keep a large key-value (KV) cache throughout generation and attend to it at every denoising step, limiting both memory capacity and generation speed. Reducing these costs requires deciding which past tokens to use for denoising the current block (selection) and which to keep in memory for future blocks (eviction). We propose MaskAhead, a training-free method that solves both tasks with a single mask-query-based ranking mechanism. Current-block masks guide selection, while probes of upcoming masked blocks guide eviction. Both rank KV entries by their estimated contribution to the attention output. Our quantized variant, Q-MaskAhead, computes selection and attention directly from low-bit KV, largely preserving the selected entries. Experiments on Fast-dLLM-v2, DreamReasoner, and LLaDA2.0-mini cover long-generation reasoning, long-prompt question answering, and needle-in-a-haystack retrieval. On long-prompt QA, MaskAhead reduces KV memory by $9.5\times$ on average with a 1.2-point mean F1 loss relative to dense inference. Q-MaskAhead increases the reduction to $20.1\times$ with a 2.3-point mean F1 loss. In a batch-32 systems profile, MaskAhead achieves $1.23\times$ end-to-end and $1.68\times$ decode-stage speedups over dense inference.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Gleb Molodtsov, Ekaterina Alimaskina, Evgeny Uskov, Artur Zagitov, Aleksandr Beznosikov
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
