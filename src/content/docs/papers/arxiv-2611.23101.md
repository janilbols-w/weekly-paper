---
title: "StreamingDPD: A 1.28-GSa/s Instantaneous-Power-Gated Depthwise TCN Accelerator for Real-Time 320-MHz Digital Predistortion"
description: "State feedback between successive samples limits the streaming throughput of recurrent neural networks for digital predistortion (DPD)."
---

**评分：54/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.23101) · [PDF](https://arxiv.org/pdf/2611.23101)

## 一句话摘要

State feedback between successive samples limits the streaming throughput of recurrent neural networks for digital predistortion (DPD).

## 为什么值得关注

待编辑增强。

## 摘要原文

State feedback between successive samples limits the streaming throughput of recurrent neural networks for digital predistortion (DPD). We present StreamingDPD, an accelerator that processes 320-MHz signals at 1.28 GSa/s. Its 207-parameter instantaneous-power-gated depthwise temporal convolutional network (IPG-DWTCN) uses $|x[n]|^2$ to gate feature channels and causal dilated depthwise convolutions to model power amplifier memory. The network maps to a spatially unrolled fixed-point pipeline with shift-based quadratic activations and layer-wise mixed precision, sustaining one complex sample per cycle per lane. Its algorithmic cost is 554 floating-point operations per complex sample, 30.1% fewer than the recurrent baseline with the best linearization performance. In RF playback measurements on three power amplifiers driven by 40- to 320-MHz Wi-Fi 6/7 and 5G NR waveforms, IPG-DWTCN achieves the lowest mean adjacent-channel power ratio (ACPR) and ranks first or ties for first in mean error vector magnitude (EVM) against five neural baselines of comparable size. Four-lane FPGA hardware-in-the-loop tests on a 320-MHz 4096-QAM Wi-Fi 7 waveform achieve -45.82 dBc ACPR and -42.94 dB EVM at 1.28 GSa/s. At the same sample rate, post-layout evaluation of a single-lane 12-nm FinFET ASIC yields a 0.10 mm$^2$ core, a 52-cycle (40.63 ns) latency, and an estimated typical-corner power of 142.21 mW (111.10 pJ/sample). Relative to the prior 22-nm recurrent DPD ASIC, the design provides 5.1 times the throughput at about one-seventh the energy per sample.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 18 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Yizhuo Wu, Xinling Wang, Chang Gao
- 发布：2026-11-17；更新：2026-11-18
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
