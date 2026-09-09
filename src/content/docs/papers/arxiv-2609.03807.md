---
title: "Almost Free State Prediction Separation"
description: "State--prediction separation (SPS) relieves a language model's hidden state of two competing burdens---summarizing the context and predicting the next token---by splitting the forward pass into a state stream and a prediction stream."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2609.03807) · [PDF](https://arxiv.org/pdf/2609.03807)

## 一句话摘要

State--prediction separation (SPS) relieves a language model's hidden state of two competing burdens---summarizing the context and predicting the next token---by splitting the forward pass into a state stream and a prediction stream.

## 为什么值得关注

待编辑增强。

## 摘要原文

State--prediction separation (SPS) relieves a language model's hidden state of two competing burdens---summarizing the context and predicting the next token---by splitting the forward pass into a state stream and a prediction stream. The separation works, but it is expensive: the prediction stream is a second pass over the whole backbone, costing $\sim$1.9$\times$ the pretraining FLOPs, and even more in terms of wall-clock time when using a flexible attention mask. This paper makes state--prediction separation almost free. We take the separation to its limit with a free pause token: a prediction stream that writes no keys or values at all and so rides the sequence's existing positions. It improves next-token prediction of a standard Transformer by 2-3 centinats in practice on a 1B parameter model, and because it adds no position it costs nothing at inference---no added context length, no KV cache, no decode steps, and essentially no latency, with the growth in inference flops typically irrelevant as it is not the active bottleneck on throughput. The cost is therefore entirely in training where we use four mechanisms to drive it down: a two-pass split that keeps FlashAttention kernels viable, the $w{=}0$ prediction window, a shared gated FFN that evaluates one FFN per position rather than one per stream, and phasing the separation onto the tail of the run. Together these bring the overhead versus an optimized pretraining pipeline to $1.33\times$ wall-clock while recovering ~94% of the gain compared to SPS, and to as low as $1.09\times$ along a graceful quality/compute tradeoff. Furthermore, the FFN optimization reduces the raw flops required at inference time. The result is an isoflop, isoparameter, and isotoken improvement over standard next token trained transformers.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：John Langford, Nathan Godey, Giovanni Monea, Yoav Artzi, Harry Dong, Ying Fan, Gustavo de Rosa, Zheng Zhan
- 发布：2026-09-03；更新：2026-09-09
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
