---
title: "Energy Overhead in Sensor Nodes: Embedded Machine Learning and Data Offloading via Low Power Wide Area Networks"
description: "Image- and audio-based remote IoT applications offer a substantial opportunity to address ecological changes."
---

**评分：43/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2510.24829) · [PDF](https://arxiv.org/pdf/2510.24829)

## 一句话摘要

Image- and audio-based remote IoT applications offer a substantial opportunity to address ecological changes.

## 为什么值得关注

待编辑增强。

## 摘要原文

Image- and audio-based remote IoT applications offer a substantial opportunity to address ecological changes. However, to be effective, they must operate for long periods on limited power while also providing data via LPWAN. Previous studies have investigated the energy efficiency of isolated components such as radio transmission or data processing methods within an IoT system. However, a holistic evaluation is required to determine the main drivers of energy consumption in sensor nodes. To address this, we systematically analyze energy consumption across the entire sensor-node pipeline, from data acquisition to optional on-device CNN classification and wireless network transmission, using an ESP32-S3 microcontroller. We compare on-device CNN classification followed by result transmission with transmitting raw sensor data across three environmental monitoring scenarios. Thereby, we vary developer-controllable variables, notably the model architecture and the LPWAN technologies (LTE-M, NB-IoT, LoRaWAN). Our results indicate that on-device inference can reduce sensor node energy consumption by 1.7x to 6.9x compared to raw data transmission, depending on transmission frequency, with an acceptable loss in accuracy. Further, our results narrow down the energy tradeoff to variables IoT developers can control. Therefore, our findings provide empirical guidance for designing energy-efficient, long-range sensing systems and demonstrate that TinyML enables sustainable, autonomous deployments.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 5 |
| rigor | 7 |
| practical impact | 10 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- quantitative claim detected
- no code link detected in metadata

## 元数据

- 作者：Benjamin Karic, Nina Herrmann, Jan Stenkamp, Paula Scharf, Fabian Gieseke, Angela Schwering
- 发布：2026-10-19；更新：2026-10-19
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
