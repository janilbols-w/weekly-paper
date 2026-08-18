---
title: "Hardware-in-the-Loop Phase-Aware CNN for Real-Time 5G Channel Estimation"
description: "This demo presents real-time AI-based uplink channel-estimation inference using data collected from a hardware-in-the-loop 5G platform."
---

**评分：38/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2608.14709) · [PDF](https://arxiv.org/pdf/2608.14709)

## 一句话摘要

This demo presents real-time AI-based uplink channel-estimation inference using data collected from a hardware-in-the-loop 5G platform.

## 为什么值得关注

待编辑增强。

## 摘要原文

This demo presents real-time AI-based uplink channel-estimation inference using data collected from a hardware-in-the-loop 5G platform. The data-collection setup integrates commercial RF signal generation, programmable channel emulation, an O-RAN Radio Unit, DU emulation, and a lightweight phase-aware convolutional neural network (CNN) that estimates the channel response directly from received DMRS signals. Unlike simulation-only evaluations, the hardware-derived dataset exposes the estimator to practical RF and system-level impairments, including calibration mismatches, synchronization imperfections, quantization effects, phase noise, and implementation-specific nonlinearities. During the demo, attendees will observe real-time CNN inference and channel reconstruction using captured hardware-generated DMRS observations and compare the proposed CNN against Least Squares (LS) and frequency-domain LMMSE baselines. The objective is to showcase a practical AI-native physical-layer inference pipeline that combines hardware-derived 5G data with real-time neural channel estimation for future 5G-Advanced and 6G systems.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 11 |
| practical impact | 5 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Javad Zolfaghari-Bengar, Rakibul Rony, Elisa Gomez-de-Lope, Alejandro Villena-Rodriguez, Abhinav Mahadevan, Nicolas Kourtellis
- 发布：2026-08-18；更新：2026-08-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
