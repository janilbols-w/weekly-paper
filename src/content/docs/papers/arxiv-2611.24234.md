---
title: "Hardware Acceleration of Vision-Language-Action Models with Weight Precision Rising over the Flow Steps"
description: "Vision-language-action (VLA) models such as GR00T control robots through an action head: a diffusion transformer that turns noise into a chunk of actions in a few flow-matching steps."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2611.24234) · [PDF](https://arxiv.org/pdf/2611.24234)

## 一句话摘要

Vision-language-action (VLA) models such as GR00T control robots through an action head: a diffusion transformer that turns noise into a chunk of actions in a few flow-matching steps.

## 为什么值得关注

待编辑增强。

## 摘要原文

Vision-language-action (VLA) models such as GR00T control robots through an action head: a diffusion transformer that turns noise into a chunk of actions in a few flow-matching steps. Every step re-reads all of the head's weights from DRAM but applies each weight to only about fifty tokens. Inference is therefore memory-bound, and its latency and energy are largely determined by the total number of transferred weight bits. We show that later flow steps attenuate the quantization errors of earlier steps, so the weight precision of an action head should rise over the steps. With plain per-channel rounding and without calibration or training, widths rising over the steps from 2 to 4 bits preserve the closed-loop success of robot policies. These widths transfer 25% fewer bits than 4-bit weights at every step. However, we show that on Jetson AGX Thor, current GPU kernels cannot exploit this per-step precision due to fixed overheads. We therefore present a programmable accelerator whose latency and energy both scale with the transferred weight bits. It decodes entropy-coded weights for bit-serial sub-arrays at the DRAM rate. Because the width changes per step, a run-time allocator divides these sub-arrays between the linear layers and the attention to balance their workloads. The same sub-arrays are thus capable of running action heads of different families and sizes, as well as a vision-language model. On the DRAM side, a requantizer and an entropy encoder at each bank let one stored 8-bit copy replace the copies of all widths. Simulated with LPDDR5X timing, our RTL implementation runs the GR00T N1.6 action head in 8.02 ms per inference with 2, 3, 3 and 4 bits in its four flow steps. With a copy per width and 50% of Thor's memory bandwidth, the accelerator runs this schedule 1.7x faster than Thor in NVFP4, at 9.1x less energy and equal closed-loop success.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 14 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Robin Geens, Simon Haepers, Jonas Crols, Chao Fang, Marian Verhelst
- 发布：2026-11-18；更新：2026-11-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
