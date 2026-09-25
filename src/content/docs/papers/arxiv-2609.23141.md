---
title: "Real-Time Plasma State Prediction via FPGA-Accelerated Quantized Recurrent Probabilistic Neural Networks"
description: "Real time plasma state estimation for control of Tokamak devices are challenging due to the stringent latency requirements of the plasma control system (PCS)."
---

**评分：40/100** · LLM 高效推理 > 模型与算法效率 > 量化与低精度

[论文原文](https://arxiv.org/abs/2609.23141) · [PDF](https://arxiv.org/pdf/2609.23141)

## 一句话摘要

Real time plasma state estimation for control of Tokamak devices are challenging due to the stringent latency requirements of the plasma control system (PCS).

## 为什么值得关注

待编辑增强。

## 摘要原文

Real time plasma state estimation for control of Tokamak devices are challenging due to the stringent latency requirements of the plasma control system (PCS). We present an end-to-end workflow for deploying a recurrent probabilistic neural network (RPNN) on FPGA hardware. We combine architecture size reduction with quantization-aware training via QKeras. The model is then synthesized using hls4ml, targeting a Xilinx Alveo U50 device. We report a design that fits comfortably within all four resource budgets (DSP, LUT, FF, BRAM) at deterministic sub-10~$\mu$s single-timestep latency, meeting the requirements for real-time inference inside a model-predictive-control-style plasma control loop.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 18 |
| novelty | 5 |
| rigor | 5 |
| practical impact | 7 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: quantization, quantized
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Daniel Gaytan-Villarreal, Aiken Xie, Tu Pham, Rohit Sonker, Chiara Amendola, Matteo Cremonesi, Cong Hao, Jeff Schneider
- 发布：2026-09-19；更新：2026-09-22
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
