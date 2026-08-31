---
title: "Accelerating Data Preprocessing for Efficient Vision Model Inference on Jetson Edge Device"
description: "Data preprocessing is a crucial part of deep learning workflows on edge devices."
---

**评分：42/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2608.27655) · [PDF](https://arxiv.org/pdf/2608.27655)

## 一句话摘要

Data preprocessing is a crucial part of deep learning workflows on edge devices.

## 为什么值得关注

待编辑增强。

## 摘要原文

Data preprocessing is a crucial part of deep learning workflows on edge devices. However, decoding data saved in JPEG format is very compute-intensive and occupies a major portion of the preprocessing pipeline. Therefore, increasing the decoding speed is vital for improving overall throughput, especially for inputs with large image sizes, which are often subject to preprocessing bottlenecks. On the other hand, edge devices are equipped with specialized hardware units to accelerate media processing and image decoding. For instance, the NVIDIA Jetson platform possesses a dedicated NVJPEG unit. These units can be used to enhance the performance of the preprocessing pipeline. This paper introduces the utilization of such specific hardware acceleration units for offloading decoding tasks. By combining this with a multi-instance approach, it allows for the parallelization of all compute resources including CPU, NVJPEG, GPU, and DLA in Jetson devices. In this work, we compare various potential pipeline designs. On ResNet18, ResNet50, and ResNet152, three models with different sizes, we evaluate the impact of batch sizes and image sizes, as well as the characteristics of GPU/DLA inference. Finally, a fine-tuning experiment for multi-instance design has been conducted. The multi-instance design with a specific hardware decoding unit involved offers up to 30.02% speedup for large image sizes, compared with the most optimized design without it. Based on these findings, we demonstrate the benefits of using the NVJPEG unit in deep learning workflows and provide guidelines for tuning and optimizing edge inference workflows.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 5 |
| rigor | 9 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Tian Chen (DK), Nawras Alnaasan (DK), Jinghan Yao (DK), Aamir Shafi (DK), Hari Subramoni (DK), Dhabaleswar K. (DK), Panda
- 发布：2026-08-31；更新：2026-08-31
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
