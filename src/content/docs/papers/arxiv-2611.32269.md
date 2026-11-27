---
title: "Pando: Noise-Coupled Parallel Draft Trees for Efficient Edge Speculative Decoding"
description: "Autoregressive (AR) decoding emits one token per forward pass, reloading the full model each time, so LLM inference on edge devices is memory-bound while the compute units sit idle."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.32269) · [PDF](https://arxiv.org/pdf/2611.32269)

## 一句话摘要

Autoregressive (AR) decoding emits one token per forward pass, reloading the full model each time, so LLM inference on edge devices is memory-bound while the compute units sit idle.

## 为什么值得关注

待编辑增强。

## 摘要原文

Autoregressive (AR) decoding emits one token per forward pass, reloading the full model each time, so LLM inference on edge devices is memory-bound while the compute units sit idle. Speculative decoding puts that idle compute to work by verifying several drafted tokens in a single pass. State-of-the-art parallel drafters such as DFlash and DSpark propose an entire block of draft tokens in one forward pass, which makes drafting compute-efficient. However, they are deployed with draft chains whose length is capped by the block size they are trained for, leaving most of the computational budget for verification unused. To tackle this problem, we propose Pando, which builds dynamic draft trees on top of a parallel drafter and thereby removes this cap. Pando employs noise-coupled pruning, which draws the target model's sampling noise before drafting and ranks candidate branches under that noise, so the tree retains the branches the target will actually sample. Noise coupling is lossless and requires no retraining or additional model pass, yet increases acceptance length by up to $8.4\%$ on Qwen3-8B. To optimize and evaluate Pando configurations across hardware, we normalize an operator-level roofline to AR decoding, reducing every platform to its ridge point. On a representative edge device, a 16-node Pando tree attains $5.3\times$ speedup and $4.2\times$ energy reduction over AR decoding: $25\%$ faster than DSpark's released chain, and $27\%$ faster and $72\%$ more energy-efficient than an EAGLE-3 tree. The best configurations remain memory-bound on every edge device we model, so added compute capacity does not reduce their latency.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 13 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Joren Dumoulin, Hyoukjun Kwon, Subhankar Pal, Steven Li, Vignesh Vivekraja, Marian Verhelst
- 发布：2026-11-24；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
