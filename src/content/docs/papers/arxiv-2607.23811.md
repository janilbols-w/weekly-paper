---
title: "Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers"
description: "Siri Expressive Voices synthesize rich, configurable speech in real time and entirely on device, powered by AFM 3 Core Advanced, Apple's most powerful on-device foundation model."
---

**评分：39/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2607.23811) · [PDF](https://arxiv.org/pdf/2607.23811)

## 一句话摘要

Siri Expressive Voices synthesize rich, configurable speech in real time and entirely on device, powered by AFM 3 Core Advanced, Apple's most powerful on-device foundation model.

## 为什么值得关注

待编辑增强。

## 摘要原文

Siri Expressive Voices synthesize rich, configurable speech in real time and entirely on device, powered by AFM 3 Core Advanced, Apple's most powerful on-device foundation model. This work presents the memory-efficient audio synthesis architecture behind that capability: a detokenizer that converts the semantic audio tokens emitted by the foundation model into high-fidelity audio within the tight compute and memory budget of the Scalable Matrix Extension (SME). We convert semantic audio tokens to a residual vector quantization (RVQ) representation with a three-component design, a streaming encoder, a temporal decoder, and a depth decoder, that systematically decouples temporal and depth processing. A single reusable depth decoder with Diffusion Transformer (DiT)-style stage conditioning generates all RVQ levels autoregressively, replacing the dedicated per-level decoders of prior multi-decoder architectures, while causal sliding window attention with fixed-window key-value caching yields constant memory complexity independent of sequence length. Deployed on the AMX, the detokenizer sustains roughly 10 ms per generation step, about 16x faster than real time, with a peak runtime memory of only 21 MB and 329 MB of on-device assets, enabling continuous streaming synthesis of 20-320 seconds of audio. This constant, small footprint replaces the linear and quadratic memory scaling of conventional transformer- and GAN-based approaches. Ablation studies validate the key architectural components, and audio quality assessment confirms that the architecture maintains synthesis fidelity while achieving efficiency gains over existing methods. Operating at a 1-billion-parameter activation size within AFM 3 Core Advanced, it improves Mean Opinion Score by +0.28 overall (4.15 vs. 3.87) and by +0.42 on conversational speech (4.24 vs. 3.82) over the prior on-device text-to-speech system.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Dongseong Hwang, Prasanth Yadla, Kaan Elgin, Shifas Padinjaru Veettil, Sivanand Achanta, Dipjyoti Paul, Ramya Rasipuram, Tyler Johnson, Emad Soroush, Chung-Cheng Chiu, Zhifeng Chen
- 发布：2026-11-03；更新：2026-11-03
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
