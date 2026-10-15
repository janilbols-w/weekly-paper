---
title: "Seeing at the Edge: Energy Characterization of Vision-Language Model Inference on Edge Platforms"
description: "Vision-language models (VLMs) are moving onto edge devices, but little is known about how much energy they draw on single-board computers with NPU or GPU accelerators, or where that energy goes."
---

**评分：39/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2610.20136) · [PDF](https://arxiv.org/pdf/2610.20136)

## 一句话摘要

Vision-language models (VLMs) are moving onto edge devices, but little is known about how much energy they draw on single-board computers with NPU or GPU accelerators, or where that energy goes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language models (VLMs) are moving onto edge devices, but little is known about how much energy they draw on single-board computers with NPU or GPU accelerators, or where that energy goes. We measure total-system energy, latency, and thermal behavior of Qwen2-VL-2B-Instruct and its text-only sibling on a Raspberry Pi 5 with a Hailo-10H NPU and on a Jetson Orin Nano Super, on both CPU and accelerator, and separate the fixed energy of each request from the energy that grows with output length. Because the accelerators use different quantization and serving software, we compare deployment stacks rather than silicon. Three findings stand out. First, NPU offloading makes the Pi a much more efficient VLM platform: it cuts energy per generated token by about two-thirds, leaves the host CPU largely free, and avoids the thermal throttling that the CPU backend reaches in sustained use. Second, an image adds both fixed and per-token energy, but at typical response lengths generating the answer costs far more than processing the image. Third, the Jetson GPU favors short responses through its lower fixed cost per request, whereas the Pi NPU favors longer ones through its lower cost per output token; their energy curves cross near 40 output tokens.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Junlin Liao, Harshit Kondle, Di Liu, Zonghua Gu
- 发布：2026-10-15；更新：2026-10-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
