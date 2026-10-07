---
title: "Offline AI Modules: Voice-First Offline Architecture, Hardware Reference Stack, Quantization and Benchmarking"
description: "The Offline AI Modules workstream enables practical, low-power, and community-accessible deployment of voice-first AI systems that operate fully offline."
---

**评分：52/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2610.07026) · [PDF](https://arxiv.org/pdf/2610.07026)

## 一句话摘要

The Offline AI Modules workstream enables practical, low-power, and community-accessible deployment of voice-first AI systems that operate fully offline.

## 为什么值得关注

待编辑增强。

## 摘要原文

The Offline AI Modules workstream enables practical, low-power, and community-accessible deployment of voice-first AI systems that operate fully offline. Designed for African language communities where speech is the dominant mode of interaction and internet connectivity is unreliable or absent, the workstream delivers three reinforcing components: a modular voice-first offline architecture, a low-cost hardware reference bill of materials, and a reproducible quantization and a reproducible quantization and benchmarking pipeline for instruction-tuned language models in the 2-5B parameter class. This paper presents the first end-to-end benchmark evaluation of the stack across two hardware tiers: an NVIDIA Jetson Orin NX (TierB) and a Raspberry Pi5 (TierA). Three instruction-tuned models are evaluated across four quantization formats, assessed for deployment metrics (decode throughput, chat latency, memory, power) and multilingual quality (topic classification accuracy on MasakhaNEWS across English, Hausa, Igbo, Nigerian Pidgin, and Yoruba; per-language perplexity drift). Speech recognition is evaluated using Ethio-ASR on Amharic and Oromo across both tiers. The principal finding is that Q4_K_M quantization represents the best size-to-quality trade-off for deployment on both tiers: gemma-4-E2B-it achieves 28.8t/s decode throughput and 89.2% topic classification accuracy at Q4_K_M on TierB, while all three models run within the 16GB memory budget on TierA.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 11 |
| practical impact | 13 |
| reproducibility | 3 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Sunday Afariogun, Odunolaoluwa Jenrola, Zeinab Nezami
- 发布：2026-10-07；更新：2026-10-07
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
