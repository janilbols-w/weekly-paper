---
title: "Exstill: The Most Efficient Single-Chip Processor for the Next Token"
description: "Generating a token with a language model requires a fixed amount of arithmetic, whose energy sets a floor beneath any hardware."
---

**评分：48/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.18859) · [PDF](https://arxiv.org/pdf/2611.18859)

## 一句话摘要

Generating a token with a language model requires a fixed amount of arithmetic, whose energy sets a floor beneath any hardware.

## 为什么值得关注

待编辑增强。

## 摘要原文

Generating a token with a language model requires a fixed amount of arithmetic, whose energy sets a floor beneath any hardware. For Qwen3-1.7B at a 16K-token context, gate-level measurements at 5 nm place this floor at 0.89 mJ per token, yet an NVIDIA B300 spends 391-1,120x that. The excess is the price of generality, software layers, programmable hardware and moving weights and key-value (KV) caches from external memory, and it widens with each process generation. We present a co-design approach that brings token generation close to this floor and then lowers the floor itself, optimizing silicon and model together in a gate-level search loop. Fixing one model architecture in the datapath, with weights still loadable, and holding weights and every conversation's KV cache on-die, a pre-silicon 5 nm design brings an unchanged Qwen3-1.7B token to 3.4x its floor. Co-designing the model with the circuits at fixed quality lowers the floor to 0.29 mJ and the token to 0.52 mJ, 1.8x the new floor and less than the baseline model's arithmetic alone, while on-die capacity grows from one user to twelve. Against a measured B300 serving the same twelve users, the design decodes each user's tokens 110x faster at 690x lower energy. To show that one fixed architecture can serve, as a co-processor, the latency-critical workloads around a frontier model, we introduce Polyglot-DC (1.7B and 4B, each with its own design), specialized for each job by distillation and task-specific training into its own weights. As a drafter it speeds single-user speculative decoding of large open models by up to 6.6x at the maximum reasoning effort. Its guard returns multilingual verdicts in a millisecond or less, within a point of the strongest open guard. Its agent and financial-reasoning models lead comparable open models on established benchmarks, with a reasoning turn falling from seconds to tens of milliseconds.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Valavan Manohararajah, Vithursan Thangarasa
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
