---
title: "The Battery Price of edge AI: A study of the Environmental Impact of LLM Inference on Mobile Devices"
description: "The rapid diffusion of generative artificial intelligence raises privacy, latency, and performance concerns that motivate a shift toward \"local-first\" AI, where inferences are performed on the user's device instead of on remote cloud servers."
---

**评分：42/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.11940) · [PDF](https://arxiv.org/pdf/2609.11940)

## 一句话摘要

The rapid diffusion of generative artificial intelligence raises privacy, latency, and performance concerns that motivate a shift toward "local-first" AI, where inferences are performed on the user's device instead of on remote cloud servers.

## 为什么值得关注

待编辑增强。

## 摘要原文

The rapid diffusion of generative artificial intelligence raises privacy, latency, and performance concerns that motivate a shift toward "local-first" AI, where inferences are performed on the user's device instead of on remote cloud servers. This paradigm also places a significant computational load on battery-powered smartphones, potentially shortening battery life and increasing the overall replacement rate of mobile devices. This paper presents a systematic study of the energy consumption, performance, and accuracy of on-device large language model (LLM) inference. We evaluate 18 models from different model families, sizes, and quantization levels, on two modern smartphones and on a server, using the respective state-of-the-art for such deployments. We measure the energy per generated token, inter-token latency, model accuracy, and battery-cycle consumption. Our results show that (i) on-device inference is on average 3 times less energy-efficient than batched server inference; (ii) the relationship between quantization bit-width and energy per token is non-monotonic, with energy sweet spots on both tested smartphones; (iii) eight out of 18 model configurations lie on the Pareto front of accuracy and energy-efficiency, allowing practitioners to build battery-aware model routers; and (iv) realistic modeling assumptions do not allow local inference to be less environmentally impacting per token than batched server inference, with 88--90% of that impact attributable to device embodied carbon rather than electricity consumption. These findings challenge the premise that local AI is more sustainable than cloud inference, and motivate the need for context-aware and life-cycle-aware model selection when deploying edge AI on battery-powered mobile platforms.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 7 |
| practical impact | 12 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：\'Edouard Gu\'egain, Tristan Coignion
- 发布：2026-09-14；更新：2026-09-14
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
