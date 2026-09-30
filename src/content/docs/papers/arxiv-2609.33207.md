---
title: "MorphAtt: A Neuromorphic Accelerator for Efficient Multi-Head Attention Processing in Spiking Vision Transformers"
description: "Spiking Vision Transformers (SViTs) are developed as an energy-efficient alternative to conventional ViTs for computer vision tasks at the edge."
---

**评分：44/100** · LLM 高效推理 > Serving 与分布式推理 > 硬件感知与边缘推理

[论文原文](https://arxiv.org/abs/2609.33207) · [PDF](https://arxiv.org/pdf/2609.33207)

## 一句话摘要

Spiking Vision Transformers (SViTs) are developed as an energy-efficient alternative to conventional ViTs for computer vision tasks at the edge.

## 为什么值得关注

待编辑增强。

## 摘要原文

Spiking Vision Transformers (SViTs) are developed as an energy-efficient alternative to conventional ViTs for computer vision tasks at the edge. However, huge parameter counts and complex multi-head self-attention (MHSA) operations make it challenging to achieve high energy efficiency in SViT inference, especially in tightly constrained applications. To maximize efficiency gains of SViT processing, we propose MorphAtt, a novel digital accelerator that expedites SViT inference through streamlined processing. Specifically, it processes MHSA operations using cascaded hardware modules: a Spiking Query-Key-Value generator (SpikeQKV), a low-complexity Spiking Multi-Head Self-Attention engine (SpikeAtten), and Reparameterization Convolution (RepConv) modules. To mitigate traffic congestion in on-chip memory accesses and data reuse, specialized inter-module buffers are integrated within the dataflow. Under synthesis using 32nm CMOS technology, MorphAtt achieves 792-1605 GOPS of throughput, while incurring ~39-55 mW of power consumption and 1.5 mm^2 of area, which lead to 20.3-29.1 TOPS/W of energy efficiency. These results also demonstrate that our MorphAtt offers better performance and efficiency trade-offs than state-of-the-art, thereby enabling highly energy-efficient vision-based AI systems at the edge.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 16 |
| novelty | 7 |
| rigor | 5 |
| practical impact | 11 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: accelerator
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Rachmad Vidya Wicaksana Putra, Amirhesam Jafari Rad, Muhammad Shafique
- 发布：2026-09-30；更新：2026-09-30
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
