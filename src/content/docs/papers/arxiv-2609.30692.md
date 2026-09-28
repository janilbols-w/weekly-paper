---
title: "LUMO (Lightweight Unified Multilingual Orchestrator): A Privacy Preserving Offline Voice Assistant"
description: "Reliable voice interaction is essential in environments with limited internet connectivity and strong privacy."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.30692) · [PDF](https://arxiv.org/pdf/2609.30692)

## 一句话摘要

Reliable voice interaction is essential in environments with limited internet connectivity and strong privacy.

## 为什么值得关注

待编辑增强。

## 摘要原文

Reliable voice interaction is essential in environments with limited internet connectivity and strong privacy. However, most existing voice assistants depend on cloud-based services, which leads to latency issues, dependency on internet access, and privacy vulnerabilities. This research presents LUMO (Lightweight Unified Multilingual Orchestrator), a privacy preserving offline voice assistant designed for edge computing environments. This system integrates local Automatic Speech Recognition (ASR), locally deployed quantized Large Language Model (LLM), and Text-to-Speech (TTS) synthesis into a fully offline pipeline running on a Raspberry Pi 5 with 8 GB RAM. To enable efficient operation on resource constrained hardware, the language model is compressed using 4-bit GGUF quantization, which reduces memory usage while preserving practical conversational capability. Existing edge based voice assistants Mycroft provides partial offline functionality without a generative LLM, with an approximate latency of ~5 s and power consumption of ~12 W, while Rhasspy supports full offline operation but lacks generative capabilities, with ~3 s latency and ~11 W power usage. In contrast, LUMO achieves a Word Error Rate (WER) of 6.8% for short English utterances in low noise conditions, an end-to-end response latency of 2.0-4.0 s, and a lower peak power consumption of approximately 9.0 W. The system also achieves effective offline recognition for Bangla speech, supporting multilingual accessibility in low resource settings. By operating entirely offline, LUMO provides strong data privacy, reduced need for cloud connectivity, and suitability for privacy sensitive edge execution such as rural healthcare, education, and disaster response scenarios.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 14 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Md. Mehedi Hasan Naeem, Mst. Kamrunnahar Ruma, Nafiza Anjum, Shakila Sultana, Md. Sujan Ali
- 发布：2026-09-28；更新：2026-09-28
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
