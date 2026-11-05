---
title: "Dory1.0-4B: A Looped Normalized-GPT"
description: "We introduce Dory1.0-4B, a 4-billion-parameter looped (latent-recurrent) language model with elastic depth: a single checkpoint serves different inference compute budgets."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.03998) · [PDF](https://arxiv.org/pdf/2611.03998)

## 一句话摘要

We introduce Dory1.0-4B, a 4-billion-parameter looped (latent-recurrent) language model with elastic depth: a single checkpoint serves different inference compute budgets.

## 为什么值得关注

待编辑增强。

## 摘要原文

We introduce Dory1.0-4B, a 4-billion-parameter looped (latent-recurrent) language model with elastic depth: a single checkpoint serves different inference compute budgets. Dory1.0-4B is built on a normalized Transformer (nGPT) backbone with interleaved sliding-window and full-attention layers, organized into an input block, a shared recurrent block, and an output block. At inference, the recurrent block can be applied a variable number of times. We pre-trained Dory1.0-4B on 6 trillion tokens. The first 4.5 trillion tokens were trained in NVFP4, and additional pre-training then extended the context length to 256K tokens. Next, we post-trained the model using Supervised Fine-Tuning (SFT) and Reinforcement Learning with Verifiable Rewards (RLVR), with a difficulty-aware loop curriculum that routes harder prompts to deeper loops. Increasing the loop count improves accuracy, with the largest gains on coding, agentic, and long-context benchmarks. With two or more loops, Dory1.0-4B outperforms larger models such as Qwen3.5-9B, Gemma 4 12B, and Gemma 4 26B-A4B on average across 12 benchmarks. Looping also makes Dory1.0-4B more token-efficient on agentic benchmarks: with four loops, it generates 1.3-2.5x fewer tokens than with one loop, as the extra computation is spent in latent space rather than on longer outputs. To reduce memory during looping, Dory1.0-4B caches keys and values only from the last loop, keeping its KV-cache footprint equal to that of a non-looped model at any loop count while retaining most of the accuracy gains. We open-source the BF16, MXFP8, NVFP4, and GGUF quantized checkpoints.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 7 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv-cache
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Maxim Fishman, Simeng Sun, Shantanu Acharya, Faisal Ladhak, Brian Chmiel, Santiago Akle Serano, Ron Banner, Boris Ginsburg, Krishna C. Puvvada
- 发布：2026-11-04；更新：2026-11-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
