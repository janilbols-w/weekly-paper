---
title: "Unlocking Lossless Speedups in LLMs via Discrete Diffusion"
description: "Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation."
---

**评分：43/100** · LLM 高效推理 > 模型与算法效率 > 推测解码

[论文原文](https://arxiv.org/abs/2609.04010) · [PDF](https://arxiv.org/pdf/2609.04010)

## 一句话摘要

Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation.

## 为什么值得关注

待编辑增强。

## 摘要原文

Large Language Models (LLMs) owe much of their success to next-token prediction (NTP), but their autoregressive (AR) structure requires slow, sequential token generation. To overcome this bottleneck, we introduce diffusion-augmented LLMs, a new class of models that defines an AR model distribution while using diffusion to draw multiple tokens in parallel from that distribution. We decouple the parameters of these models into two sets: AR weights, trained using the standard NTP objective, and lightweight diffusion weights, trained to generate multiple tokens simultaneously. The diffusion weights are learned through a simple Diffusion Distillation phase that adds negligible overhead to existing LLM training pipelines. We also introduce $\Psi$-Spec, a family of samplers that enables lossless acceleration and inference-time scaling at a fixed context length. Unlike speculative decoding, our method requires no separate draft model. Unlike diffusion LLMs (d-LLMs), it accelerates generation without sacrificing the quality of the underlying AR model. The resulting models, called Uno, can be trained from scratch or built by augmenting existing open-weight AR LLMs. Uno achieves higher throughput than leading speculative-decoding methods at every evaluated batch size and delivers up to $3\times$ speedups over the base AR model, including at the largest batch size supported by the device. Notably, our 8B Uno model outperforms the leading open d-LLM, the 26B DiffusionGemma, and the proprietary Mercury 2 across all evaluated benchmarks in agentic tool use, coding, and long-context reasoning. We release code and checkpoints at: https://s-sahoo.github.io/uno/

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: draft model, speculative decoding
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham, Jonathan Geuter, Chaitanya Dwivedi, Varad Pimpalkhute, Yash Akhauri, Alexander Moreno, Mikhail Yurochkin, Zhenting Wang, Mostafa Elhoushi, Nolan Dey, Shane Bergsma, Joel Hestness, John Thickstun, Eric Xing, Zhengzhong Liu
- 发布：2026-09-03；更新：2026-09-04
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
