---
title: "ViTrail: Transmission-Inference Co-Design for Vision Transformer-Based Mobile Video Analytics"
description: "Edge-assisted mobile video analytics (MVA) relies on a tight device-edge feedback loop in which captured frames are transmitted for remote inference and the returned results are rendered on the mobile device."
---

**评分：41/100** · LLM 高效推理 > Runtime 与内存效率 > 缓存、换入换出与内存管理

[论文原文](https://arxiv.org/abs/2601.21362) · [PDF](https://arxiv.org/pdf/2601.21362)

## 一句话摘要

Edge-assisted mobile video analytics (MVA) relies on a tight device-edge feedback loop in which captured frames are transmitted for remote inference and the returned results are rendered on the mobile device.

## 为什么值得关注

待编辑增强。

## 摘要原文

Edge-assisted mobile video analytics (MVA) relies on a tight device-edge feedback loop in which captured frames are transmitted for remote inference and the returned results are rendered on the mobile device. Many existing systems optimize frame transmission while treating server-side inference as a fixed cost. This separation becomes inefficient for vision transformer (ViT)-based dense prediction, where high-resolution inputs simultaneously increase network traffic and server computation. We present ViTrail, which co-designs transmission and ViT inference through a shared mixed-resolution representation. The device preserves task-relevant regions at full resolution and downsamples less informative regions before encoding. The server tokenizes each region at its transmitted resolution, so the same regional resolution assignment reduces both the upload payload and the number of tokens processed by the ViT. For dense prediction, ViTrail aligns regions with ViT patches and attention windows and restores a regular feature grid at a configurable stage. At runtime, it selects regional downsampling, compression quality, and the restoration point to maximize predicted installation accuracy, the accuracy of the rendered result when a new remote result is first used for rendering. We build a fully functional prototype on commodity mobile and edge devices and evaluate it in real time across 300 video-trace pairs with real-world 4G/5G traces. ViTrail achieves the highest mean rendering accuracy among the evaluated systems and leads each baseline on 81% to 95% of pairs, while reducing median end-to-end offloading latency by 38% against the most accurate baseline.

## 质量评分

| 维度 | 得分 |
|---|---:|
| relevance | 12 |
| novelty | 6 |
| rigor | 9 |
| practical impact | 9 |
| reproducibility | 2 |
| credibility | 3 |

## 证据与限制

- taxonomy keywords: offloading
- no quantitative claim in metadata
- no code link detected in metadata

## 元数据

- 作者：Miao Zhang, Guanzhen Wu, Hao Fang, Yifei Zhu, Fangxin Wang, Ruixiao Zhang, Linfeng Shen, Jiangchuan Liu
- 发布：2026-11-25；更新：2026-11-25
- 来源：arXiv RSS；Venue：未确认
- 代码：未发现
- 阅读深度：metadata
