---
title: "Block Parallelism For Efficient Distributed Long-Context Diffusion Language Model Training"
description: "Block diffusion language models (BDLMs) combine autoregressive dependencies across blocks with parallel denoising within blocks, but long-context training is constrained by distributed attention communication and activation memory."
---

**评分：49/100** · AI 基础设施 > 训练与数据中心基础设施 > 分布式训练与 Checkpoint

[论文原文](https://arxiv.org/abs/2609.19242) · [PDF](https://arxiv.org/pdf/2609.19242)

## 一句话摘要

Block diffusion language models (BDLMs) combine autoregressive dependencies across blocks with parallel denoising within blocks, but long-context training is constrained by distributed attention communication and activation memory.

## 为什么值得关注

待编辑增强。

## 摘要原文

Block diffusion language models (BDLMs) combine autoregressive dependencies across blocks with parallel denoising within blocks, but long-context training is constrained by distributed attention communication and activation memory. Conventional context parallelism (CP) shards the combined clean-plus-corrupted sequence by position, communicating shared clean K/V together with block-specific corrupted K/V and their gradients. We observe that the BDLM objective separates over target blocks. We introduce block parallelism (BP), a new distributed parallelism dimension that assigns each corrupted-block computation to one rank. To scale BP to long contexts, we introduce context-sharded block parallelism (CSBP), which also shards the shared clean sequence across those ranks. CSBP keeps corrupted K/V and gradients local, avoids replicated clean prefixes, and preserves BDLM training semantics. On 16 H200 GPUs at 256K context, CSBP improves throughput over the best baseline by 1.18-1.45x for supervised fine-tuning and 1.27-1.33x for conversion of autoregressive models to BDLMs, while matching or reducing peak HBM. Full-model speedup reaches 1.61x at 512K. On eight H100 GPUs, CSBP accelerates DFlash2 speculative-decoder training by 2.48x at 512K and 7.59x at 1M. In matched 12-hour DiffusionGemma 26B-A4B SFT runs, CSBP achieves higher pass rates at every trained checkpoint on SWE-bench Verified and Terminal-Bench Lite. Code: https://github.com/ScalingIntelligence/Turbo-dLLM

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 7 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: checkpoint
- quantitative claim detected
- code/artifact link detected

## 元数据

- 作者：Tarun Suresh, Pranshu Chaturvedi, Hangoo Kang, Parth Shroff, Ishan S. Khare, Hermann Kumbong, Azalia Mirhoseini
- 发布：2026-09-16；更新：2026-09-18
- 来源：arXiv RSS；Venue：未确认
- 代码：[https://github.com/ScalingIntelligence/Turbo-dLLM](https://github.com/ScalingIntelligence/Turbo-dLLM)
- 阅读深度：metadata
