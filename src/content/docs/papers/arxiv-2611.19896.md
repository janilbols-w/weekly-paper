---
title: "LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models"
description: "Looped language models such as Ouro and Raven apply one weight-shared block several times per token, so autoregressive decoding (AR) runs every loop of every token in sequence."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2611.19896) · [PDF](https://arxiv.org/pdf/2611.19896)

## 一句话摘要

Looped language models such as Ouro and Raven apply one weight-shared block several times per token, so autoregressive decoding (AR) runs every loop of every token in sequence.

## 为什么值得关注

待编辑增强。

## 摘要原文

Looped language models such as Ouro and Raven apply one weight-shared block several times per token, so autoregressive decoding (AR) runs every loop of every token in sequence. Pipelined self-speculative decoders overlap these loops by drafting tokens from shallow readouts and verifying them at full depth. Yet every loop of a looped LM ends in a readout of the next token, and draft tokens pass through every depth anyway, so each depth can check them without an extra pass. We introduce LoopSkim, in which the depth of the pipeline is the verifier. Draft tokens copied from the context, as in prompt lookup decoding, enter after the first loops, any later readout that contradicts one replaces it at that depth, and only full-depth readouts commit tokens. LoopSkim fixes the random draws of every position in advance, so each check compares two tokens and decoding stays lossless in exact arithmetic under sampling for any number of checks and draft chains. Without training, its speedup over AR averages 1.73x that of LoopSpec across greedy decoding and sampling, and its checks between the first loops and full depth speed it up on every model. An optional draft head adds a second chain and raises this average to 1.99x.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: speculative decoding
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Muhan Xiao, Shijian Li
- 发布：2026-11-15；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
