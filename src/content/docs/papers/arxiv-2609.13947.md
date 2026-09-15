---
title: "Hardware-Aware Learned Representation Compression for Distributed In-Sensor Vision"
description: "In-sensor computing reduces the cost of transmitting high-resolution image data by performing early-stage processing near the sensor."
---

**评分：43/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.13947) · [PDF](https://arxiv.org/pdf/2609.13947)

## 一句话摘要

In-sensor computing reduces the cost of transmitting high-resolution image data by performing early-stage processing near the sensor.

## 为什么值得关注

待编辑增强。

## 摘要原文

In-sensor computing reduces the cost of transmitting high-resolution image data by performing early-stage processing near the sensor. However, the logic chip integrated with a CMOS image sensor (CIS) is tightly constrained in compute and memory, limiting conventional deep neural network partitioning. We present OASIS, a distributed in-sensor vision framework that uses a lightweight encoder to generate compact, task-relevant representations before off-chip transmission. The encoder is trained end-to-end using task, entropy, and reconstruction objectives, while the decoder is used only during training. OASIS supports two complementary deployment paths. The first applies 4-bit quantization and Huffman coding while preserving the spatial structure required by classification and dense-prediction tasks. The second uses Sobol-based hyperdimensional computing (HDC) to transform the encoder latent into a fixed-dimensional binary hypervector for associative-memory classification. For the SwinViT-based VWW model, mapping a $3\times3\times8$ latent to a 64-dimensional hypervector provides an additional $1.77\times$ communication reduction with less than one percentage point of accuracy loss relative to the 128-dimensional configuration, yielding an overall $18{,}816\times$ reduction compared with raw 8-bit image transmission. We implement the digital near-sensor pipeline on an AMD Xilinx Zynq UltraScale+ FPGA and characterize it using direct board-level power measurements and Vivado post-implementation analysis, together with circuit-simulated CIS models and a 7-nm ASIC projection. Across visual wake-word classification, hand tracking, and eye tracking, OASIS reduces total system energy by approximately $2\times$-$4.5\times$ while maintaining competitive accuracy, demonstrating a practical hardware-algorithm co-design path for communication-efficient in-sensor vision.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 6 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: hardware-aware
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Chengwei Zhou, Abu Masum, Xuming Chen, Mehran Moghadam, Sreetama Sarkar, Arnab Sanyal, Md Abdullah-Al Kaiser, M. Hassan Najafi, Sercan Aygun, Gourav Datta
- 发布：2026-09-15；更新：2026-09-15
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
