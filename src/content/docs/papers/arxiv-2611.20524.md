---
title: "GaugeRoPE: RoPE-Compatible Executable Latent Attention"
description: "Latent KV cache compression reduces memory footprint by mapping historical keys and values into compact representations."
---

**评分：40/100** · LLM 高效推理 > Runtime 与内存效率 > Attention 与 KV Cache

[论文原文](https://arxiv.org/abs/2611.20524) · [PDF](https://arxiv.org/pdf/2611.20524)

## 一句话摘要

Latent KV cache compression reduces memory footprint by mapping historical keys and values into compact representations.

## 为什么值得关注

待编辑增强。

## 摘要原文

Latent KV cache compression reduces memory footprint by mapping historical keys and values into compact representations. However, generic compressed key states require reconstruction to native dimension before applying RoPE and computing attention scores, adding sequence-scaling overhead to the decode path. We characterize when a latent KV representation can serve directly as the execution state of pretrained RoPE. For RoPE-based transformers, exact static linear execution of the rotary key path requires the latent-to-native map to preserve the pretrained RoPE action through an intertwining relation, restricting exact mixing to coordinates that share the same RoPE frequency. Guided by this characterization, we build GaugeRoPE, a training-free executable latent KV representation. It combines a RoPE-compatible carrier that preserves the rotary action with an approximate position-independent residual key--value (RKV) correction for complementary key and value information, both evaluated without per-token dense historical K/V reconstruction. On Mistral-7B, GaugeRoPE achieves $5.85\times$ KV compression while maintaining quality close to the full-cache baseline. Additional MHA results validate the construction beyond GQA. GaugeRoPE achieves up to $2.48\times$ the decode throughput of the vanilla uncompressed baseline through direct latent execution.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: kv cache
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Yuanhang Gao, Xiangrui Yang, Lingyuan Meng, Yuanfeng Chen, Dongsheng Li
- 发布：2026-11-17；更新：2026-11-17
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
