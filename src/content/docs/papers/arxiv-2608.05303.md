---
title: "EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding"
description: "On-device deployment of Large Language Models (LLMs) has become essential for personalized edge applications."
---

**评分：47/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2608.05303) · [PDF](https://arxiv.org/pdf/2608.05303)

## 一句话摘要

On-device deployment of Large Language Models (LLMs) has become essential for personalized edge applications.

## 为什么值得关注

待编辑增强。

## 摘要原文

On-device deployment of Large Language Models (LLMs) has become essential for personalized edge applications. A primary bottleneck is external memory access (EMA) in feed-forward network (FFN) layers. Speculative decoding and mixture-of-experts (MoE) are promising solutions. Speculative decoding reduces the number of decoding stages by generating multiple tokens per stage, and MoE minimizes per-stage cost through sparse expert activation. However, there is an incompatibility when combining these two techniques. We propose EdgeXpert, a software-hardware co-designed LLM accelerator that resolves this incompatibility. In the prefill stage, the prompt-wise expert reuse reformulates routing as prompt-level expert reuse rather than independent per-token expert selection. It identifies important tokens using a lightweight encoder, constructs a shared expert set from them, and routes less important tokens with a reduced expert budget to lower expert EMA. In the decode stage, depth-aware expert coalescing exploits the contextual similarity and mutual exclusivity of same-depth candidate tokens. Rather than loading the union of all required channels, EdgeXpert loads only salient channels and applies computational calibration to recover accuracy without additional memory access. Synthesized in Samsung 28nm technology at 800 MHz, EdgeXpert achieves up to 56.3% latency reduction and 44.1% energy reduction compared to prior works, while maintaining near-baseline accuracy.

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

- 作者：Sangwoo Ha, Hyunwoo Seo, Yurim Jo, Youngjin Moon, Hoi-Jun Yoo
- 发布：2026-08-05；更新：2026-08-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
